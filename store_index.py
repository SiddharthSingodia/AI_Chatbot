from dotenv import load_dotenv
import os
from src.helper import load_pdf_file, filter_to_minimal_docs, text_split
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from pinecone import Pinecone
from pinecone import ServerlessSpec 
from langchain_pinecone import PineconeVectorStore
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()

PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')
GEMINI_API_KEY=os.environ.get('GEMINI_API_KEY')

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY

extracted_data=load_pdf_file(data='data/')
print(f"Loaded {len(extracted_data)} documents from PDF files")

filter_data = filter_to_minimal_docs(extracted_data)
print(f"Filtered to {len(filter_data)} documents")

text_chunks=text_split(filter_data)
print(f"Created {len(text_chunks)} text chunks")

# Filter out chunks that are too long for Pinecone (max ~4MB)
max_chunk_size = 4000000  # 4MB limit
filtered_chunks = []
for chunk in text_chunks:
    if len(chunk.page_content.encode('utf-8')) < max_chunk_size:
        filtered_chunks.append(chunk)
    else:
        print(f"Filtering out chunk with size: {len(chunk.page_content.encode('utf-8'))} bytes")

text_chunks = filtered_chunks
print(f"After filtering: {len(text_chunks)} chunks remain")

# Use Gemini embeddings with 768 dimensions (default for embedding-001)
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=GEMINI_API_KEY
    # Remove task_type to get default 768 dimensions
)
print("Gemini embeddings model loaded successfully")

pinecone_api_key = PINECONE_API_KEY
pc = Pinecone(api_key=pinecone_api_key)

index_name = "medical-chatbot"  # change if desired

# Delete existing index first to avoid dimension mismatch
if pc.has_index(index_name):
    print(f"Deleting existing index: {index_name}")
    pc.delete_index(index_name)
    print("Waiting for index deletion to complete...")
    import time
    time.sleep(10)  # Wait for deletion to complete

# Create new index with 768 dimensions for Gemini embeddings
try:
    print(f"Creating new index: {index_name} with 768 dimensions...")
    pc.create_index(
        name=index_name,
        dimension=768,  # Gemini embedding-001 uses 768 dimensions
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),  # Using supported region
    )
    print(f"Index {index_name} created successfully!")
except Exception as e:
    print(f"Error creating index: {e}")
    exit(1)

index = pc.Index(index_name)

# Upload documents in smaller batches to avoid message size limits
try:
    print("Starting document upload to Pinecone...")
    batch_size = 100  # Process in smaller batches
    
    for i in range(0, len(text_chunks), batch_size):
        batch = text_chunks[i:i + batch_size]
        print(f"Uploading batch {i//batch_size + 1}/{(len(text_chunks) + batch_size - 1)//batch_size} ({len(batch)} chunks)")
        
        docsearch = PineconeVectorStore.from_documents(
            documents=batch,
            index_name=index_name,
            embedding=embeddings, 
        )
        print(f"Batch {i//batch_size + 1} uploaded successfully!")
    
    print("All documents uploaded successfully!")
    
except Exception as e:
    print(f"Error uploading documents: {e}")
    print("Trying alternative approach...")
    
    # Alternative: upload one by one
    try:
        for i, chunk in enumerate(text_chunks):
            if i % 100 == 0:
                print(f"Uploading chunk {i+1}/{len(text_chunks)}")
            
            docsearch = PineconeVectorStore.from_documents(
                documents=[chunk],
                index_name=index_name,
                embedding=embeddings, 
            )
        print("All documents uploaded successfully using alternative method!")
    except Exception as e2:
        print(f"Alternative method also failed: {e2}")
        exit(1)