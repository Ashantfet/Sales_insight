# from openai import OpenAI
# from config import OPENAI_API_KEY, MODEL_NAME

# client = OpenAI(api_key=OPENAI_API_KEY)

# def analyze_sales_with_llm(question: str, data: list) -> str:
#     """Send sales data + question to LLM and return summarized response."""
#     prompt = (
#         "You are a sales analysis assistant.\n"
#         "Given this sales data (JSON) and the user's question, analyze and summarize clearly.\n\n"
#         f"Sales Data:\n{data}\n\n"
#         f"Question: {question}\n\n"
#         "Answer concisely and in plain English."
#     )

#     response = client.chat.completions.create(
#         model=MODEL_NAME,
#         messages=[{"role": "user", "content": prompt}],
#         max_tokens=300,
#         temperature=0.2,
#     )

#     return response.choices[0].message.content.strip()
# import json
# from groq import Groq
# from config import GROQ_API_KEY, MODEL_NAME

# client = Groq(api_key=GROQ_API_KEY)

# def analyze_sales_with_llm(question: str, data: list) -> str:
#     """Send summarized sales data + question to Groq LLM."""
#     # Trim: only include first few orders to avoid context overflow
#     if isinstance(data, dict) and "orders" in data:
#         data_summary = data["orders"][:20]  # limit to 20 orders
#     else:
#         data_summary = data[:20]

#     compact_data = json.dumps(data_summary, indent=2)[:8000]  # cap tokens

#     prompt = (
#         "You are a sales analysis assistant.\n"
#         "Analyze the following summarized sales data and answer the user's question.\n\n"
#         f"Sales Data:\n{compact_data}\n\n"
#         f"Question: {question}\n\n"
#         "Give a clear, short, human-readable answer."
#     )

#     response = client.chat.completions.create(
#         model=MODEL_NAME,
#         messages=[{"role": "user", "content": prompt}],
#         max_tokens=300,
#         temperature=0.2,
#     )

#     return response.choices[0].message.content.strip()
import os
from dotenv import load_dotenv
from groq import Groq
import json
import requests

# Load environment variables
load_dotenv()

# Initialize Groq client
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY not found. Please add it to your .env file.")

client = Groq(api_key=GROQ_API_KEY)

# Default API endpoint
API_URL = os.getenv("API_URL", "https://sandbox.mkonnekt.net/ch-portal/api/v1/orders/recent")


def fetch_sales_data():
    """Fetch sales data from API."""
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise Exception(f"Error fetching sales data: {str(e)}")


def analyze_sales_with_llm(query: str, data=None):
    """
    Analyze sales data using LLM.
    Automatically handles both list and dict-based inputs.
    """

    if not query:
        raise ValueError("Query cannot be empty.")

    # ✅ Step 1: Handle missing data
    if data is None:
        data = fetch_sales_data()

    # ✅ Step 2: Handle dict-style API responses
    # Some responses wrap data inside {"orders": [...]}
    if isinstance(data, dict):
        if "orders" in data:
            orders = data["orders"]
        else:
            raise KeyError("Expected 'orders' key in the API response.")
    elif isinstance(data, list):
        orders = data
    else:
        raise TypeError(f"Unsupported data type: {type(data)}")

    # ✅ Step 3: Limit data for context length
    sample_data = orders[:10]
    context = json.dumps(sample_data, indent=2)

    # ✅ Step 4: Prepare the LLM prompt
    prompt = f"""
    You are a Sales Analysis Assistant.
    The user will ask questions about sales data (items, revenue, trends, etc.).
    Use the following JSON data to answer accurately and concisely.

    Sales Data (partial sample):
    {context}

    Question: {query}

    Answer in clear natural language with structured results if applicable.
    """

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )

        return completion.choices[0].message.content.strip()

    except Exception as e:
        raise Exception(f"LLM processing error: {str(e)}")
