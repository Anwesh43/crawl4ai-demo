from crawl4ai import *
import asyncio
import sys 
async def extract(site : str):
    print("Getting data of {0}".format(site))
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url = site)
        print(result.markdown)

if __name__ == "__main__" and len(sys.argv) == 2:
    asyncio.run(extract(sys.argv[1]))