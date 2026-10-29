require "json"
require "net/http"
require "uri"

module Crawlora
  module Reelshort
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"reelshort-fandom-categories": {"bodyParam": null, "bodyRequired": false, "id": "reelshort-fandom-categories", "method": "GET", "params": [], "path": "/reelshort/fandom-categories", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "reelshort-fandom-post": {"bodyParam": null, "bodyRequired": false, "id": "reelshort-fandom-post", "method": "GET", "params": [{"description": "Article id (digits), article slug, or a reelshort.com/fandom URL", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "54181"}], "path": "/reelshort/fandom-post", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "reelshort-fandom-posts": {"bodyParam": null, "bodyRequired": false, "id": "reelshort-fandom-posts", "method": "GET", "params": [{"description": "Text to search articles for, up to 100 characters", "in": "query", "name": "search", "type": "string", "x-example": "alpha"}, {"description": "Category slug: general-topic, movie-cast-list, top-movie-stories, where-to-watch or where-to-watch-2", "enum": ["general-topic", "movie-cast-list", "top-movie-stories", "where-to-watch", "where-to-watch-2"], "in": "query", "name": "category", "type": "string", "x-example": "movie-cast-list"}, {"description": "Page number, 1 to 10000; defaults to 1", "in": "query", "name": "page", "type": "integer", "x-example": 2}, {"description": "Page size, 1 to 100; defaults to 10", "in": "query", "name": "limit", "type": "integer", "x-example": 10}], "path": "/reelshort/fandom-posts", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "search", "type": "string"}, {"enum": ["general-topic", "movie-cast-list", "top-movie-stories", "where-to-watch", "where-to-watch-2"], "in": "query", "name": "category", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "reelshort-home": {"bodyParam": null, "bodyRequired": false, "id": "reelshort-home", "method": "GET", "params": [{"description": "Site locale, one of: en, es, pt, fr, de, it, ja, ko, th, id, tr, ar, ru, pl, ro, cs, bg, vi, zh-TW; defaults to en. Titles and tags are translated", "enum": ["en", "es", "pt", "fr", "de", "it", "ja", "ko", "th", "id", "tr", "ar", "ru", "pl", "ro", "cs", "bg", "vi", "zh-TW"], "in": "query", "name": "language", "type": "string", "x-example": "es"}], "path": "/reelshort/home", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["en", "es", "pt", "fr", "de", "it", "ja", "ko", "th", "id", "tr", "ar", "ru", "pl", "ro", "cs", "bg", "vi", "zh-TW"], "in": "query", "name": "language", "type": "string"}], "security": ["ApiKeyAuth"]}, "reelshort-movie": {"bodyParam": null, "bodyRequired": false, "id": "reelshort-movie", "method": "GET", "params": [{"description": "Title id (24 hex characters) from reelshort-home, reelshort-shelf or reelshort-search, or a reelshort.com movie or episode URL", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "6a8752ac7c23cb02b40f062b"}], "path": "/reelshort/movie", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "reelshort-new-releases": {"bodyParam": null, "bodyRequired": false, "id": "reelshort-new-releases", "method": "GET", "params": [{"description": "A 24-character title id, from reelshort-movie, reelshort-shelf or reelshort-home; required by ReelShort but not observed to change the result", "in": "query", "name": "book_id", "required": true, "type": "string", "x-example": "6aac85383511c0b6df0eec87"}, {"description": "Site language, one of en, es, pt, fr, de, it, ja, ko, th, id, tr, ar, ru, pl, ro, cs, bg, vi, zh-TW; defaults to en", "enum": ["en", "es", "pt", "fr", "de", "it", "ja", "ko", "th", "id", "tr", "ar", "ru", "pl", "ro", "cs", "bg", "vi", "zh-TW"], "in": "query", "name": "language", "type": "string", "x-example": "en"}], "path": "/reelshort/new-releases", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "book_id", "required": true, "type": "string"}, {"enum": ["en", "es", "pt", "fr", "de", "it", "ja", "ko", "th", "id", "tr", "ar", "ru", "pl", "ro", "cs", "bg", "vi", "zh-TW"], "in": "query", "name": "language", "type": "string"}], "security": ["ApiKeyAuth"]}, "reelshort-search": {"bodyParam": null, "bodyRequired": false, "id": "reelshort-search", "method": "GET", "params": [{"description": "Title text to search for, up to 100 characters", "in": "query", "name": "keywords", "required": true, "type": "string", "x-example": "billionaire"}, {"description": "Page number, 1 to 200; defaults to 1. Each page holds 12 titles", "in": "query", "name": "page", "type": "integer", "x-example": 2}, {"description": "Site locale, one of: en, es, pt, fr, de, it, ja, ko, th, id, tr, ar, ru, pl, ro, cs, bg, vi, zh-TW; defaults to en. Titles and tags are translated", "enum": ["en", "es", "pt", "fr", "de", "it", "ja", "ko", "th", "id", "tr", "ar", "ru", "pl", "ro", "cs", "bg", "vi", "zh-TW"], "in": "query", "name": "language", "type": "string", "x-example": "es"}], "path": "/reelshort/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keywords", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"enum": ["en", "es", "pt", "fr", "de", "it", "ja", "ko", "th", "id", "tr", "ar", "ru", "pl", "ro", "cs", "bg", "vi", "zh-TW"], "in": "query", "name": "language", "type": "string"}], "security": ["ApiKeyAuth"]}, "reelshort-shelf": {"bodyParam": null, "bodyRequired": false, "id": "reelshort-shelf", "method": "GET", "params": [{"description": "Shelf id from reelshort-home (for example 51003506), or a reelshort.com shelf URL", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "51003506"}], "path": "/reelshort/shelf", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "reelshort-tag-books": {"bodyParam": null, "bodyRequired": false, "id": "reelshort-tag-books", "method": "GET", "params": [{"description": "Tag id, 24 lowercase hex characters, from reelshort-tags, reelshort-tag-search or reelshort-movie", "in": "query", "name": "tag_id", "required": true, "type": "string", "x-example": "676d210e4582b53a14081aab"}, {"description": "Page number, 1 to 10000; defaults to 1", "in": "query", "name": "page", "type": "integer", "x-example": 1}, {"description": "Page size, 1 to 100; defaults to 20", "in": "query", "name": "limit", "type": "integer", "x-example": 20}, {"description": "Site language, one of en, es, pt, fr, de, it, ja, ko, th, id, tr, ar, ru, pl, ro, cs, bg, vi, zh-TW; defaults to en", "enum": ["en", "es", "pt", "fr", "de", "it", "ja", "ko", "th", "id", "tr", "ar", "ru", "pl", "ro", "cs", "bg", "vi", "zh-TW"], "in": "query", "name": "language", "type": "string", "x-example": "en"}], "path": "/reelshort/tag-books", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "tag_id", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"enum": ["en", "es", "pt", "fr", "de", "it", "ja", "ko", "th", "id", "tr", "ar", "ru", "pl", "ro", "cs", "bg", "vi", "zh-TW"], "in": "query", "name": "language", "type": "string"}], "security": ["ApiKeyAuth"]}, "reelshort-tag-search": {"bodyParam": null, "bodyRequired": false, "id": "reelshort-tag-search", "method": "GET", "params": [{"description": "Tag text to search for, up to 100 characters", "in": "query", "name": "word", "required": true, "type": "string", "x-example": "Billionaire"}, {"description": "Page number, 1 to 10000; defaults to 1", "in": "query", "name": "page", "type": "integer", "x-example": 1}, {"description": "Site language, one of en, es, pt, fr, de, it, ja, ko, th, id, tr, ar, ru, pl, ro, cs, bg, vi, zh-TW; defaults to en", "enum": ["en", "es", "pt", "fr", "de", "it", "ja", "ko", "th", "id", "tr", "ar", "ru", "pl", "ro", "cs", "bg", "vi", "zh-TW"], "in": "query", "name": "language", "type": "string", "x-example": "en"}], "path": "/reelshort/tag-search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "word", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"enum": ["en", "es", "pt", "fr", "de", "it", "ja", "ko", "th", "id", "tr", "ar", "ru", "pl", "ro", "cs", "bg", "vi", "zh-TW"], "in": "query", "name": "language", "type": "string"}], "security": ["ApiKeyAuth"]}, "reelshort-tags": {"bodyParam": null, "bodyRequired": false, "id": "reelshort-tags", "method": "GET", "params": [{"description": "Tag category: actor, actress, identity or trope", "enum": ["actor", "actress", "identity", "trope"], "in": "query", "name": "category", "required": true, "type": "string", "x-example": "identity"}, {"description": "Site language, one of en, es, pt, fr, de, it, ja, ko, th, id, tr, ar, ru, pl, ro, cs, bg, vi, zh-TW; defaults to en", "enum": ["en", "es", "pt", "fr", "de", "it", "ja", "ko", "th", "id", "tr", "ar", "ru", "pl", "ro", "cs", "bg", "vi", "zh-TW"], "in": "query", "name": "language", "type": "string", "x-example": "en"}], "path": "/reelshort/tags", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["actor", "actress", "identity", "trope"], "in": "query", "name": "category", "required": true, "type": "string"}, {"enum": ["en", "es", "pt", "fr", "de", "it", "ja", "ko", "th", "id", "tr", "ar", "ru", "pl", "ro", "cs", "bg", "vi", "zh-TW"], "in": "query", "name": "language", "type": "string"}], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["reelshort-fandom-categories", "reelshort-fandom-post", "reelshort-fandom-posts", "reelshort-home", "reelshort-movie", "reelshort-new-releases", "reelshort-search", "reelshort-shelf", "reelshort-tag-books", "reelshort-tag-search", "reelshort-tags"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-reelshort-ruby/0.1.0", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        payload = request_body(operation, normalized)
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = operation["method"] == "POST" ? Net::HTTP::Post.new(uri) : Net::HTTP::Get.new(uri)
        unless payload.nil?
          request.body = payload
          request["Content-Type"] = "application/json"
        end
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = if operation["method"] == "POST"
              @transport.call(url, request.to_hash, @timeout, "POST", payload)
            else
              @transport.call(url, request.to_hash, @timeout)
            end
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('fandom_categories') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reelshort-fandom-categories', params, response_type: response_type)
      end
      define_method('fandom_post') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reelshort-fandom-post', params, response_type: response_type)
      end
      define_method('fandom_posts') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reelshort-fandom-posts', params, response_type: response_type)
      end
      define_method('home') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reelshort-home', params, response_type: response_type)
      end
      define_method('movie') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reelshort-movie', params, response_type: response_type)
      end
      define_method('new_releases') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reelshort-new-releases', params, response_type: response_type)
      end
      define_method('search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reelshort-search', params, response_type: response_type)
      end
      define_method('shelf') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reelshort-shelf', params, response_type: response_type)
      end
      define_method('tag_books') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reelshort-tag-books', params, response_type: response_type)
      end
      define_method('tag_search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reelshort-tag-search', params, response_type: response_type)
      end
      define_method('tags') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reelshort-tags', params, response_type: response_type)
      end

      private

      # POST operations take their JSON body under the body parameter name or "body".
      def request_body(operation, params)
        name = operation["bodyParam"]
        return nil if name.nil?
        value = params.key?(name) ? params[name] : params["body"]
        if value.nil?
          raise Errors::ClientError.new("missing request body: #{name}", operation_id: operation["id"]) if operation["bodyRequired"]
          return nil
        end
        value.is_a?(String) ? value : JSON.generate(value)
      end

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        known << "body" if operation["bodyParam"]
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end
