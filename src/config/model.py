from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
gemini_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-preview-09-2025")
openai_model = ChatOpenAI(model="gpt-5.1")