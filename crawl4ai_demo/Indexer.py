from llama_index.core import VectorStoreIndex, Document
class Indexer:

    def __init__(self):
        self.documents = [] 

    def addDocument(self, text : str):
        self.documents.append(Document(text = text))
        self.index = VectorStoreIndex.from_documents(self.documents)
        self.query_engine = self.index.as_query_engine()
    
    def query(self, prompt : str) -> str:
        return self.query_engine.query(prompt)

    
indexer = Indexer()