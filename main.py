import typer
from sales_api import fetch_recent_orders, cache as sales_cache
from llm_agent import analyze_sales_with_llm
from nlp_utils import parse_date_range

app = typer.Typer()

@app.command()
def ask(question: str):
    """Ask a natural language sales question."""
    print(f"🧠 Question: {question}")
    
    start, end = parse_date_range(question)
    print(f"📅 Date range: {start} → {end}")

    data = fetch_recent_orders()
    if not data:
        print("⚠️ No data available.")
        return

    answer = analyze_sales_with_llm(question, data)
    print("\n💬 Answer:\n", answer)


@app.command()
def clear_cache():
    """Clear cached API responses."""
    try:
        sales_cache.clear()
        print("🧹 Cache cleared successfully!")
    except Exception as e:
        print(f"⚠️ Failed to clear cache: {e}")


if __name__ == "__main__":
    app()
