require_relative "lib/crawlora/reelshort/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-reelshort"
  spec.version = Crawlora::Reelshort::VERSION
  spec.summary = "ReelShort API client for Crawlora (11 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted ReelShort API. Covers title discovery, search, movie details, new releases, and public Fandom articles across 11 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=reelshort-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-reelshort", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-reelshort/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
