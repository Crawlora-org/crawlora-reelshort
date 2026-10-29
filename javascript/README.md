# @crawlora-org/reelshort — ReelShort API client for JavaScript and TypeScript

JavaScript and TypeScript client for Crawlora's hosted ReelShort API.
It exposes 11 API endpoints for title discovery, search, movie details, new releases, and public Fandom articles through [Crawlora](https://crawlora.net/?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=reelshort-javascript-homepage). It does not run a browser or scrape ReelShort locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by ReelShort or its owners.

## Install

```sh
npm install @crawlora-org/reelshort
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=reelshort-javascript-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=reelshort-javascript-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.mjs`, then run `node example.mjs` after installing the package and setting your API key.

```js
import process from "node:process";
import { ReelShortClient } from "@crawlora-org/reelshort";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new ReelShortClient({ apiKey });
const result1 = await client.home({});
console.log(result1);
const result2 = await client.search({ keywords: "romance" });
console.log(result2);
```

The client also exports `Client` as an alias for `ReelShortClient`. Operation
methods are available directly in camelCase and through the `reelshort`
group. See the full method and parameter list in the [online reference](https://github.com/Crawlora-org/crawlora-reelshort/blob/main/docs/usage.md).

Methods return promises and can be awaited. See the [runnable example](https://github.com/Crawlora-org/crawlora-reelshort/blob/main/examples/javascript.mjs) for a complete usage example.

## Supported ReelShort API endpoints

This package exposes each route below as a direct method and through the `reelshort` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-reelshort/blob/main/docs/usage.md) for complete input details.

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

## Configuration

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API. Response data and availability depend on
Crawlora's current API behavior.
