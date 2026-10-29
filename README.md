# ReelShort clients for Crawlora

Official Crawlora client packages for the hosted ReelShort API. Access 11 API endpoints covering title discovery, search, movie details, new releases, and public Fandom articles from JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust. These clients call Crawlora's hosted API; they do not scrape ReelShort locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by ReelShort or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/reelshort`](javascript/README.md)
- Python: [`crawlora-reelshort`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-reelshort`](go.mod)
- Ruby: [`crawlora-reelshort`](ruby/README.md)
- Java: [`net.crawlora:crawlora-reelshort:0.1.0`](java/README.md)
- PHP: [`crawlora/reelshort`](php/README.md)
- Rust: [`crawlora-reelshort`](rust/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=reelshort-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=reelshort-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=reelshort-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The seven language clients provide access to all 11 selected public ReelShort API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

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

## License

MIT. See [LICENSE](LICENSE).
