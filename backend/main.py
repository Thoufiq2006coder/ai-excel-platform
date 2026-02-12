import uvicorn
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import pandas as pd
import io
import json
import os

# --- AI CONFIGURATION (HARDCODED FOR SPEED) ---
API_KEY = "AIzaSyA16-bgTd3ZIHe5rBlr9jIEUSQHC15Qqk0"  # Your Key

try:
    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain_core.prompts import ChatPromptTemplate
    
    # Using Flash model for speed
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash", 
        google_api_key=API_KEY
    )
    AI_AVAILABLE = True
    print("✅ AI Engine Connected (Gemini Flash)")
except Exception as e:
    print(f"⚠️ AI Module Error: {e}")
    AI_AVAILABLE = False

app = FastAPI()

# --- CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    text: str

current_df = None

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    global current_df
    try:
        contents = await file.read()
        filename = file.filename.lower()
        
        # INSIDE upload_file FUNCTION:
        if filename.endswith('.csv'):
            df = pd.read_csv(io.BytesIO(contents))
        elif filename.endswith('.tsv'):
            df = pd.read_csv(io.BytesIO(contents), sep='\t')
        elif filename.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(io.BytesIO(contents))
        elif filename.endswith('.json'):
            # NEW: Support for JSON upload
            df = pd.read_json(io.BytesIO(contents))
        else:
            return {"error": "Invalid file type. Please upload CSV, Excel, or JSON."}
        
        df = df.fillna("")
        current_df = df
        
        # Preview first 20 rows
        preview = df.head(40).to_dict(orient='records')
        return {
            "status": "success", 
            "preview": preview, 
            "filename": file.filename,
            "columns": df.columns.tolist()
        }
    except Exception as e:
        return {"error": str(e)}

@app.post("/analyze")
async def analyze(request: ChatRequest):
    global current_df
    if current_df is None:
        return {"insights": ["⚠️ Please upload a file first."]}
    
    if AI_AVAILABLE:
        try:
            # Context: First 10 rows
            data_preview = str(current_df.head(10).to_dict())
            
            prompt = ChatPromptTemplate.from_template(
                """You are an Expert Data Analyst.
                Data Preview: {data}
                User Question: {query}
                
                Return a JSON object with a single key "insights" (list of strings).
                Example: {{"insights": ["Total revenue is $50k", "Formula: =SUM(B:B)"]}}
                DO NOT output Markdown."""
            )
            
            chain = prompt | llm
            res = chain.invoke({"data": data_preview, "query": request.text})
            
            clean_json = res.content.replace("```json", "").replace("```", "").strip()
            return json.loads(clean_json)
        except Exception as e:
            return {"insights": [f"AI Error: {str(e)}"]}
    else:
        return {"insights": ["AI Disconnected."]}

@app.get("/download")
async def download():
    global current_df
    if current_df is None: return {"error": "No data"}
    
    stream = io.StringIO()
    current_df.to_csv(stream, index=False)
    response = StreamingResponse(iter([stream.getvalue()]), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=export.csv"
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)