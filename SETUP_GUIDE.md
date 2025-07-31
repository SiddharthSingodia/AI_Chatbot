# Complete Setup Guide for Medical Chatbot

## Step 1: Fix Python Installation Issue

### Option A: Use Python Launcher (Recommended)
Since you have Python installed but `python` command doesn't work, use `py` instead:

```bash
# Check Python version
py --version

# Use py for all Python commands
py -m pip install -r requirements.txt
py store_index.py
py app.py
```

### Option B: Add Python to PATH (Permanent Fix)
1. Open Windows Settings
2. Go to "Apps" → "Advanced app settings" → "App execution aliases"
3. Turn OFF "python.exe" and "python3.exe"
4. Add Python to PATH:
   - Open System Properties → Advanced → Environment Variables
   - Add `C:\Users\asus\AppData\Local\Programs\Python\Python312\` to PATH
   - Add `C:\Users\asus\AppData\Local\Programs\Python\Python312\Scripts\` to PATH

## Step 2: Install Dependencies

```bash
# Navigate to project directory
cd "C:\Users\asus\OneDrive\Desktop\Build-a-Complete-Medical-Chatbot-with-LLMs-LangChain-Pinecone-Flask-AWS-main"

# Install requirements
py -m pip install -r requirements.txt
```

## Step 3: Set Up Environment Variables

Create a `.env` file in the project root:

```bash
# Create .env file
echo PINECONE_API_KEY=your_pinecone_api_key_here > .env
echo GEMINI_API_KEY=your_gemini_api_key_here >> .env
```

Or manually create `.env` file with:
```
PINECONE_API_KEY=your_pinecone_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

## Step 4: Get API Keys

### Pinecone API Key:
1. Go to [Pinecone Console](https://app.pinecone.io/)
2. Create account/login
3. Create a new project
4. Go to API Keys section
5. Copy your API key

### Gemini API Key:
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create account/login
3. Create a new API key
4. Copy the API key

## Step 5: Update .env File

Replace the placeholder values in `.env`:
```
PINECONE_API_KEY=your_actual_pinecone_api_key
GEMINI_API_KEY=your_actual_gemini_api_key
```

## Step 6: Store Embeddings

```bash
# Run the script to store embeddings in Pinecone
py store_index.py
```

## Step 7: Run the Application

```bash
# Start the Flask application
py app.py
```

## Step 8: Access the Application

Open your web browser and go to:
```
http://localhost:8080
```

## Troubleshooting

### If you get "Python was not found":
- Use `py` instead of `python`
- Example: `py -m pip install package_name`

### If you get import errors:
```bash
# Reinstall requirements
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
```

### If you get API key errors:
- Make sure your `.env` file exists in the project root
- Verify your API keys are correct
- Check that the keys are active in their respective consoles

### If you get Pinecone region errors:
- The code is already configured to use `us-east-1` region
- Make sure your Pinecone project is in the same region

## Complete Command Sequence

```bash
# 1. Navigate to project
cd "C:\Users\asus\OneDrive\Desktop\Build-a-Complete-Medical-Chatbot-with-LLMs-LangChain-Pinecone-Flask-AWS-main"

# 2. Install dependencies
py -m pip install -r requirements.txt

# 3. Create .env file (replace with your actual keys)
echo PINECONE_API_KEY=your_actual_pinecone_key > .env
echo GEMINI_API_KEY=your_actual_gemini_key >> .env

# 4. Store embeddings
py store_index.py

# 5. Run application
py app.py

# 6. Open browser
start http://localhost:8080
```

## Verification Steps

1. **Check Python**: `py --version` should show Python 3.12.8
2. **Check Dependencies**: `py -m pip list` should show all packages installed
3. **Check .env**: File should exist with your API keys
4. **Check Application**: Browser should show the chat interface at localhost:8080

## Deployment Ready

Once local setup works, you can deploy to:
- Render
- Vercel  
- Railway
- Heroku

See `DEPLOYMENT.md` for deployment instructions. 