# Crawlora ReelShort API client for Java

The official Java client for Crawlora's hosted ReelShort API. It exposes 11 endpoints covering title discovery, search, movie details, new releases, and public Fandom articles. Requests use your `x-api-key`; the client does not connect to the upstream site directly.

## Install

```xml
<dependency>
  <groupId>net.crawlora</groupId>
  <artifactId>crawlora-reelshort</artifactId>
  <version>0.1.0</version>
</dependency>
```

## Use

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=reelshort-java-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=reelshort-java-console) to get an API key.

```java
import net.crawlora.reelshort.Client;
import java.time.Duration;
import java.util.Map;

try (Client client = new Client(System.getenv("CRAWLORA_API_KEY"))) {
    Object result = client.home(Map.of());
    System.out.println(result);
}
```

Each operation has a direct method that accepts the parameters documented for that endpoint. Use `client.request(operationId, params)` for generic dispatch. `Client.OPERATION_IDS`, `Client.OPERATION_COUNT`, `client.getOperationIds()`, and `client.getOperationCount()` describe this platform's operations only.

For custom hosted API routing and timeouts, use `new Client(apiKey, baseUrl, Duration.ofSeconds(20))`. Text responses are returned as `String`; JSON responses are parsed into Java maps, lists, and scalar values.

## Supported ReelShort API endpoints

Browse every route included in this Java package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-reelshort/blob/main/docs/usage.md) also lists parameters and response details.

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

## Links

- [Crawlora](https://crawlora.net/?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=reelshort-java-homepage)
- [Crawlora platform clients](https://github.com/Crawlora-org/crawlora-reelshort)
- [API documentation](https://crawlora.net/docs?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=reelshort-java-api-docs)
