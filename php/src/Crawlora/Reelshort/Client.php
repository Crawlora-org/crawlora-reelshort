<?php

declare(strict_types=1);

namespace Crawlora\Reelshort;

class CrawloraException extends \RuntimeException
{
    public function __construct(string $message, public readonly ?int $status = null, public readonly ?string $operationId = null, public readonly ?string $responseBody = null, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, $previous);
    }
}

class ClientException extends CrawloraException {}
class ServerException extends CrawloraException {}
class NetworkException extends CrawloraException {}

final class Client
{
    private static array $operations;
    private bool $closed = false;
    private string $apiKey;
    private string $baseUrl;
    private float $timeout;
    private ?\Closure $transport;

    public const PLATFORM = 'reelshort';
    public const VERSION = '0.1.0';
    public const OPERATION_COUNT = 11;
    public const OPERATION_IDS = ["reelshort-fandom-categories", "reelshort-fandom-post", "reelshort-fandom-posts", "reelshort-home", "reelshort-movie", "reelshort-new-releases", "reelshort-search", "reelshort-shelf", "reelshort-tag-books", "reelshort-tag-search", "reelshort-tags"];

    public function __construct(?string $apiKey = null, string $baseUrl = 'https://api.crawlora.net/api/v1', float $timeout = 30.0, ?callable $transport = null)
    {
        $this->apiKey = $apiKey ?? (getenv('CRAWLORA_API_KEY') ?: '');
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->transport = $transport === null ? null : \Closure::fromCallable($transport);
        self::$operations ??= json_decode(<<<'JSON'
{"reelshort-fandom-categories": {"bodyParam": null, "bodyRequired": false, "id": "reelshort-fandom-categories", "method": "GET", "params": [], "path": "/reelshort/fandom-categories", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "reelshort-fandom-post": {"bodyParam": null, "bodyRequired": false, "id": "reelshort-fandom-post", "method": "GET", "params": [{"description": "Article id (digits), article slug, or a reelshort.com/fandom URL", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "54181"}], "path": "/reelshort/fandom-post", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "reelshort-fandom-posts": {"bodyParam": null, "bodyRequired": false, "id": "reelshort-fandom-posts", "method": "GET", "params": [{"description": "Text to search articles for, up to 100 characters", "in": "query", "name": "search", "type": "string", "x-example": "alpha"}, {"description": "Category slug: general-topic, movie-cast-list, top-movie-stories, where-to-watch or where-to-watch-2", "enum": ["general-topic", "movie-cast-list", "top-movie-stories", "where-to-watch", "where-to-watch-2"], "in": "query", "name": "category", "type": "string", "x-example": "movie-cast-list"}, {"description": "Page number, 1 to 10000; defaults to 1", "in": "query", "name": "page", "type": "integer", "x-example": 2}, {"description": "Page size, 1 to 100; defaults to 10", "in": "query", "name": "limit", "type": "integer", "x-example": 10}], "path": "/reelshort/fandom-posts", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "search", "type": "string"}, {"enum": ["general-topic", "movie-cast-list", "top-movie-stories", "where-to-watch", "where-to-watch-2"], "in": "query", "name": "category", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "reelshort-home": {"bodyParam": null, "bodyRequired": false, "id": "reelshort-home", "method": "GET", "params": [{"description": "Site locale, one of: en, es, pt, fr, de, it, ja, ko, th, id, tr, ar, ru, pl, ro, cs, bg, vi, zh-TW; defaults to en. Titles and tags are translated", "enum": ["en", "es", "pt", "fr", "de", "it", "ja", "ko", "th", "id", "tr", "ar", "ru", "pl", "ro", "cs", "bg", "vi", "zh-TW"], "in": "query", "name": "language", "type": "string", "x-example": "es"}], "path": "/reelshort/home", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["en", "es", "pt", "fr", "de", "it", "ja", "ko", "th", "id", "tr", "ar", "ru", "pl", "ro", "cs", "bg", "vi", "zh-TW"], "in": "query", "name": "language", "type": "string"}], "security": ["ApiKeyAuth"]}, "reelshort-movie": {"bodyParam": null, "bodyRequired": false, "id": "reelshort-movie", "method": "GET", "params": [{"description": "Title id (24 hex characters) from reelshort-home, reelshort-shelf or reelshort-search, or a reelshort.com movie or episode URL", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "6a8752ac7c23cb02b40f062b"}], "path": "/reelshort/movie", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "reelshort-new-releases": {"bodyParam": null, "bodyRequired": false, "id": "reelshort-new-releases", "method": "GET", "params": [{"description": "A 24-character title id, from reelshort-movie, reelshort-shelf or reelshort-home; required by ReelShort but not observed to change the result", "in": "query", "name": "book_id", "required": true, "type": "string", "x-example": "6aac85383511c0b6df0eec87"}, {"description": "Site language, one of en, es, pt, fr, de, it, ja, ko, th, id, tr, ar, ru, pl, ro, cs, bg, vi, zh-TW; defaults to en", "enum": ["en", "es", "pt", "fr", "de", "it", "ja", "ko", "th", "id", "tr", "ar", "ru", "pl", "ro", "cs", "bg", "vi", "zh-TW"], "in": "query", "name": "language", "type": "string", "x-example": "en"}], "path": "/reelshort/new-releases", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "book_id", "required": true, "type": "string"}, {"enum": ["en", "es", "pt", "fr", "de", "it", "ja", "ko", "th", "id", "tr", "ar", "ru", "pl", "ro", "cs", "bg", "vi", "zh-TW"], "in": "query", "name": "language", "type": "string"}], "security": ["ApiKeyAuth"]}, "reelshort-search": {"bodyParam": null, "bodyRequired": false, "id": "reelshort-search", "method": "GET", "params": [{"description": "Title text to search for, up to 100 characters", "in": "query", "name": "keywords", "required": true, "type": "string", "x-example": "billionaire"}, {"description": "Page number, 1 to 200; defaults to 1. Each page holds 12 titles", "in": "query", "name": "page", "type": "integer", "x-example": 2}, {"description": "Site locale, one of: en, es, pt, fr, de, it, ja, ko, th, id, tr, ar, ru, pl, ro, cs, bg, vi, zh-TW; defaults to en. Titles and tags are translated", "enum": ["en", "es", "pt", "fr", "de", "it", "ja", "ko", "th", "id", "tr", "ar", "ru", "pl", "ro", "cs", "bg", "vi", "zh-TW"], "in": "query", "name": "language", "type": "string", "x-example": "es"}], "path": "/reelshort/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keywords", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"enum": ["en", "es", "pt", "fr", "de", "it", "ja", "ko", "th", "id", "tr", "ar", "ru", "pl", "ro", "cs", "bg", "vi", "zh-TW"], "in": "query", "name": "language", "type": "string"}], "security": ["ApiKeyAuth"]}, "reelshort-shelf": {"bodyParam": null, "bodyRequired": false, "id": "reelshort-shelf", "method": "GET", "params": [{"description": "Shelf id from reelshort-home (for example 51003506), or a reelshort.com shelf URL", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "51003506"}], "path": "/reelshort/shelf", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "reelshort-tag-books": {"bodyParam": null, "bodyRequired": false, "id": "reelshort-tag-books", "method": "GET", "params": [{"description": "Tag id, 24 lowercase hex characters, from reelshort-tags, reelshort-tag-search or reelshort-movie", "in": "query", "name": "tag_id", "required": true, "type": "string", "x-example": "676d210e4582b53a14081aab"}, {"description": "Page number, 1 to 10000; defaults to 1", "in": "query", "name": "page", "type": "integer", "x-example": 1}, {"description": "Page size, 1 to 100; defaults to 20", "in": "query", "name": "limit", "type": "integer", "x-example": 20}, {"description": "Site language, one of en, es, pt, fr, de, it, ja, ko, th, id, tr, ar, ru, pl, ro, cs, bg, vi, zh-TW; defaults to en", "enum": ["en", "es", "pt", "fr", "de", "it", "ja", "ko", "th", "id", "tr", "ar", "ru", "pl", "ro", "cs", "bg", "vi", "zh-TW"], "in": "query", "name": "language", "type": "string", "x-example": "en"}], "path": "/reelshort/tag-books", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "tag_id", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"enum": ["en", "es", "pt", "fr", "de", "it", "ja", "ko", "th", "id", "tr", "ar", "ru", "pl", "ro", "cs", "bg", "vi", "zh-TW"], "in": "query", "name": "language", "type": "string"}], "security": ["ApiKeyAuth"]}, "reelshort-tag-search": {"bodyParam": null, "bodyRequired": false, "id": "reelshort-tag-search", "method": "GET", "params": [{"description": "Tag text to search for, up to 100 characters", "in": "query", "name": "word", "required": true, "type": "string", "x-example": "Billionaire"}, {"description": "Page number, 1 to 10000; defaults to 1", "in": "query", "name": "page", "type": "integer", "x-example": 1}, {"description": "Site language, one of en, es, pt, fr, de, it, ja, ko, th, id, tr, ar, ru, pl, ro, cs, bg, vi, zh-TW; defaults to en", "enum": ["en", "es", "pt", "fr", "de", "it", "ja", "ko", "th", "id", "tr", "ar", "ru", "pl", "ro", "cs", "bg", "vi", "zh-TW"], "in": "query", "name": "language", "type": "string", "x-example": "en"}], "path": "/reelshort/tag-search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "word", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"enum": ["en", "es", "pt", "fr", "de", "it", "ja", "ko", "th", "id", "tr", "ar", "ru", "pl", "ro", "cs", "bg", "vi", "zh-TW"], "in": "query", "name": "language", "type": "string"}], "security": ["ApiKeyAuth"]}, "reelshort-tags": {"bodyParam": null, "bodyRequired": false, "id": "reelshort-tags", "method": "GET", "params": [{"description": "Tag category: actor, actress, identity or trope", "enum": ["actor", "actress", "identity", "trope"], "in": "query", "name": "category", "required": true, "type": "string", "x-example": "identity"}, {"description": "Site language, one of en, es, pt, fr, de, it, ja, ko, th, id, tr, ar, ru, pl, ro, cs, bg, vi, zh-TW; defaults to en", "enum": ["en", "es", "pt", "fr", "de", "it", "ja", "ko", "th", "id", "tr", "ar", "ru", "pl", "ro", "cs", "bg", "vi", "zh-TW"], "in": "query", "name": "language", "type": "string", "x-example": "en"}], "path": "/reelshort/tags", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["actor", "actress", "identity", "trope"], "in": "query", "name": "category", "required": true, "type": "string"}, {"enum": ["en", "es", "pt", "fr", "de", "it", "ja", "ko", "th", "id", "tr", "ar", "ru", "pl", "ro", "cs", "bg", "vi", "zh-TW"], "in": "query", "name": "language", "type": "string"}], "security": ["ApiKeyAuth"]}}
JSON, true, 512, JSON_THROW_ON_ERROR);
    }

    public function request(string $operationId, array $params = [], string $responseType = 'auto'): mixed
    {
        if ($this->closed) {
            throw new ClientException('Client is closed', null, $operationId);
        }
        $operation = self::$operations[$operationId] ?? null;
        if ($operation === null) {
            throw new ClientException('Unknown operation: ' . $operationId, null, $operationId);
        }
        if ($this->apiKey === '') {
            throw new ClientException('Crawlora API key is required', null, $operationId);
        }
        $payload = $this->requestBody($operation, $params);
        $url = $this->buildUrl($operation, $params);
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'User-Agent: crawlora-reelshort-php/0.1.0',
            'Accept: ' . (in_array('text/plain', $operation['produces'], true) ? 'application/json, text/plain' : 'application/json'),
        ];
        if ($payload !== null) {
            $headers[] = 'Content-Type: application/json';
        }
        try {
            [$status, $contentType, $body] = $this->send($url, $headers, $operationId, $operation['method'], $payload);
        } catch (CrawloraException $exception) {
            throw $exception;
        } catch (\Throwable $exception) {
            throw new NetworkException('Crawlora request failed: ' . $exception->getMessage(), null, $operationId, null, $exception);
        }
        if ($status < 200 || $status >= 300) {
            $class = $status >= 500 ? ServerException::class : ClientException::class;
            throw new $class('Crawlora returned HTTP ' . $status, $status, $operationId, $body);
        }
        return $this->parseResponse($body, $contentType, $operation, $params, $responseType);
    }

    public function close(): void
    {
        $this->closed = true;
    }

    public function isClosed(): bool
    {
        return $this->closed;
    }

    public function operationCount(): int
    {
        return self::OPERATION_COUNT;
    }

    public function operationIds(): array
    {
        return self::OPERATION_IDS;
    }

    public function operations(): array
    {
        return self::$operations;
    }

    public function fandom_categories(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reelshort-fandom-categories", $params, $responseType);
    }
    public function fandom_post(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reelshort-fandom-post", $params, $responseType);
    }
    public function fandom_posts(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reelshort-fandom-posts", $params, $responseType);
    }
    public function home(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reelshort-home", $params, $responseType);
    }
    public function movie(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reelshort-movie", $params, $responseType);
    }
    public function new_releases(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reelshort-new-releases", $params, $responseType);
    }
    public function search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reelshort-search", $params, $responseType);
    }
    public function shelf(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reelshort-shelf", $params, $responseType);
    }
    public function tag_books(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reelshort-tag-books", $params, $responseType);
    }
    public function tag_search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reelshort-tag-search", $params, $responseType);
    }
    public function tags(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reelshort-tags", $params, $responseType);
    }

    /** POST operations take their JSON body under the body parameter name or "body". */
    private function requestBody(array $operation, array $params): ?string
    {
        $name = $operation['bodyParam'] ?? null;
        if ($name === null) {
            return null;
        }
        $value = $params[$name] ?? ($params['body'] ?? null);
        if ($value === null) {
            if ($operation['bodyRequired'] ?? false) {
                throw new ClientException('Missing request body: ' . $name, null, $operation['id']);
            }
            return null;
        }
        return is_string($value) ? $value : json_encode($value, JSON_THROW_ON_ERROR);
    }

    private function buildUrl(array $operation, array $params): string
    {
        $known = array_column($operation['params'], 'name');
        if (($operation['bodyParam'] ?? null) !== null) {
            $known[] = 'body';
        }
        $unknown = array_diff(array_keys($params), $known, ['response_type', '_response_type']);
        if ($unknown !== []) {
            throw new ClientException('Unknown parameters: ' . implode(', ', $unknown), null, $operation['id']);
        }
        $path = $operation['path'];
        foreach ($operation['params'] as $param) {
            if ($param['in'] !== 'path') {
                continue;
            }
            $name = $param['name'];
            if (!array_key_exists($name, $params) || $params[$name] === null) {
                throw new ClientException('Missing path parameter: ' . $name, null, $operation['id']);
            }
            $path = str_replace('{' . $name . '}', rawurlencode((string) $params[$name]), $path);
        }
        $pairs = [];
        foreach ($operation['queryParams'] as $param) {
            $name = $param['name'];
            $value = $params[$name] ?? ($param['default'] ?? null);
            if ($value === null) {
                if ($param['required'] ?? false) {
                    throw new ClientException('Missing query parameter: ' . $name, null, $operation['id']);
                }
                continue;
            }
            $enumValues = $param['enum'] ?? ($param['items']['enum'] ?? null);
            $values = is_array($value) ? $value : [$value];
            $invalidEnum = false;
            foreach ($values as $item) {
                if ($enumValues !== null && !in_array((string) $item, array_map('strval', $enumValues), true)) {
                    $invalidEnum = true;
                    break;
                }
            }
            if ($invalidEnum) {
                throw new ClientException('Invalid value for ' . $name, null, $operation['id']);
            }
            if (is_array($value)) {
                $format = $param['collectionFormat'] ?? 'csv';
                if ($format === 'multi') {
                    foreach ($value as $item) {
                        $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($item))];
                    }
                } else {
                    $separator = ['csv' => ',', 'ssv' => ' ', 'tsv' => "\t", 'pipes' => '|'][$format] ?? ',';
                    $pairs[] = [rawurlencode($name), rawurlencode(implode($separator, array_map([$this, 'stringify'], $value)))];
                }
            } else {
                $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($value))];
            }
        }
        $query = implode('&', array_map(static fn(array $pair): string => $pair[0] . '=' . $pair[1], $pairs));
        return $this->baseUrl . $path . ($query === '' ? '' : '?' . $query);
    }

    private function stringify(mixed $value): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }
        if (is_array($value)) {
            return json_encode($value, JSON_THROW_ON_ERROR);
        }
        return (string) $value;
    }

    private function send(string $url, array $headers, string $operationId, string $method = 'GET', ?string $payload = null): array
    {
        if ($this->transport !== null) {
            $result = $method === 'POST'
                ? ($this->transport)($url, $headers, $this->timeout, $method, $payload)
                : ($this->transport)($url, $headers, $this->timeout);
            return [(int) $result['status'], (string) ($result['content_type'] ?? ''), (string) ($result['body'] ?? '')];
        }
        $handle = curl_init($url);
        if ($handle === false) {
            throw new NetworkException('Could not initialize cURL', null, $operationId);
        }
        curl_setopt_array($handle, $method === 'POST' ? [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $payload ?? '',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ] : [
            CURLOPT_HTTPGET => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ]);
        $body = curl_exec($handle);
        if ($body === false) {
            $message = curl_error($handle);
            curl_close($handle);
            throw new NetworkException('Crawlora request failed: ' . $message, null, $operationId);
        }
        $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
        $contentType = (string) curl_getinfo($handle, CURLINFO_CONTENT_TYPE);
        curl_close($handle);
        return [$status, $contentType, (string) $body];
    }

    private function parseResponse(string $body, string $contentType, array $operation, array $params, string $responseType): mixed
    {
        if (!in_array($responseType, ['auto', 'json', 'text'], true)) {
            throw new ClientException('responseType must be auto, json, or text', null, $operation['id']);
        }
        $format = null;
        foreach ($operation['params'] as $param) {
            if ($param['name'] === 'format') {
                $format = $param;
                break;
            }
        }
        $textFormats = array_values(array_filter($format['enum'] ?? [], static fn($value): bool => !in_array(strtolower((string) $value), ['json', 'application/json'], true)));
        $rawFormat = isset($params['format']) && in_array((string) $params['format'], array_map('strval', $textFormats), true);
        $jsonFormat = isset($params['format']) && in_array(strtolower((string) $params['format']), ['json', 'application/json'], true);
        $isJson = $jsonFormat || stripos($contentType, 'json') !== false || $operation['produces'] === ['application/json'];
        if ($responseType === 'text' || $rawFormat || ($responseType === 'auto' && !$isJson)) {
            return $body;
        }
        try {
            return json_decode($body, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new CrawloraException('Invalid JSON response from Crawlora: ' . $exception->getMessage(), null, $operation['id'], $body, $exception);
        }
    }
}
