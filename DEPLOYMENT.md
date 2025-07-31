# Deployment Guide

## Environment Variables Required

Set these environment variables in your deployment platform:

```
PINECONE_API_KEY=your_pinecone_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

## Getting API Keys

### Pinecone API Key
1. Go to [Pinecone Console](https://app.pinecone.io/)
2. Create a new project or use existing one
3. Go to API Keys section
4. Copy your API key

### Gemini API Key
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the API key

## Deployment Platforms

### Render
1. Connect your GitHub repository
2. Set environment variables in the dashboard
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn app:app`

### Vercel
1. Connect your GitHub repository
2. Set environment variables in the dashboard
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn app:app`

### Railway
1. Connect your GitHub repository
2. Set environment variables in the dashboard
3. Deploy automatically

### Heroku
1. Connect your GitHub repository
2. Set environment variables in the dashboard
3. Deploy automatically

## Local Development

1. Create a `.env` file with your API keys
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`

## Notes

- The application uses Pinecone with AWS region `us-east-1` (supports global access)
- Uses Gemini 1.5 Flash model for chat responses
- Uses HuggingFace embeddings for vector search
- Configured for production deployment with Gunicorn 