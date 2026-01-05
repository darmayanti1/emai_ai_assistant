import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

MODEL_NAME = "models/gemini-3-flash-preview"

def load_model():
    return genai.GenerativeModel(MODEL_NAME)

