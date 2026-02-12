# backend/ai_service.py
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Load API Key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

class AIService:
    def __init__(self):
        # Initialize Gemini
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key="AIzaSyA16-bgTd3ZIHe5rBlr9jIEUSQHC15Qqk0",
            temperature=0.2
        )

    def analyze(self, query: str, data_preview: list):
        # 1. Create a prompt that gives the AI the data context
        prompt = ChatPromptTemplate.from_template("""
            You are an Expert Data Analyst.
            Here is the first few rows of the user's dataset:
            {data_preview}

            The user asks: "{query}"

            If they ask for a calculation, give the answer and the Excel formula.
            If they ask for a summary, describe the data columns and trends.
            
            Format your response as a JSON object with this key:
            "insights": ["Point 1", "Point 2", "Formula: ..."]
            
            Do not include markdown formatting like ```json. Just raw JSON.
        """)

        # 2. Convert data list to string for the prompt
        data_str = str(data_preview)

        # 3. Get response
        chain = prompt | self.llm
        try:
            response = chain.invoke({"data_preview": data_str, "query": query})
            # Clean up response if AI adds markdown
            clean_content = response.content.replace("```json", "").replace("```", "").strip()
            return clean_content
        except Exception as e:
            return f'{{"insights": ["Error connecting to AI: {str(e)}"]}}'