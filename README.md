

## 🧠 Sales Insight Agent

An **AI-powered sales analysis assistant** that answers natural language questions about sales data using the **Sales API** and **Groq LLM**.

---

### 🚀 Features

* Natural-language Q&A on sales (e.g. *“What were our best-selling items yesterday?”*)
* Fetches real-time data via `Sales API`
* Uses **Groq LLM** (`llama-3.3-70b-versatile`) for reasoning
* Smart relative date parsing (`yesterday`, `last week`, etc.)
* Local caching to avoid redundant API calls
* CLI interface built with **Typer**
* Cache management command (`clear-cache`)

---

### ⚙️ Setup

#### 1️⃣ Clone and install

```bash
git clone <your_repo_url>
cd sales_insight_agent
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### 2️⃣ Environment file

Create `.env` in the project root:

```
GROQ_API_KEY=your_groq_api_key_here
```

#### 3️⃣ Install dependencies

```bash
pip install groq requests typer python-dotenv diskcache
```

---

### 🧩 File Structure

```
sales_insight_agent/
│
├── main.py             # CLI entry point
├── sales_api.py        # Fetch + cache API data
├── llm_agent.py        # Query Groq model
├── nlp_utils.py        # Parse relative dates
├── config.py           # Env + constants
├── .env.example
├── README.md
└── cache_dir/          # Local cache storage
```

---

### 💻 Usage

#### Ask a question

```bash
python main.py ask -- "What were our best-selling items yesterday?"
python main.py ask -- "How much revenue did we make today?"
python main.py ask -- "Show me the sales trend for last week"
python main.py ask -- "What’s the average order value this month?"
```

#### Clear cache

```bash
python main.py clear-cache
```

---

### 🧠 Example Output

```
🧠 Question: What were our best-selling items yesterday?
📅 Date range: 2025-11-08 → 2025-11-08
💬 Answer:
1. “Hd Honey” - 3 sold ($129 each)
2. “Sonoma Green 100 Box” - 2 sold ($616 each)
3. “Good Time Woods” - 2 sold ($139 each)
```

---

### 🧹 Bonus Features Implemented

* ✅ Caching with per-day auto-expiry
* ✅ Date parsing
* ✅ Error handling
* ✅ CLI usability
* ✅ Secure `.env` key management

---

### 🧩 Reflection

**Most challenging aspect:** Handling dynamic data volume and preventing LLM context overflow.
**Improvement:** Add web dashboard (Streamlit) for visualization.
**Interesting decision:** Used Groq’s `llama-3.3-70b-versatile` for cost-efficient, fast reasoning.

---


# Sales_insight
