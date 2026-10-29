import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class ReelShortClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-reelshort-js/0.1.0" });
    this["fandomCategories"] = (...args) => this.request("reelshort-fandom-categories", ...args);
    this["fandomPost"] = (...args) => this.request("reelshort-fandom-post", ...args);
    this["fandomPosts"] = (...args) => this.request("reelshort-fandom-posts", ...args);
    this["home"] = (...args) => this.request("reelshort-home", ...args);
    this["movie"] = (...args) => this.request("reelshort-movie", ...args);
    this["newReleases"] = (...args) => this.request("reelshort-new-releases", ...args);
    this["search"] = (...args) => this.request("reelshort-search", ...args);
    this["shelf"] = (...args) => this.request("reelshort-shelf", ...args);
    this["tagBooks"] = (...args) => this.request("reelshort-tag-books", ...args);
    this["tagSearch"] = (...args) => this.request("reelshort-tag-search", ...args);
    this["tags"] = (...args) => this.request("reelshort-tags", ...args);
  }
}

export { ReelShortClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.0";
export default ReelShortClient;
