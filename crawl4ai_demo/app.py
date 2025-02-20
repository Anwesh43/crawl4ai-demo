from crawl4ai import *
from llama_index.core import VectorStoreIndex, Document 
import asyncio
import sys 
import dotenv
import sys
from Indexer import indexer
from DataExtractor import dataExtractor 

dotenv.load_dotenv()


async def extract(site : str, promptSentence : str):
    await dataExtractor.crawl(site)
    for data in dataExtractor.load_data():
        indexer.addDocument(data)
    for prompt in promptSentence.split("? "):
        print(indexer.query(prompt))
    

if __name__ == "__main__" and len(sys.argv) == 2:
    print("Running by creating objects")
    asyncio.run(extract(sys.argv[1], "Who we are referring to? And What does this person do? Where was he born"))
