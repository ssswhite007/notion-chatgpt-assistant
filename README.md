# Notion ChatGPT Assistant

A powerful AI assistant that combines Notion database data with ChatGPT to provide intelligent, context-aware responses about your Notion content.

## Features

- 🔄 **Notion Integration**: Seamlessly connects with your Notion database to access and analyze your data
- 🤖 **AI-Powered Responses**: Uses GPT-4 to provide intelligent, context-aware answers
- 🔍 **Semantic Search**: Employs embeddings to find the most relevant information from your Notion data
- 💾 **Vector Storage**: Uses Pinecone for efficient storage and retrieval of embeddings
- 🌐 **Modern Web Interface**: Clean, responsive UI built with Tailwind CSS
- ⚡ **Real-time Updates**: Instant responses with loading indicators

## Architecture

The project consists of three main components:

1. **Backend (Flask)**
   - Handles API requests
   - Manages Notion API integration
   - Processes embeddings
   - Interfaces with OpenAI's GPT-4
   - Serves the frontend

2. **Frontend (HTML/JavaScript)**
   - Modern, responsive UI
   - Real-time query interface
   - Loading states and error handling
   - Clean, user-friendly design

3. **Data Processing**
   - Notion data extraction
   - Embedding generation
   - Vector storage in Pinecone
   - Context-aware response generation

## Setup

1. **Environment Variables**
   Create a `.env` file with the following variables:
   ```
   NOTION_API_KEY=your_notion_api_key
   NOTION_DATABASE_ID=your_database_id
   OPENAI_API_KEY=your_openai_api_key
   PINECONE_API_KEY=your_pinecone_api_key
   PINECONE_ENVIRONMENT=your_pinecone_environment
   PINECONE_INDEX_NAME=your_index_name
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   python app.py
   ```

4. **Access the Application**
   Open your browser and navigate to `http://127.0.0.1:9000`

## API Endpoints

- `GET /`: Serves the main application interface
- `POST /ingest`: Extracts data from Notion and stores embeddings in Pinecone
- `POST /query`: Processes user queries and returns AI-generated responses

## Technologies Used

- **Backend**:
  - Flask (Python web framework)
  - Notion API
  - OpenAI API (GPT-4)
  - Pinecone (Vector database)

- **Frontend**:
  - HTML5
  - JavaScript (ES6+)
  - Tailwind CSS
  - Fetch API

## Development

The application is configured for development with:
- Hot reloading enabled
- Caching disabled for immediate updates
- Debug mode for detailed error messages

## Future Enhancements

Potential improvements could include:
- User authentication
- Multiple Notion database support
- Conversation history
- Custom embedding models
- Advanced filtering options
- Export functionality

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details. 