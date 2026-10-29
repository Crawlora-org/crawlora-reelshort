# crawlora-reelshort — ReelShort API client for Python

Python client for Crawlora's hosted ReelShort API. It exposes 11 API endpoints covering title discovery, search, movie details, new releases, and public Fandom articles. Requests go to [Crawlora](https://crawlora.net/?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=reelshort-python-homepage); the package does not run a browser or scrape
ReelShort locally. A Crawlora account and `CRAWLORA_API_KEY` are required,
and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by
ReelShort or its owners.

## Install

```sh
python -m pip install crawlora-reelshort
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=reelshort-python-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=reelshort-python-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.py`, then run `python example.py` after installing the package and setting your API key.

```python
import os

from crawlora_reelshort import ReelShortClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with ReelShortClient(api_key=api_key) as client:
    result_1 = client.home()
    print(result_1)
    result_2 = client.search(keywords='romance')
    print(result_2)
```

The package also exports `Client` as an alias for `ReelShortClient`. Operation
methods are available directly in snake_case and through the `reelshort`
group. The async package client is `AsyncReelShortClient`; see the [online
endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-reelshort/blob/main/docs/usage.md) and [runnable example](https://github.com/Crawlora-org/crawlora-reelshort/blob/main/examples/python.py).

### Async usage

The package also exports `AsyncClient` for asynchronous requests:

```python
import asyncio
import os

from crawlora_reelshort import AsyncClient

async def main():
    api_key = os.environ.get("CRAWLORA_API_KEY")
    if not api_key:
        raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")
    async with AsyncClient(api_key=api_key) as client:
        result_1 = await client.home()
        print(result_1)

asyncio.run(main())
```

See the [runnable example](https://github.com/Crawlora-org/crawlora-reelshort/blob/main/examples/python.py) for a complete usage example.

## Supported ReelShort API endpoints

This package exposes every route below through direct snake_case methods and the `reelshort` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-reelshort/blob/main/docs/usage.md) for complete input details.

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

Pass your key through `api_key` or read `CRAWLORA_API_KEY` from the environment.
Keep credentials out of source control and logs. Requests go to Crawlora's
hosted API.
