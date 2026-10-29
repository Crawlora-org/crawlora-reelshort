# Crawlora ReelShort API client for Ruby (`crawlora-reelshort`)

This Ruby gem calls Crawlora's hosted ReelShort API at `https://api.crawlora.net/api/v1`. It exposes 11 endpoints covering title discovery, search, movie details, new releases, and public Fandom articles; it does not call or scrape ReelShort directly. Requests require your Crawlora API key and use your account's service plan.

## Install

```ruby
gem "crawlora-reelshort"
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=reelshort-ruby-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=reelshort-ruby-console) to get an API key, and set `CRAWLORA_API_KEY` before running the client:

```ruby
require "json"
require "crawlora/reelshort"

client = Crawlora::Reelshort::Client.new
result = client.request("reelshort-search", JSON.parse("{\"keywords\": \"sample\"}"))
puts result
client.close
```

Use an operation-specific method for normal calls. `request(operation_id, params = {}, response_type: :auto)` is available for every operation. `response_type: :text` returns raw response text. This gem includes 11 API operations.

```ruby
client = Crawlora::Reelshort::Client.new(api_key: ENV.fetch("CRAWLORA_API_KEY"), timeout: 30)
# client.<operation_method>(<endpoint parameters>)
client.close
```

Client options include `api_key`, `base_url`, and `timeout`. Ruby stdlib provides the HTTP and JSON support.

## Supported ReelShort API endpoints

Browse every route included in this gem. The [endpoint reference](https://github.com/Crawlora-org/crawlora-reelshort/blob/main/docs/usage.md) includes parameter and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/reelshort/fandom-categories` | `reelshort-fandom-categories` | List ReelShort Fandom's article categories |
| `GET` | `/reelshort/fandom-post` | `reelshort-fandom-post` | Get a ReelShort Fandom article |
| `GET` | `/reelshort/fandom-posts` | `reelshort-fandom-posts` | List ReelShort Fandom articles |
| `GET` | `/reelshort/home` | `reelshort-home` | List ReelShort's home page shelves |
| `GET` | `/reelshort/movie` | `reelshort-movie` | Get a ReelShort short drama and its episodes |
| `GET` | `/reelshort/new-releases` | `reelshort-new-releases` | List ReelShort's curated New Release titles |
| `GET` | `/reelshort/search` | `reelshort-search` | Search ReelShort short dramas by title |
| `GET` | `/reelshort/shelf` | `reelshort-shelf` | Get a whole ReelShort shelf |
| `GET` | `/reelshort/tag-books` | `reelshort-tag-books` | List the ReelShort titles carrying a tag |
| `GET` | `/reelshort/tag-search` | `reelshort-tag-search` | Search ReelShort tags by text |
| `GET` | `/reelshort/tags` | `reelshort-tags` | List ReelShort's featured tags in one category |

See [Crawlora](https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=reelshort-ruby-homepage), the [API documentation](https://crawlora.net/docs?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=reelshort-ruby-api-docs), and [the package repository](https://github.com/Crawlora-org/crawlora-reelshort) for account setup, the API operation reference, and release history.
