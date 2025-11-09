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
import json
from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME

client = Groq(api_key=GROQ_API_KEY)

def analyze_sales_with_llm(question: str, data: list) -> str:
    """Send summarized sales data + question to Groq LLM."""
    # Trim: only include first few orders to avoid context overflow
    if isinstance(data, dict) and "orders" in data:
        data_summary = data["orders"][:20]  # limit to 20 orders
    else:
        data_summary = data[:20]

    compact_data = json.dumps(data_summary, indent=2)[:8000]  # cap tokens

    prompt = (
        "You are a sales analysis assistant.\n"
        "Analyze the following summarized sales data and answer the user's question.\n\n"
        f"Sales Data:\n{compact_data}\n\n"
        f"Question: {question}\n\n"
        "Give a clear, short, human-readable answer."
    )

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
        temperature=0.2,
    )

    return response.choices[0].message.content.strip()
