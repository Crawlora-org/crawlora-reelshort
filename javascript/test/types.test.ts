import { ReelShortClient } from "../src/index.js";

const client = new ReelShortClient({ apiKey: "test-key" });
void client.fandomPost({"id": "sample"});
void client.request("reelshort-fandom-post", {"id": "sample"});
const streamResponse: Promise<Response> = client.request("reelshort-fandom-post", {"id": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("reelshort-fandom-post", {"id": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.fandomPost({"id": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("reelshort-fandom-post", {"id": "sample"}, { responseType: "text" });
const rawText: Promise<string> = client.request("reelshort-fandom-post", {"id": "sample"}, { responseType: "text" });
void rawText;


void client.fandomCategories();
void client.request("reelshort-fandom-categories");
// @ts-expect-error The selected operation requires its documented params.
void client.fandomPost();
