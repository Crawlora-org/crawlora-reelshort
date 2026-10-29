# Crawlora ReelShort JavaScript Client Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `11`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| reelshort | `reelshort.fandomCategories` | `reelshort-fandom-categories` | `GET /reelshort/fandom-categories` | none | `ApiKeyAuth` | `ReelshortFandomCategoriesResponse` |  |
| reelshort | `reelshort.fandomPost` | `reelshort-fandom-post` | `GET /reelshort/fandom-post` | `id` (query string required) | `ApiKeyAuth` | `ReelshortFandomPostResponse` |  |
| reelshort | `reelshort.fandomPosts` | `reelshort-fandom-posts` | `GET /reelshort/fandom-posts` | `search` (query string)<br>`category` (query "general-topic" \| "movie-cast-list" \| "top-movie-stories" \| "where-to-watch" \| "where-to-watch-2")<br>`page` (query number)<br>`limit` (query number) | `ApiKeyAuth` | `ReelshortFandomPostsResponse` |  |
| reelshort | `reelshort.home` | `reelshort-home` | `GET /reelshort/home` | `language` (query "en" \| "es" \| "pt" \| "fr" \| "de" \| "it" \| "ja" \| "ko" \| "th" \| "id" \| "tr" \| "ar" \| "ru" \| "pl" \| "ro" \| "cs" \| "bg" \| "vi" \| "zh-TW") | `ApiKeyAuth` | `ReelshortHomeResponse` |  |
| reelshort | `reelshort.movie` | `reelshort-movie` | `GET /reelshort/movie` | `id` (query string required) | `ApiKeyAuth` | `ReelshortMovieResponse` |  |
| reelshort | `reelshort.newReleases` | `reelshort-new-releases` | `GET /reelshort/new-releases` | `book_id` (query string required)<br>`language` (query "en" \| "es" \| "pt" \| "fr" \| "de" \| "it" \| "ja" \| "ko" \| "th" \| "id" \| "tr" \| "ar" \| "ru" \| "pl" \| "ro" \| "cs" \| "bg" \| "vi" \| "zh-TW") | `ApiKeyAuth` | `ReelshortNewReleasesResponse` |  |
| reelshort | `reelshort.search` | `reelshort-search` | `GET /reelshort/search` | `keywords` (query string required)<br>`page` (query number)<br>`language` (query "en" \| "es" \| "pt" \| "fr" \| "de" \| "it" \| "ja" \| "ko" \| "th" \| "id" \| "tr" \| "ar" \| "ru" \| "pl" \| "ro" \| "cs" \| "bg" \| "vi" \| "zh-TW") | `ApiKeyAuth` | `ReelshortSearchResponse` |  |
| reelshort | `reelshort.shelf` | `reelshort-shelf` | `GET /reelshort/shelf` | `id` (query string required) | `ApiKeyAuth` | `ReelshortShelfResponse` |  |
| reelshort | `reelshort.tagBooks` | `reelshort-tag-books` | `GET /reelshort/tag-books` | `tag_id` (query string required)<br>`page` (query number)<br>`limit` (query number)<br>`language` (query "en" \| "es" \| "pt" \| "fr" \| "de" \| "it" \| "ja" \| "ko" \| "th" \| "id" \| "tr" \| "ar" \| "ru" \| "pl" \| "ro" \| "cs" \| "bg" \| "vi" \| "zh-TW") | `ApiKeyAuth` | `ReelshortTagBooksResponse` |  |
| reelshort | `reelshort.tagSearch` | `reelshort-tag-search` | `GET /reelshort/tag-search` | `word` (query string required)<br>`page` (query number)<br>`language` (query "en" \| "es" \| "pt" \| "fr" \| "de" \| "it" \| "ja" \| "ko" \| "th" \| "id" \| "tr" \| "ar" \| "ru" \| "pl" \| "ro" \| "cs" \| "bg" \| "vi" \| "zh-TW") | `ApiKeyAuth` | `ReelshortTagSearchResponse` |  |
| reelshort | `reelshort.tags` | `reelshort-tags` | `GET /reelshort/tags` | `category` (query "actor" \| "actress" \| "identity" \| "trope" required)<br>`language` (query "en" \| "es" \| "pt" \| "fr" \| "de" \| "it" \| "ja" \| "ko" \| "th" \| "id" \| "tr" \| "ar" \| "ru" \| "pl" \| "ro" \| "cs" \| "bg" \| "vi" \| "zh-TW") | `ApiKeyAuth` | `ReelshortTagsResponse` |  |
