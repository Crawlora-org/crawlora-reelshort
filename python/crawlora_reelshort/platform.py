"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class ReelShortClient(CrawloraClient):
    """Synchronous ReelShort API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-reelshort-python/0.1.0')
        super().__init__(*args, **kwargs)

    def fandom_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reelshort-fandom-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    def fandom_post(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reelshort-fandom-post', params, response_type=response_type, timeout=timeout, headers=headers)

    def fandom_posts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reelshort-fandom-posts', params, response_type=response_type, timeout=timeout, headers=headers)

    def home(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reelshort-home', params, response_type=response_type, timeout=timeout, headers=headers)

    def movie(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reelshort-movie', params, response_type=response_type, timeout=timeout, headers=headers)

    def new_releases(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reelshort-new-releases', params, response_type=response_type, timeout=timeout, headers=headers)

    def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reelshort-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def shelf(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reelshort-shelf', params, response_type=response_type, timeout=timeout, headers=headers)

    def tag_books(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reelshort-tag-books', params, response_type=response_type, timeout=timeout, headers=headers)

    def tag_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reelshort-tag-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def tags(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reelshort-tags', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncReelShortClient(AsyncCrawloraClient):
    """Asynchronous ReelShort API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-reelshort-python/0.1.0')
        super().__init__(*args, **kwargs)

    async def fandom_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reelshort-fandom-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    async def fandom_post(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reelshort-fandom-post', params, response_type=response_type, timeout=timeout, headers=headers)

    async def fandom_posts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reelshort-fandom-posts', params, response_type=response_type, timeout=timeout, headers=headers)

    async def home(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reelshort-home', params, response_type=response_type, timeout=timeout, headers=headers)

    async def movie(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reelshort-movie', params, response_type=response_type, timeout=timeout, headers=headers)

    async def new_releases(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reelshort-new-releases', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reelshort-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def shelf(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reelshort-shelf', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tag_books(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reelshort-tag-books', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tag_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reelshort-tag-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tags(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reelshort-tags', params, response_type=response_type, timeout=timeout, headers=headers)
