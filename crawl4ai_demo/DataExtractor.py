from crawl4ai import AsyncWebCrawler

class DataExtractor:
    
    def __init__(self):
        self.url_content_map = {}
    
    async def crawl(self, url):
        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun(url)
            self.url_content_map[url] = result.markdown 
            print("Type of markdown")
            print(type(result.markdown))
    
    def load_data(self):
        contents = []
        for k in self.url_content_map.keys():
            contents.append(self.url_content_map[k])
        return contents

dataExtractor = DataExtractor()