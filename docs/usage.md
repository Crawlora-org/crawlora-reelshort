# ReelShort API endpoint reference and client usage

This reference lists all 11 public ReelShort API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/reelshort`, `crawlora-reelshort`, and `crawlora-reelshort` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape ReelShort locally; Crawlora is independent from and not endorsed by ReelShort or its owners.

The package tracks the public API contract revision `sha256:d05c7c916e44f76874f1d3a98ebf61fce4706f0a7c795a3bc5a64259a6894f4c` bundled with release `0.1.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `reelshort`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `fandomCategories` | `fandom_categories` | `reelshort.fandom_categories` | `GET /reelshort/fandom-categories` | — | List ReelShort Fandom's article categories |
| `fandomPost` | `fandom_post` | `reelshort.fandom_post` | `GET /reelshort/fandom-post` | `id` (query, required) | Get a ReelShort Fandom article |
| `fandomPosts` | `fandom_posts` | `reelshort.fandom_posts` | `GET /reelshort/fandom-posts` | `search` (query, optional), `category` (query, optional; values: `general-topic`, `movie-cast-list`, `top-movie-stories`, `where-to-watch`, `where-to-watch-2`), `page` (query, optional), `limit` (query, optional) | List ReelShort Fandom articles |
| `home` | `home` | `reelshort.home` | `GET /reelshort/home` | `language` (query, optional; values: `en`, `es`, `pt`, `fr`, `de`, `it`, `ja`, `ko`, `th`, `id`, `tr`, `ar`, `ru`, `pl`, `ro`, `cs`, `bg`, `vi`, `zh-TW`) | List ReelShort's home page shelves |
| `movie` | `movie` | `reelshort.movie` | `GET /reelshort/movie` | `id` (query, required) | Get a ReelShort short drama and its episodes |
| `newReleases` | `new_releases` | `reelshort.new_releases` | `GET /reelshort/new-releases` | `book_id` (query, required), `language` (query, optional; values: `en`, `es`, `pt`, `fr`, `de`, `it`, `ja`, `ko`, `th`, `id`, `tr`, `ar`, `ru`, `pl`, `ro`, `cs`, `bg`, `vi`, `zh-TW`) | List ReelShort's curated New Release titles |
| `search` | `search` | `reelshort.search` | `GET /reelshort/search` | `keywords` (query, required), `page` (query, optional), `language` (query, optional; values: `en`, `es`, `pt`, `fr`, `de`, `it`, `ja`, `ko`, `th`, `id`, `tr`, `ar`, `ru`, `pl`, `ro`, `cs`, `bg`, `vi`, `zh-TW`) | Search ReelShort short dramas by title |
| `shelf` | `shelf` | `reelshort.shelf` | `GET /reelshort/shelf` | `id` (query, required) | Get a whole ReelShort shelf |
| `tagBooks` | `tag_books` | `reelshort.tag_books` | `GET /reelshort/tag-books` | `tag_id` (query, required), `page` (query, optional), `limit` (query, optional), `language` (query, optional; values: `en`, `es`, `pt`, `fr`, `de`, `it`, `ja`, `ko`, `th`, `id`, `tr`, `ar`, `ru`, `pl`, `ro`, `cs`, `bg`, `vi`, `zh-TW`) | List the ReelShort titles carrying a tag |
| `tags` | `tags` | `reelshort.tags` | `GET /reelshort/tags` | `category` (query, required; values: `actor`, `actress`, `identity`, `trope`), `language` (query, optional; values: `en`, `es`, `pt`, `fr`, `de`, `it`, `ja`, `ko`, `th`, `id`, `tr`, `ar`, `ru`, `pl`, `ro`, `cs`, `bg`, `vi`, `zh-TW`) | List ReelShort's featured tags in one category |
| `tagSearch` | `tag_search` | `reelshort.tag_search` | `GET /reelshort/tag-search` | `word` (query, required), `page` (query, optional), `language` (query, optional; values: `en`, `es`, `pt`, `fr`, `de`, `it`, `ja`, `ko`, `th`, `id`, `tr`, `ar`, `ru`, `pl`, `ro`, `cs`, `bg`, `vi`, `zh-TW`) | Search ReelShort tags by text |

## Client forms

- JavaScript: import `ReelShortClient` (also exported as `Client`) from `@crawlora-org/reelshort`; use `new ReelShortClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `ReelShortClient` (also exported as `Client`) from `crawlora_reelshort`; use `with ReelShortClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncReelShortClient`, used with `async with` and `await`.
- Rust: add `crawlora-reelshort` with Cargo; import `Client` and the generated operation parameter struct, then call `client.reelshort.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-reelshort/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
