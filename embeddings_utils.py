import openai  
from pinecone import Pinecone

class EmbeddingUtils:  
    def __init__(self, openai_api_key, pinecone_api_key, pinecone_environment, pinecone_index_name):  
        # Initialize OpenAI and Pinecone  
        openai.api_key = openai_api_key  
        self.pc = Pinecone(api_key=pinecone_api_key)
        self.index = self.pc.Index(pinecone_index_name) 

    def generate_embedding(self, text):  
        """  
        Generate embedding for a given text using OpenAI's text-embedding-ada-002 model.  
        """  
        response = openai.Embedding.create(  
            input=text,  
            model="text-embedding-ada-002"  
        )  
        return response["data"][0]["embedding"]  

    def upsert_embeddings(self, content_chunks):  
        """  
        Upsert text chunks and their embeddings to the Pinecone index.  
        """  
        for i, chunk in enumerate(content_chunks):  
            embedding = self.generate_embedding(chunk["content"])  
            metadata = {"title": chunk["title"]}  
            self.index.upsert([{  
                "id": f"doc-{i}",  
                "values": embedding,  
                "metadata": metadata  
            }])  

    def query_embeddings(self, query, top_k=5):  
        """  
        Query Pinecone to retrieve the most relevant chunks.  
        """  
        query_embedding = self.generate_embedding(query)  
        results = self.index.query(  
            vector=query_embedding,  
            top_k=top_k,  
            include_metadata=True  
        )  
        return results  