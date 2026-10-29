from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelReelshortTagsResponseDoc = TypedDict('ModelReelshortTagsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelReelshortTagsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelReelshortTagsResponse = TypedDict('ModelReelshortTagsResponse', {
    'category': NotRequired[str],
    'category_id': NotRequired[int],
    'language': NotRequired[str],
    'tags': NotRequired[list[ModelReelshortTag]],
}, total=False)

ModelReelshortTag = TypedDict('ModelReelshortTag', {
    'category_id': NotRequired[str],
    'id': NotRequired[str],
    'kind': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelReelshortTagSearchResponseDoc = TypedDict('ModelReelshortTagSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelReelshortTagSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelReelshortTagSearchResponse = TypedDict('ModelReelshortTagSearchResponse', {
    'language': NotRequired[str],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
    'tags': NotRequired[list[ModelReelshortTagMatch]],
    'total': NotRequired[int],
    'word': NotRequired[str],
}, total=False)

ModelReelshortTagMatch = TypedDict('ModelReelshortTagMatch', {
    'category_id': NotRequired[int],
    'description': NotRequired[str],
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'kind': NotRequired[str],
    'name': NotRequired[str],
    'titles': NotRequired[int],
}, total=False)

ModelReelshortTagBooksResponseDoc = TypedDict('ModelReelshortTagBooksResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelReelshortTagBooksResponse],
    'msg': NotRequired[str],
}, total=False)

ModelReelshortTagBooksResponse = TypedDict('ModelReelshortTagBooksResponse', {
    'books': NotRequired[list[ModelReelshortBook]],
    'description': NotRequired[str],
    'limit': NotRequired[int],
    'page': NotRequired[int],
    'related_tags': NotRequired[list[ModelReelshortRelatedTag]],
    'tag': NotRequired[ModelReelshortTag],
    'top_titles': NotRequired[list[ModelReelshortTitleRef]],
    'total_items': NotRequired[int],
}, total=False)

