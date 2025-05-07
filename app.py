from flask import Flask, request, jsonify, send_from_directory
from notion_utils import NotionAPI  
from embeddings_utils import EmbeddingUtils  
import os  
import openai  
from dotenv import load_dotenv
from flask_cors import CORS

# Load environment variables from .env file
load_dotenv()

# Load environment variables or API keys directly  
NOTION_API_KEY = os.getenv("NOTION_API_KEY")  
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")  
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")  
PINECONE_ENV = os.getenv("PINECONE_ENVIRONMENT")  
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")  

# Initialize Notion and Embedding utilities  
notion_api = NotionAPI(api_key=NOTION_API_KEY)  
embedding_utils = EmbeddingUtils(  
    openai_api_key=OPENAI_API_KEY,  
    pinecone_api_key=PINECONE_API_KEY,  
    pinecone_environment=PINECONE_ENV,  
    pinecone_index_name=PINECONE_INDEX_NAME  
)  

# Flask app setup  
app = Flask(__name__)  
CORS(app)  # Enable CORS for all routes

# Disable caching in development
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

@app.route("/")
def home():
    return send_from_directory('.', 'template/index.html')

@app.route("/ingest", methods=["POST"])  
def ingest_data():  
    """  
    API endpoint to extract data from Notion and store embeddings in Pinecone.  
    """  
    notion_data = notion_api.fetch_database_data(DATABASE_ID)  
    print(notion_data)
    embedding_utils.upsert_embeddings(notion_data)  
    return jsonify({"message": "Data ingested successfully!"})  

@app.route("/query", methods=["POST"])  
def query_data():  
    """  
    API endpoint to query data and get context-aware answers.  
    """  
    user_input = request.json.get("query")  
    results = embedding_utils.query_embeddings(user_input)  
    context = "\n".join([f"Name: {result['metadata']['name']}, Tech: {result['metadata']['tech']}, Experience: {result['metadata']['experience']}" for result in results["matches"]])  
    print(context)
    # Generate response with OpenAI  
    prompt = f"""  
    You are a helpful assistant. Use the following context to answer the user's query:  

    Context:  
    {context}  

    Question: {user_input}  
    """  
    openai_response = openai.ChatCompletion.create(  
        model="gpt-4",  
        messages=[{"role": "system", "content": prompt}]  
    )  
    answer = openai_response["choices"][0]["message"]["content"]  
    return jsonify({"answer": answer})  

if __name__ == "__main__":  
    app.run(host='127.0.0.1', port=9000, debug=True, use_reloader=False)  