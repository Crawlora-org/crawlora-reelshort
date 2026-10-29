# Crawlora ReelShort Rust SDK Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `11`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| reelshort | `reelshort.fandom_categories` | `reelshort-fandom-categories` | `GET /reelshort/fandom-categories` | none | `ApiKeyAuth` | `ReelshortFandomCategoriesResponse` |  |
| reelshort | `reelshort.fandom_post` | `reelshort-fandom-post` | `GET /reelshort/fandom-post` | `id` (query String required) | `ApiKeyAuth` | `ReelshortFandomPostResponse` |  |
| reelshort | `reelshort.fandom_posts` | `reelshort-fandom-posts` | `GET /reelshort/fandom-posts` | `search` (query String)<br>`category` (query String enum{general-topic, movie-cast-list, top-movie-stories, where-to-watch, where-to-watch-2})<br>`page` (query i64)<br>`limit` (query i64) | `ApiKeyAuth` | `ReelshortFandomPostsResponse` |  |
| reelshort | `reelshort.home` | `reelshort-home` | `GET /reelshort/home` | `language` (query String enum{en, es, pt, fr, de, it, ja, ko, th, id, tr, ar, ru, pl, ro, cs, bg, vi, zh-TW}) | `ApiKeyAuth` | `ReelshortHomeResponse` |  |
| reelshort | `reelshort.movie` | `reelshort-movie` | `GET /reelshort/movie` | `id` (query String required) | `ApiKeyAuth` | `ReelshortMovieResponse` |  |
| reelshort | `reelshort.new_releases` | `reelshort-new-releases` | `GET /reelshort/new-releases` | `book_id` (query String required)<br>`language` (query String enum{en, es, pt, fr, de, it, ja, ko, th, id, tr, ar, ru, pl, ro, cs, bg, vi, zh-TW}) | `ApiKeyAuth` | `ReelshortNewReleasesResponse` |  |
| reelshort | `reelshort.search` | `reelshort-search` | `GET /reelshort/search` | `keywords` (query String required)<br>`page` (query i64)<br>`language` (query String enum{en, es, pt, fr, de, it, ja, ko, th, id, tr, ar, ru, pl, ro, cs, bg, vi, zh-TW}) | `ApiKeyAuth` | `ReelshortSearchResponse` |  |
| reelshort | `reelshort.shelf` | `reelshort-shelf` | `GET /reelshort/shelf` | `id` (query String required) | `ApiKeyAuth` | `ReelshortShelfResponse` |  |
| reelshort | `reelshort.tag_books` | `reelshort-tag-books` | `GET /reelshort/tag-books` | `tag_id` (query String required)<br>`page` (query i64)<br>`limit` (query i64)<br>`language` (query String enum{en, es, pt, fr, de, it, ja, ko, th, id, tr, ar, ru, pl, ro, cs, bg, vi, zh-TW}) | `ApiKeyAuth` | `ReelshortTagBooksResponse` |  |
| reelshort | `reelshort.tag_search` | `reelshort-tag-search` | `GET /reelshort/tag-search` | `word` (query String required)<br>`page` (query i64)<br>`language` (query String enum{en, es, pt, fr, de, it, ja, ko, th, id, tr, ar, ru, pl, ro, cs, bg, vi, zh-TW}) | `ApiKeyAuth` | `ReelshortTagSearchResponse` |  |
| reelshort | `reelshort.tags` | `reelshort-tags` | `GET /reelshort/tags` | `category` (query String enum{actor, actress, identity, trope} required)<br>`language` (query String enum{en, es, pt, fr, de, it, ja, ko, th, id, tr, ar, ru, pl, ro, cs, bg, vi, zh-TW}) | `ApiKeyAuth` | `ReelshortTagsResponse` |  |
