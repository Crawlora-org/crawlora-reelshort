import os

from crawlora_reelshort import ReelShortClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with ReelShortClient(api_key=api_key) as client:
    home = client.home()
    print('home', home)
    search = client.search(keywords='romance')
    print('search', search)
