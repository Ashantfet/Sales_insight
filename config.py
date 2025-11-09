import os
from dotenv import load_dotenv

load_dotenv()

# API endpoints
SALES_API_URL = "https://sandbox.mkonnekt.net/ch-portal/api/v1/orders/recent"

# # Keys
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# # Model
# MODEL_NAME = "gpt-4o-mini"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama-3.3-70b-versatile"