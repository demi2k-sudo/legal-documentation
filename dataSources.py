from llama_index.core import Settings
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import VectorStoreIndex,SummaryIndex

__import__ ('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

#print current time
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()



llm = OpenAI(
    model="gpt-3.5-turbo"
)
Settings.llm = llm

embed_model = OpenAIEmbedding(model="text-embedding-3-large")

Settings.embed_model = embed_model


class QueryEngine:
    def __init__(self, type, content):
        self.type = type
        if type == "Gdrive":
            self.content = content
        elif type == "Upload":
            self.documents = SimpleDirectoryReader(input_files=content).load_data()
            
    def get_query_engine(self):
        if self.type == "Upload":
            # chroma_client = chromadb.EphemeralClient()
            # chroma_collection = chroma_client.create_collection(datetime.now().strftime("%Y%m%d%H%M%S"))
            # vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
            # service_context = ServiceContext.from_defaults(embed_model=embed_model,llm=llm)
            # storage_context = StorageContext.from_defaults(vector_store=vector_store)
            index = VectorStoreIndex.from_documents(self.documents)
            query_engine = index.as_query_engine()
            return query_engine
