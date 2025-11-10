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

    Args:
        query (str): Natural language query (e.g. 'What were our best-selling items yesterday?')
        data (list, optional): Sales data. If not provided, fetches automatically.

    Returns:
        str: LLM-generated analysis
    """

    if not query:
        raise ValueError("Query cannot be empty.")

    # ✅ If data is not provided, fetch it automatically
    if data is None:
        data = fetch_sales_data()

    # Prepare the data sample for the LLM (limit for context length)
    sample_data = data[:10]  # You can adjust for efficiency
    context = json.dumps(sample_data, indent=2)

    # LLM prompt
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
            model="llama-3.3-70b-versatile",  # You can replace with another model if needed
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )

        return completion.choices[0].message.content.strip()

    except Exception as e:
        raise Exception(f"LLM processing error: {str(e)}")
