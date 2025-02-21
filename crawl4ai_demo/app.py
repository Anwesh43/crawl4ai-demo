from crawl4ai import *
from llama_index.core import VectorStoreIndex, Document
import asyncio
import sys
import dotenv
import sys
from Indexer import Indexer
from DataExtractor import DataExtractor
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

dotenv.load_dotenv()


# async def extract(site : str, promptSentence : str):
#     await dataExtractor.crawl(site)
#     for data in dataExtractor.load_data():
#         indexer.addDocument(data)
#     for prompt in promptSentence.split("? "):
#         print(indexer.query(prompt))

#     uvicorn.run('app:app', port = 5000, reload = True)


# if __name__ == "__main__" and len(sys.argv) == 2:
#     print("Running by creating objects")
#     asyncio.run(extract(sys.argv[1], "Who we are referring to? And What does this person do? Where was he born"))


class Engine:
    def __init__(self):
        self.indexer = Indexer()
        self.dataExtractor = DataExtractor()

    async def crawlInject(self, url: str):
        await self.dataExtractor.crawl(url)
        for data in self.dataExtractor.load_data():
            self.indexer.addDocument(data)

    def query(self, query: str) -> str:
        return self.indexer.query(query)


engine = Engine()

app = FastAPI()


@app.get("/query/{query_str}")
def query(query_str: str):
    return {
        "result": engine.query(query_str)
    }


class UrlInput(BaseModel):
    url: str


@app.post("/inject")
async def inject(urlInput: UrlInput):
    print("URL is {0}".format(urlInput.url))
    await engine.crawlInject(urlInput.url)
    return {
        "status": "success"
    }
if __name__ == "__main__":
    uvicorn.run('app:app', port=5000, loop='asyncio')
