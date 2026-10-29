import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class ReelShortClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  fandomCategories(params?: OperationParamsMap["reelshort-fandom-categories"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  fandomPost(params: OperationParamsMap["reelshort-fandom-post"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  fandomPosts(params?: OperationParamsMap["reelshort-fandom-posts"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  home(params?: OperationParamsMap["reelshort-home"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  movie(params: OperationParamsMap["reelshort-movie"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  newReleases(params: OperationParamsMap["reelshort-new-releases"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  search(params: OperationParamsMap["reelshort-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  shelf(params: OperationParamsMap["reelshort-shelf"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tagBooks(params: OperationParamsMap["reelshort-tag-books"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tagSearch(params: OperationParamsMap["reelshort-tag-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tags(params: OperationParamsMap["reelshort-tags"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  fandomCategories(params?: OperationParamsMap["reelshort-fandom-categories"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  fandomPost(params: OperationParamsMap["reelshort-fandom-post"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  fandomPosts(params?: OperationParamsMap["reelshort-fandom-posts"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  home(params?: OperationParamsMap["reelshort-home"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  movie(params: OperationParamsMap["reelshort-movie"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  newReleases(params: OperationParamsMap["reelshort-new-releases"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  search(params: OperationParamsMap["reelshort-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  shelf(params: OperationParamsMap["reelshort-shelf"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tagBooks(params: OperationParamsMap["reelshort-tag-books"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tagSearch(params: OperationParamsMap["reelshort-tag-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tags(params: OperationParamsMap["reelshort-tags"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  fandomCategories(...args: OperationRequestArgs<"reelshort-fandom-categories">): Promise<OperationResponseMap["reelshort-fandom-categories"]>;
  fandomPost(...args: OperationRequestArgs<"reelshort-fandom-post">): Promise<OperationResponseMap["reelshort-fandom-post"]>;
  fandomPosts(...args: OperationRequestArgs<"reelshort-fandom-posts">): Promise<OperationResponseMap["reelshort-fandom-posts"]>;
  home(...args: OperationRequestArgs<"reelshort-home">): Promise<OperationResponseMap["reelshort-home"]>;
  movie(...args: OperationRequestArgs<"reelshort-movie">): Promise<OperationResponseMap["reelshort-movie"]>;
  newReleases(...args: OperationRequestArgs<"reelshort-new-releases">): Promise<OperationResponseMap["reelshort-new-releases"]>;
  search(...args: OperationRequestArgs<"reelshort-search">): Promise<OperationResponseMap["reelshort-search"]>;
  shelf(...args: OperationRequestArgs<"reelshort-shelf">): Promise<OperationResponseMap["reelshort-shelf"]>;
  tagBooks(...args: OperationRequestArgs<"reelshort-tag-books">): Promise<OperationResponseMap["reelshort-tag-books"]>;
  tagSearch(...args: OperationRequestArgs<"reelshort-tag-search">): Promise<OperationResponseMap["reelshort-tag-search"]>;
  tags(...args: OperationRequestArgs<"reelshort-tags">): Promise<OperationResponseMap["reelshort-tags"]>;
}
export { ReelShortClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default ReelShortClient;
