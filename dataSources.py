from llama_index.readers.google import GoogleDriveReader
from llama_index.core import Settings
from llama_index.embeddings.azure_openai import AzureOpenAIEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import VectorStoreIndex,SummaryIndex
from llama_index.core import ServiceContext, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb

#print current time
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()

llm = OpenAI(
    model="gpt-4"
)
Settings.llm = llm

embed_model = AzureOpenAIEmbedding(
    model=os.getenv("EMBD_MODEL"),
    deployment_name=os.getenv("EMBD_DEPLOYMENT"),
    api_key=os.getenv('API_KEY'),
    azure_endpoint=os.getenv('ENDPOINT'),
    api_version="2024-02-15-preview",
)
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
            chroma_client = chromadb.EphemeralClient()
            chroma_collection = chroma_client.create_collection(datetime.now().strftime("%Y%m%d%H%M%S"))
            vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
            service_context = ServiceContext.from_defaults(embed_model=embed_model,llm=llm)
            storage_context = StorageContext.from_defaults(vector_store=vector_store)
            index = VectorStoreIndex.from_documents(self.documents,
                                                    service_context=service_context,
                                                    storage_context=storage_context)
            query_engine = index.as_query_engine()
            return query_engine
        elif self.type == "Gdrive":
            # Make sure credentials.json file exists in the current directory (data_connectors)
            documents = GoogleDriveReader().load_data(folder_id=self.content)
            index = VectorStoreIndex.from_documents(documents)
            # Set Logging to DEBUG for more detailed outputs
            query_engine = index.as_query_engine()

            return query_engine