ModelReelshortTitleRef = TypedDict('ModelReelshortTitleRef', {
    'id': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelReelshortRelatedTag = TypedDict('ModelReelshortRelatedTag', {
    'id': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelReelshortBook = TypedDict('ModelReelshortBook', {
    'cover_url': NotRequired[str],
    'description': NotRequired[str],
    'episodes': NotRequired[int],
    'favorites': NotRequired[int],
    'first_paid_episode': NotRequired[int],
    'has_trailer': NotRequired[bool],
    'id': NotRequired[str],
    'language': NotRequired[str],
    'plays': NotRequired[int],
    'tags': NotRequired[list[str]],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelReelshortShelfResponseDoc = TypedDict('ModelReelshortShelfResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelReelshortShelfResponse],
    'msg': NotRequired[str],
}, total=False)

ModelReelshortShelfResponse = TypedDict('ModelReelshortShelfResponse', {
    'books': NotRequired[list[ModelReelshortBook]],
    'id': NotRequired[int],
    'name': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelReelshortSearchResponseDoc = TypedDict('ModelReelshortSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelReelshortSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelReelshortSearchResponse = TypedDict('ModelReelshortSearchResponse', {
    'books': NotRequired[list[ModelReelshortBook]],
    'keywords': NotRequired[str],
    'language': NotRequired[str],
    'page': NotRequired[int],
    'total': NotRequired[int],
    'total_pages': NotRequired[int],
}, total=False)

ModelReelshortNewReleasesResponseDoc = TypedDict('ModelReelshortNewReleasesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelReelshortNewReleasesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelReelshortNewReleasesResponse = TypedDict('ModelReelshortNewReleasesResponse', {
    'books': NotRequired[list[ModelReelshortBook]],
    'language': NotRequired[str],
}, total=False)

ModelReelshortMovieResponseDoc = TypedDict('ModelReelshortMovieResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelReelshortMovieResponse],
    'msg': NotRequired[str],
}, total=False)

ModelReelshortMovieResponse = TypedDict('ModelReelshortMovieResponse', {
    'actors': NotRequired[list[ModelReelshortActor]],
    'ai_generated': NotRequired[bool],
    'badge': NotRequired[str],
    'cover_url': NotRequired[str],
    'description': NotRequired[str],
    'dubbed': NotRequired[bool],
    'episode_count': NotRequired[int],
    'episodes': NotRequired[list[ModelReelshortEpisode]],
    'favorites': NotRequired[int],
    'first_paid_episode': NotRequired[int],
    'id': NotRequired[str],
    'imdb_url': NotRequired[str],
    'language': NotRequired[str],
    'online_at': NotRequired[str],
    'original_language': NotRequired[str],
    'plays': NotRequired[int],
    'published_at': NotRequired[str],
    'tags': NotRequired[list[ModelReelshortTag]],
    'title': NotRequired[str],
    'update_status': NotRequired[int],
    'url': NotRequired[str],
}, total=False)

ModelReelshortEpisode = TypedDict('ModelReelshortEpisode', {
    'free': NotRequired[bool],
    'id': NotRequired[str],
    'kind': NotRequired[str],
    'likes': NotRequired[int],
    'number': NotRequired[int],
    'published_at': NotRequired[str],
    'thumbnail_url': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelReelshortActor = TypedDict('ModelReelshortActor', {
    'imdb_url': NotRequired[str],
    'name': NotRequired[str],
    'photo_url': NotRequired[str],
}, total=False)

ModelReelshortHomeResponseDoc = TypedDict('ModelReelshortHomeResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelReelshortHomeResponse],
    'msg': NotRequired[str],
}, total=False)

ModelReelshortHomeResponse = TypedDict('ModelReelshortHomeResponse', {
    'language': NotRequired[str],
    'shelves': NotRequired[list[ModelReelshortShelf]],
}, total=False)

ModelReelshortShelf = TypedDict('ModelReelshortShelf', {
    'books': NotRequired[list[ModelReelshortBook]],
    'id': NotRequired[int],
    'name': NotRequired[str],
}, total=False)

ModelReelshortFandomPostsResponseDoc = TypedDict('ModelReelshortFandomPostsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelReelshortFandomPostsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelReelshortFandomPostsResponse = TypedDict('ModelReelshortFandomPostsResponse', {
    'category': NotRequired[str],
    'limit': NotRequired[int],
    'page': NotRequired[int],
    'posts': NotRequired[list[ModelReelshortFandomPost]],
    'search': NotRequired[str],
    'total': NotRequired[int],
    'total_pages': NotRequired[int],
}, total=False)

ModelReelshortFandomPost = TypedDict('ModelReelshortFandomPost', {
    'categories': NotRequired[list[str]],
    'excerpt': NotRequired[str],
    'id': NotRequired[int],
    'image_url': NotRequired[str],
    'modified_at': NotRequired[str],
    'published_at': NotRequired[str],
    'slug': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelReelshortFandomPostResponseDoc = TypedDict('ModelReelshortFandomPostResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelReelshortFandomPostResponse],
    'msg': NotRequired[str],
}, total=False)

ModelReelshortFandomPostResponse = TypedDict('ModelReelshortFandomPostResponse', {
    'categories': NotRequired[list[str]],
    'content': NotRequired[str],
    'excerpt': NotRequired[str],
    'id': NotRequired[int],
    'image_url': NotRequired[str],
    'modified_at': NotRequired[str],
    'published_at': NotRequired[str],
    'slug': NotRequired[str],
    'title': NotRequired[str],
    'title_ids': NotRequired[list[str]],
    'url': NotRequired[str],
}, total=False)

ModelReelshortFandomCategoriesResponseDoc = TypedDict('ModelReelshortFandomCategoriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelReelshortFandomCategoriesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelReelshortFandomCategoriesResponse = TypedDict('ModelReelshortFandomCategoriesResponse', {
    'categories': NotRequired[list[ModelReelshortFandomCategory]],
}, total=False)

ModelReelshortFandomCategory = TypedDict('ModelReelshortFandomCategory', {
    'description': NotRequired[str],
    'id': NotRequired[int],
    'name': NotRequired[str],
    'posts': NotRequired[int],
    'slug': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ReelshortFandomCategoriesResponse = ModelReelshortFandomCategoriesResponseDoc
ReelshortFandomCategoriesParams = TypedDict('ReelshortFandomCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

ReelshortFandomPostResponse = ModelReelshortFandomPostResponseDoc
ReelshortFandomPostParams = TypedDict('ReelshortFandomPostParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

ReelshortFandomPostsResponse = ModelReelshortFandomPostsResponseDoc
ReelshortFandomPostsParams = TypedDict('ReelshortFandomPostsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'search': NotRequired[str],
    'category': NotRequired[Literal['general-topic', 'movie-cast-list', 'top-movie-stories', 'where-to-watch', 'where-to-watch-2']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

ReelshortHomeResponse = ModelReelshortHomeResponseDoc
ReelshortHomeParams = TypedDict('ReelshortHomeParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'language': NotRequired[Literal['en', 'es', 'pt', 'fr', 'de', 'it', 'ja', 'ko', 'th', 'id', 'tr', 'ar', 'ru', 'pl', 'ro', 'cs', 'bg', 'vi', 'zh-TW']],
}, total=False)

ReelshortMovieResponse = ModelReelshortMovieResponseDoc
ReelshortMovieParams = TypedDict('ReelshortMovieParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

ReelshortNewReleasesResponse = ModelReelshortNewReleasesResponseDoc
ReelshortNewReleasesParams = TypedDict('ReelshortNewReleasesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'book_id': Required[str],
    'language': NotRequired[Literal['en', 'es', 'pt', 'fr', 'de', 'it', 'ja', 'ko', 'th', 'id', 'tr', 'ar', 'ru', 'pl', 'ro', 'cs', 'bg', 'vi', 'zh-TW']],
}, total=False)

ReelshortSearchResponse = ModelReelshortSearchResponseDoc
ReelshortSearchParams = TypedDict('ReelshortSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keywords': Required[str],
    'page': NotRequired[int],
    'language': NotRequired[Literal['en', 'es', 'pt', 'fr', 'de', 'it', 'ja', 'ko', 'th', 'id', 'tr', 'ar', 'ru', 'pl', 'ro', 'cs', 'bg', 'vi', 'zh-TW']],
}, total=False)

ReelshortShelfResponse = ModelReelshortShelfResponseDoc
ReelshortShelfParams = TypedDict('ReelshortShelfParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

ReelshortTagBooksResponse = ModelReelshortTagBooksResponseDoc
ReelshortTagBooksParams = TypedDict('ReelshortTagBooksParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'tag_id': Required[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
    'language': NotRequired[Literal['en', 'es', 'pt', 'fr', 'de', 'it', 'ja', 'ko', 'th', 'id', 'tr', 'ar', 'ru', 'pl', 'ro', 'cs', 'bg', 'vi', 'zh-TW']],
}, total=False)

ReelshortTagSearchResponse = ModelReelshortTagSearchResponseDoc
ReelshortTagSearchParams = TypedDict('ReelshortTagSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'word': Required[str],
    'page': NotRequired[int],
    'language': NotRequired[Literal['en', 'es', 'pt', 'fr', 'de', 'it', 'ja', 'ko', 'th', 'id', 'tr', 'ar', 'ru', 'pl', 'ro', 'cs', 'bg', 'vi', 'zh-TW']],
}, total=False)

ReelshortTagsResponse = ModelReelshortTagsResponseDoc
ReelshortTagsParams = TypedDict('ReelshortTagsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'category': Required[Literal['actor', 'actress', 'identity', 'trope']],
    'language': NotRequired[Literal['en', 'es', 'pt', 'fr', 'de', 'it', 'ja', 'ko', 'th', 'id', 'tr', 'ar', 'ru', 'pl', 'ro', 'cs', 'bg', 'vi', 'zh-TW']],
}, total=False)

class ReelshortGroup:
    @overload
    def fandom_categories(self, **params: Unpack[ReelshortFandomCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def fandom_categories(self, **params: Unpack[ReelshortFandomCategoriesTextResponseParams]) -> str: ...
    @overload
    def fandom_categories(self, **params: Unpack[ReelshortFandomCategoriesDefaultParams]) -> ReelshortFandomCategoriesResponse: ...
    @overload
    def fandom_post(self, **params: Unpack[ReelshortFandomPostStreamParams]) -> BinaryIO: ...
    @overload
    def fandom_post(self, **params: Unpack[ReelshortFandomPostTextResponseParams]) -> str: ...
    @overload
    def fandom_post(self, **params: Unpack[ReelshortFandomPostDefaultParams]) -> ReelshortFandomPostResponse: ...
    @overload
    def fandom_posts(self, **params: Unpack[ReelshortFandomPostsStreamParams]) -> BinaryIO: ...
    @overload
    def fandom_posts(self, **params: Unpack[ReelshortFandomPostsTextResponseParams]) -> str: ...
    @overload
    def fandom_posts(self, **params: Unpack[ReelshortFandomPostsDefaultParams]) -> ReelshortFandomPostsResponse: ...
    @overload
    def home(self, **params: Unpack[ReelshortHomeStreamParams]) -> BinaryIO: ...
    @overload
    def home(self, **params: Unpack[ReelshortHomeTextResponseParams]) -> str: ...
    @overload
    def home(self, **params: Unpack[ReelshortHomeDefaultParams]) -> ReelshortHomeResponse: ...
    @overload
    def movie(self, **params: Unpack[ReelshortMovieStreamParams]) -> BinaryIO: ...
    @overload
    def movie(self, **params: Unpack[ReelshortMovieTextResponseParams]) -> str: ...
    @overload
    def movie(self, **params: Unpack[ReelshortMovieDefaultParams]) -> ReelshortMovieResponse: ...
    @overload
    def new_releases(self, **params: Unpack[ReelshortNewReleasesStreamParams]) -> BinaryIO: ...
    @overload
    def new_releases(self, **params: Unpack[ReelshortNewReleasesTextResponseParams]) -> str: ...
    @overload
    def new_releases(self, **params: Unpack[ReelshortNewReleasesDefaultParams]) -> ReelshortNewReleasesResponse: ...
    @overload
    def search(self, **params: Unpack[ReelshortSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[ReelshortSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[ReelshortSearchDefaultParams]) -> ReelshortSearchResponse: ...
    @overload
    def shelf(self, **params: Unpack[ReelshortShelfStreamParams]) -> BinaryIO: ...
    @overload
    def shelf(self, **params: Unpack[ReelshortShelfTextResponseParams]) -> str: ...
    @overload
    def shelf(self, **params: Unpack[ReelshortShelfDefaultParams]) -> ReelshortShelfResponse: ...
    @overload
    def tag_books(self, **params: Unpack[ReelshortTagBooksStreamParams]) -> BinaryIO: ...
    @overload
    def tag_books(self, **params: Unpack[ReelshortTagBooksTextResponseParams]) -> str: ...
    @overload
    def tag_books(self, **params: Unpack[ReelshortTagBooksDefaultParams]) -> ReelshortTagBooksResponse: ...
    @overload
    def tag_search(self, **params: Unpack[ReelshortTagSearchStreamParams]) -> BinaryIO: ...
    @overload
    def tag_search(self, **params: Unpack[ReelshortTagSearchTextResponseParams]) -> str: ...
    @overload
    def tag_search(self, **params: Unpack[ReelshortTagSearchDefaultParams]) -> ReelshortTagSearchResponse: ...
    @overload
    def tags(self, **params: Unpack[ReelshortTagsStreamParams]) -> BinaryIO: ...
    @overload
    def tags(self, **params: Unpack[ReelshortTagsTextResponseParams]) -> str: ...
    @overload
    def tags(self, **params: Unpack[ReelshortTagsDefaultParams]) -> ReelshortTagsResponse: ...

OperationId = Literal[
    'reelshort-fandom-categories',
    'reelshort-fandom-post',
    'reelshort-fandom-posts',
    'reelshort-home',
    'reelshort-movie',
    'reelshort-new-releases',
    'reelshort-search',
    'reelshort-shelf',
    'reelshort-tag-books',
    'reelshort-tag-search',
    'reelshort-tags',
]

class CrawloraClient:
    reelshort: ReelshortGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reelshort-fandom-categories'],
        params: ReelshortFandomCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ReelshortFandomCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reelshort-fandom-post'],
        params: ReelshortFandomPostParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ReelshortFandomPostResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reelshort-fandom-posts'],
        params: ReelshortFandomPostsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ReelshortFandomPostsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reelshort-home'],
        params: ReelshortHomeParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ReelshortHomeResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reelshort-movie'],
        params: ReelshortMovieParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ReelshortMovieResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reelshort-new-releases'],
        params: ReelshortNewReleasesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ReelshortNewReleasesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reelshort-search'],
        params: ReelshortSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ReelshortSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reelshort-shelf'],
        params: ReelshortShelfParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ReelshortShelfResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reelshort-tag-books'],
        params: ReelshortTagBooksParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ReelshortTagBooksResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reelshort-tag-search'],
        params: ReelshortTagSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ReelshortTagSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reelshort-tags'],
        params: ReelshortTagsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ReelshortTagsResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['reelshort-fandom-categories'],
        params: ReelshortFandomCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ReelshortFandomCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reelshort-fandom-post'],
        params: ReelshortFandomPostParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ReelshortFandomPostResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reelshort-fandom-posts'],
        params: ReelshortFandomPostsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ReelshortFandomPostsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reelshort-home'],
        params: ReelshortHomeParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ReelshortHomeResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reelshort-movie'],
        params: ReelshortMovieParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ReelshortMovieResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reelshort-new-releases'],
        params: ReelshortNewReleasesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ReelshortNewReleasesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reelshort-search'],
        params: ReelshortSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ReelshortSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reelshort-shelf'],
        params: ReelshortShelfParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ReelshortShelfResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reelshort-tag-books'],
        params: ReelshortTagBooksParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ReelshortTagBooksResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reelshort-tag-search'],
        params: ReelshortTagSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ReelshortTagSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reelshort-tags'],
        params: ReelshortTagsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ReelshortTagsResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class ReelShortClient(CrawloraClient):
    def __enter__(self) -> ReelShortClient: ...
    @overload
    def fandom_categories(self, **params: Unpack[ReelshortFandomCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def fandom_categories(self, **params: Unpack[ReelshortFandomCategoriesTextResponseParams]) -> str: ...
    @overload
    def fandom_categories(self, **params: Unpack[ReelshortFandomCategoriesDefaultParams]) -> ReelshortFandomCategoriesResponse: ...
    @overload
    def fandom_post(self, **params: Unpack[ReelshortFandomPostStreamParams]) -> BinaryIO: ...
    @overload
    def fandom_post(self, **params: Unpack[ReelshortFandomPostTextResponseParams]) -> str: ...
    @overload
    def fandom_post(self, **params: Unpack[ReelshortFandomPostDefaultParams]) -> ReelshortFandomPostResponse: ...
    @overload
    def fandom_posts(self, **params: Unpack[ReelshortFandomPostsStreamParams]) -> BinaryIO: ...
    @overload
    def fandom_posts(self, **params: Unpack[ReelshortFandomPostsTextResponseParams]) -> str: ...
    @overload
    def fandom_posts(self, **params: Unpack[ReelshortFandomPostsDefaultParams]) -> ReelshortFandomPostsResponse: ...
    @overload
    def home(self, **params: Unpack[ReelshortHomeStreamParams]) -> BinaryIO: ...
    @overload
    def home(self, **params: Unpack[ReelshortHomeTextResponseParams]) -> str: ...
    @overload
    def home(self, **params: Unpack[ReelshortHomeDefaultParams]) -> ReelshortHomeResponse: ...
    @overload
    def movie(self, **params: Unpack[ReelshortMovieStreamParams]) -> BinaryIO: ...
    @overload
    def movie(self, **params: Unpack[ReelshortMovieTextResponseParams]) -> str: ...
    @overload
    def movie(self, **params: Unpack[ReelshortMovieDefaultParams]) -> ReelshortMovieResponse: ...
    @overload
    def new_releases(self, **params: Unpack[ReelshortNewReleasesStreamParams]) -> BinaryIO: ...
    @overload
    def new_releases(self, **params: Unpack[ReelshortNewReleasesTextResponseParams]) -> str: ...
    @overload
    def new_releases(self, **params: Unpack[ReelshortNewReleasesDefaultParams]) -> ReelshortNewReleasesResponse: ...
    @overload
    def search(self, **params: Unpack[ReelshortSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[ReelshortSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[ReelshortSearchDefaultParams]) -> ReelshortSearchResponse: ...
    @overload
    def shelf(self, **params: Unpack[ReelshortShelfStreamParams]) -> BinaryIO: ...
    @overload
    def shelf(self, **params: Unpack[ReelshortShelfTextResponseParams]) -> str: ...
    @overload
    def shelf(self, **params: Unpack[ReelshortShelfDefaultParams]) -> ReelshortShelfResponse: ...
    @overload
    def tag_books(self, **params: Unpack[ReelshortTagBooksStreamParams]) -> BinaryIO: ...
    @overload
    def tag_books(self, **params: Unpack[ReelshortTagBooksTextResponseParams]) -> str: ...
    @overload
    def tag_books(self, **params: Unpack[ReelshortTagBooksDefaultParams]) -> ReelshortTagBooksResponse: ...
    @overload
    def tag_search(self, **params: Unpack[ReelshortTagSearchStreamParams]) -> BinaryIO: ...
    @overload
    def tag_search(self, **params: Unpack[ReelshortTagSearchTextResponseParams]) -> str: ...
    @overload
    def tag_search(self, **params: Unpack[ReelshortTagSearchDefaultParams]) -> ReelshortTagSearchResponse: ...
    @overload
    def tags(self, **params: Unpack[ReelshortTagsStreamParams]) -> BinaryIO: ...
    @overload
    def tags(self, **params: Unpack[ReelshortTagsTextResponseParams]) -> str: ...
    @overload
    def tags(self, **params: Unpack[ReelshortTagsDefaultParams]) -> ReelshortTagsResponse: ...

class AsyncReelShortClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncReelShortClient: ...
    reelshort: _AsyncReelshortGroup
    @overload
    async def fandom_categories(self, **params: Unpack[ReelshortFandomCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def fandom_categories(self, **params: Unpack[ReelshortFandomCategoriesTextResponseParams]) -> str: ...
    @overload
    async def fandom_categories(self, **params: Unpack[ReelshortFandomCategoriesDefaultParams]) -> ReelshortFandomCategoriesResponse: ...
    @overload
    async def fandom_post(self, **params: Unpack[ReelshortFandomPostStreamParams]) -> BinaryIO: ...
    @overload
    async def fandom_post(self, **params: Unpack[ReelshortFandomPostTextResponseParams]) -> str: ...
    @overload
    async def fandom_post(self, **params: Unpack[ReelshortFandomPostDefaultParams]) -> ReelshortFandomPostResponse: ...
    @overload
    async def fandom_posts(self, **params: Unpack[ReelshortFandomPostsStreamParams]) -> BinaryIO: ...
    @overload
    async def fandom_posts(self, **params: Unpack[ReelshortFandomPostsTextResponseParams]) -> str: ...
    @overload
    async def fandom_posts(self, **params: Unpack[ReelshortFandomPostsDefaultParams]) -> ReelshortFandomPostsResponse: ...
    @overload
    async def home(self, **params: Unpack[ReelshortHomeStreamParams]) -> BinaryIO: ...
    @overload
    async def home(self, **params: Unpack[ReelshortHomeTextResponseParams]) -> str: ...
    @overload
    async def home(self, **params: Unpack[ReelshortHomeDefaultParams]) -> ReelshortHomeResponse: ...
    @overload
    async def movie(self, **params: Unpack[ReelshortMovieStreamParams]) -> BinaryIO: ...
    @overload
    async def movie(self, **params: Unpack[ReelshortMovieTextResponseParams]) -> str: ...
    @overload
    async def movie(self, **params: Unpack[ReelshortMovieDefaultParams]) -> ReelshortMovieResponse: ...
    @overload
    async def new_releases(self, **params: Unpack[ReelshortNewReleasesStreamParams]) -> BinaryIO: ...
    @overload
    async def new_releases(self, **params: Unpack[ReelshortNewReleasesTextResponseParams]) -> str: ...
    @overload
    async def new_releases(self, **params: Unpack[ReelshortNewReleasesDefaultParams]) -> ReelshortNewReleasesResponse: ...
    @overload
    async def search(self, **params: Unpack[ReelshortSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[ReelshortSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[ReelshortSearchDefaultParams]) -> ReelshortSearchResponse: ...
    @overload
    async def shelf(self, **params: Unpack[ReelshortShelfStreamParams]) -> BinaryIO: ...
    @overload
    async def shelf(self, **params: Unpack[ReelshortShelfTextResponseParams]) -> str: ...
    @overload
    async def shelf(self, **params: Unpack[ReelshortShelfDefaultParams]) -> ReelshortShelfResponse: ...
    @overload
    async def tag_books(self, **params: Unpack[ReelshortTagBooksStreamParams]) -> BinaryIO: ...
    @overload
    async def tag_books(self, **params: Unpack[ReelshortTagBooksTextResponseParams]) -> str: ...
    @overload
    async def tag_books(self, **params: Unpack[ReelshortTagBooksDefaultParams]) -> ReelshortTagBooksResponse: ...
    @overload
    async def tag_search(self, **params: Unpack[ReelshortTagSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def tag_search(self, **params: Unpack[ReelshortTagSearchTextResponseParams]) -> str: ...
    @overload
    async def tag_search(self, **params: Unpack[ReelshortTagSearchDefaultParams]) -> ReelshortTagSearchResponse: ...
    @overload
    async def tags(self, **params: Unpack[ReelshortTagsStreamParams]) -> BinaryIO: ...
    @overload
    async def tags(self, **params: Unpack[ReelshortTagsTextResponseParams]) -> str: ...
    @overload
    async def tags(self, **params: Unpack[ReelshortTagsDefaultParams]) -> ReelshortTagsResponse: ...

class _AsyncReelshortGroup:
    @overload
    async def fandom_categories(self, **params: Unpack[ReelshortFandomCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def fandom_categories(self, **params: Unpack[ReelshortFandomCategoriesTextResponseParams]) -> str: ...
    @overload
    async def fandom_categories(self, **params: Unpack[ReelshortFandomCategoriesDefaultParams]) -> ReelshortFandomCategoriesResponse: ...
    @overload
    async def fandom_post(self, **params: Unpack[ReelshortFandomPostStreamParams]) -> BinaryIO: ...
    @overload
    async def fandom_post(self, **params: Unpack[ReelshortFandomPostTextResponseParams]) -> str: ...
    @overload
    async def fandom_post(self, **params: Unpack[ReelshortFandomPostDefaultParams]) -> ReelshortFandomPostResponse: ...
    @overload
    async def fandom_posts(self, **params: Unpack[ReelshortFandomPostsStreamParams]) -> BinaryIO: ...
    @overload
    async def fandom_posts(self, **params: Unpack[ReelshortFandomPostsTextResponseParams]) -> str: ...
    @overload
    async def fandom_posts(self, **params: Unpack[ReelshortFandomPostsDefaultParams]) -> ReelshortFandomPostsResponse: ...
    @overload
    async def home(self, **params: Unpack[ReelshortHomeStreamParams]) -> BinaryIO: ...
    @overload
    async def home(self, **params: Unpack[ReelshortHomeTextResponseParams]) -> str: ...
    @overload
    async def home(self, **params: Unpack[ReelshortHomeDefaultParams]) -> ReelshortHomeResponse: ...
    @overload
    async def movie(self, **params: Unpack[ReelshortMovieStreamParams]) -> BinaryIO: ...
    @overload
    async def movie(self, **params: Unpack[ReelshortMovieTextResponseParams]) -> str: ...
    @overload
    async def movie(self, **params: Unpack[ReelshortMovieDefaultParams]) -> ReelshortMovieResponse: ...
    @overload
    async def new_releases(self, **params: Unpack[ReelshortNewReleasesStreamParams]) -> BinaryIO: ...
    @overload
    async def new_releases(self, **params: Unpack[ReelshortNewReleasesTextResponseParams]) -> str: ...
    @overload
    async def new_releases(self, **params: Unpack[ReelshortNewReleasesDefaultParams]) -> ReelshortNewReleasesResponse: ...
    @overload
    async def search(self, **params: Unpack[ReelshortSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[ReelshortSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[ReelshortSearchDefaultParams]) -> ReelshortSearchResponse: ...
    @overload
    async def shelf(self, **params: Unpack[ReelshortShelfStreamParams]) -> BinaryIO: ...
    @overload
    async def shelf(self, **params: Unpack[ReelshortShelfTextResponseParams]) -> str: ...
    @overload
    async def shelf(self, **params: Unpack[ReelshortShelfDefaultParams]) -> ReelshortShelfResponse: ...
    @overload
    async def tag_books(self, **params: Unpack[ReelshortTagBooksStreamParams]) -> BinaryIO: ...
    @overload
    async def tag_books(self, **params: Unpack[ReelshortTagBooksTextResponseParams]) -> str: ...
    @overload
    async def tag_books(self, **params: Unpack[ReelshortTagBooksDefaultParams]) -> ReelshortTagBooksResponse: ...
    @overload
    async def tag_search(self, **params: Unpack[ReelshortTagSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def tag_search(self, **params: Unpack[ReelshortTagSearchTextResponseParams]) -> str: ...
    @overload
    async def tag_search(self, **params: Unpack[ReelshortTagSearchDefaultParams]) -> ReelshortTagSearchResponse: ...
    @overload
    async def tags(self, **params: Unpack[ReelshortTagsStreamParams]) -> BinaryIO: ...
    @overload
    async def tags(self, **params: Unpack[ReelshortTagsTextResponseParams]) -> str: ...
    @overload
    async def tags(self, **params: Unpack[ReelshortTagsDefaultParams]) -> ReelshortTagsResponse: ...

ReelshortFandomCategoriesDefaultParams = TypedDict('ReelshortFandomCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

ReelshortFandomCategoriesTextResponseParams = TypedDict('ReelshortFandomCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

ReelshortFandomCategoriesStreamParams = TypedDict('ReelshortFandomCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

ReelshortFandomPostDefaultParams = TypedDict('ReelshortFandomPostDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

ReelshortFandomPostTextResponseParams = TypedDict('ReelshortFandomPostTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

ReelshortFandomPostStreamParams = TypedDict('ReelshortFandomPostStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

ReelshortFandomPostsDefaultParams = TypedDict('ReelshortFandomPostsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'search': NotRequired[str],
    'category': NotRequired[Literal['general-topic', 'movie-cast-list', 'top-movie-stories', 'where-to-watch', 'where-to-watch-2']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

ReelshortFandomPostsTextResponseParams = TypedDict('ReelshortFandomPostsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'search': NotRequired[str],
    'category': NotRequired[Literal['general-topic', 'movie-cast-list', 'top-movie-stories', 'where-to-watch', 'where-to-watch-2']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

ReelshortFandomPostsStreamParams = TypedDict('ReelshortFandomPostsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'search': NotRequired[str],
    'category': NotRequired[Literal['general-topic', 'movie-cast-list', 'top-movie-stories', 'where-to-watch', 'where-to-watch-2']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

ReelshortHomeDefaultParams = TypedDict('ReelshortHomeDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'language': NotRequired[Literal['en', 'es', 'pt', 'fr', 'de', 'it', 'ja', 'ko', 'th', 'id', 'tr', 'ar', 'ru', 'pl', 'ro', 'cs', 'bg', 'vi', 'zh-TW']],
}, total=False)

ReelshortHomeTextResponseParams = TypedDict('ReelshortHomeTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'language': NotRequired[Literal['en', 'es', 'pt', 'fr', 'de', 'it', 'ja', 'ko', 'th', 'id', 'tr', 'ar', 'ru', 'pl', 'ro', 'cs', 'bg', 'vi', 'zh-TW']],
}, total=False)

ReelshortHomeStreamParams = TypedDict('ReelshortHomeStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'language': NotRequired[Literal['en', 'es', 'pt', 'fr', 'de', 'it', 'ja', 'ko', 'th', 'id', 'tr', 'ar', 'ru', 'pl', 'ro', 'cs', 'bg', 'vi', 'zh-TW']],
}, total=False)

ReelshortMovieDefaultParams = TypedDict('ReelshortMovieDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

ReelshortMovieTextResponseParams = TypedDict('ReelshortMovieTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

ReelshortMovieStreamParams = TypedDict('ReelshortMovieStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

ReelshortNewReleasesDefaultParams = TypedDict('ReelshortNewReleasesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'book_id': Required[str],
    'language': NotRequired[Literal['en', 'es', 'pt', 'fr', 'de', 'it', 'ja', 'ko', 'th', 'id', 'tr', 'ar', 'ru', 'pl', 'ro', 'cs', 'bg', 'vi', 'zh-TW']],
}, total=False)

ReelshortNewReleasesTextResponseParams = TypedDict('ReelshortNewReleasesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'book_id': Required[str],
    'language': NotRequired[Literal['en', 'es', 'pt', 'fr', 'de', 'it', 'ja', 'ko', 'th', 'id', 'tr', 'ar', 'ru', 'pl', 'ro', 'cs', 'bg', 'vi', 'zh-TW']],
}, total=False)

ReelshortNewReleasesStreamParams = TypedDict('ReelshortNewReleasesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'book_id': Required[str],
    'language': NotRequired[Literal['en', 'es', 'pt', 'fr', 'de', 'it', 'ja', 'ko', 'th', 'id', 'tr', 'ar', 'ru', 'pl', 'ro', 'cs', 'bg', 'vi', 'zh-TW']],
}, total=False)

ReelshortSearchDefaultParams = TypedDict('ReelshortSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keywords': Required[str],
    'page': NotRequired[int],
    'language': NotRequired[Literal['en', 'es', 'pt', 'fr', 'de', 'it', 'ja', 'ko', 'th', 'id', 'tr', 'ar', 'ru', 'pl', 'ro', 'cs', 'bg', 'vi', 'zh-TW']],
}, total=False)

ReelshortSearchTextResponseParams = TypedDict('ReelshortSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keywords': Required[str],
    'page': NotRequired[int],
    'language': NotRequired[Literal['en', 'es', 'pt', 'fr', 'de', 'it', 'ja', 'ko', 'th', 'id', 'tr', 'ar', 'ru', 'pl', 'ro', 'cs', 'bg', 'vi', 'zh-TW']],
}, total=False)

ReelshortSearchStreamParams = TypedDict('ReelshortSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keywords': Required[str],
    'page': NotRequired[int],
    'language': NotRequired[Literal['en', 'es', 'pt', 'fr', 'de', 'it', 'ja', 'ko', 'th', 'id', 'tr', 'ar', 'ru', 'pl', 'ro', 'cs', 'bg', 'vi', 'zh-TW']],
}, total=False)

ReelshortShelfDefaultParams = TypedDict('ReelshortShelfDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

ReelshortShelfTextResponseParams = TypedDict('ReelshortShelfTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

ReelshortShelfStreamParams = TypedDict('ReelshortShelfStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

ReelshortTagBooksDefaultParams = TypedDict('ReelshortTagBooksDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'tag_id': Required[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
    'language': NotRequired[Literal['en', 'es', 'pt', 'fr', 'de', 'it', 'ja', 'ko', 'th', 'id', 'tr', 'ar', 'ru', 'pl', 'ro', 'cs', 'bg', 'vi', 'zh-TW']],
}, total=False)

ReelshortTagBooksTextResponseParams = TypedDict('ReelshortTagBooksTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'tag_id': Required[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
    'language': NotRequired[Literal['en', 'es', 'pt', 'fr', 'de', 'it', 'ja', 'ko', 'th', 'id', 'tr', 'ar', 'ru', 'pl', 'ro', 'cs', 'bg', 'vi', 'zh-TW']],
}, total=False)

ReelshortTagBooksStreamParams = TypedDict('ReelshortTagBooksStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'tag_id': Required[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
    'language': NotRequired[Literal['en', 'es', 'pt', 'fr', 'de', 'it', 'ja', 'ko', 'th', 'id', 'tr', 'ar', 'ru', 'pl', 'ro', 'cs', 'bg', 'vi', 'zh-TW']],
}, total=False)

ReelshortTagSearchDefaultParams = TypedDict('ReelshortTagSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'word': Required[str],
    'page': NotRequired[int],
    'language': NotRequired[Literal['en', 'es', 'pt', 'fr', 'de', 'it', 'ja', 'ko', 'th', 'id', 'tr', 'ar', 'ru', 'pl', 'ro', 'cs', 'bg', 'vi', 'zh-TW']],
}, total=False)

ReelshortTagSearchTextResponseParams = TypedDict('ReelshortTagSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'word': Required[str],
    'page': NotRequired[int],
    'language': NotRequired[Literal['en', 'es', 'pt', 'fr', 'de', 'it', 'ja', 'ko', 'th', 'id', 'tr', 'ar', 'ru', 'pl', 'ro', 'cs', 'bg', 'vi', 'zh-TW']],
}, total=False)

ReelshortTagSearchStreamParams = TypedDict('ReelshortTagSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'word': Required[str],
    'page': NotRequired[int],
    'language': NotRequired[Literal['en', 'es', 'pt', 'fr', 'de', 'it', 'ja', 'ko', 'th', 'id', 'tr', 'ar', 'ru', 'pl', 'ro', 'cs', 'bg', 'vi', 'zh-TW']],
}, total=False)

ReelshortTagsDefaultParams = TypedDict('ReelshortTagsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'category': Required[Literal['actor', 'actress', 'identity', 'trope']],
    'language': NotRequired[Literal['en', 'es', 'pt', 'fr', 'de', 'it', 'ja', 'ko', 'th', 'id', 'tr', 'ar', 'ru', 'pl', 'ro', 'cs', 'bg', 'vi', 'zh-TW']],
}, total=False)

ReelshortTagsTextResponseParams = TypedDict('ReelshortTagsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'category': Required[Literal['actor', 'actress', 'identity', 'trope']],
    'language': NotRequired[Literal['en', 'es', 'pt', 'fr', 'de', 'it', 'ja', 'ko', 'th', 'id', 'tr', 'ar', 'ru', 'pl', 'ro', 'cs', 'bg', 'vi', 'zh-TW']],
}, total=False)

ReelshortTagsStreamParams = TypedDict('ReelshortTagsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'category': Required[Literal['actor', 'actress', 'identity', 'trope']],
    'language': NotRequired[Literal['en', 'es', 'pt', 'fr', 'de', 'it', 'ja', 'ko', 'th', 'id', 'tr', 'ar', 'ru', 'pl', 'ro', 'cs', 'bg', 'vi', 'zh-TW']],
}, total=False)
