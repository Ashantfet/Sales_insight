# 🧠 Sales Insight Agent

An intelligent **Sales Analysis Assistant** powered by **Groq LLM**, designed to answer natural-language questions about sales data using the **MKonnect Sales API**.

Supports both a **command-line interface (CLI)** and an **interactive web dashboard** built with Streamlit.

---

## 🚀 Overview

The Sales Insight Agent allows users to ask questions like:

> 💬 “What were our best-selling items yesterday?”
> 💬 “Show me the sales trend for last week.”
> 💬 “What was our total revenue today?”
> 💬 “What’s the average order value this month?”

The agent automatically fetches live sales data, interprets the query using an LLM, and provides accurate, structured insights.

---

## 🧩 Features

✅ **Dual Interface** – Use via CLI or Streamlit web dashboard
✅ **Natural Language Understanding** – Powered by Groq’s `llama-3.3-70b-versatile` model
✅ **Automatic API Integration** – Fetches live order data from MKonnekt’s sandbox endpoint
✅ **Smart Caching** – Saves API results locally to reduce redundant calls
✅ **Error Handling** – Handles invalid responses, missing keys, and connection issues
✅ **Date Range Parsing** – Interprets relative time expressions like “yesterday” or “last week”
✅ **Configurable Models** – Easily switch between Groq and OpenAI (optional)

---

## 🧰 Tech Stack

| Component          | Technology                |
| ------------------ | ------------------------- |
| **Language**       | Python 3.10+              |
| **LLM Engine**     | Groq (`llama-3.3-70b-versatile`)     |
| **Frontend**       | Streamlit                 |
| **Backend API**    | MKonnekt Sales API        |
| **Env Management** | python-dotenv             |
| **Data Fetching**  | requests                  |
| **CLI Tools**      | argparse, rich (optional) |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Ashantfet/Sales_insight.git
cd Sales_insight
```

### 2️⃣ Create and Activate Virtual Environment

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Create Environment File

Create a file named `.env` in your project root:

```bash
GROQ_API_KEY=gsk_your_groq_key_here
API_URL=https://sandbox.mkonnekt.net/ch-portal/api/v1/orders/recent
MODEL=llama-3.3-70b-versatile
```

(Optional for fallback)

```bash
OPENAI_API_KEY=sk_your_openai_key_here
```

---

## 💻 Usage

### 🧠 **Command-Line Interface (CLI)**

#### Ask a Sales Question

```bash
python3 main.py ask -- "What were our best-selling items yesterday?"
```

Example Output:

```
🧠 Question: What were our best-selling items yesterday?
📅 Date range: 2025-11-09 → 2025-11-09
🌐 Fetched new data from API and cached it

💬 Answer:
1. Coffee Large 20 — $630
2. Marlboro Box Red — $1,798
3. Custom Item — $318
```

#### Clear Cached Data

```bash
python3 main.py clear-cache
```

Output:

```
🧹 Cache cleared successfully!
```

---

### 🌐 **Run as a Web App**

Start the Streamlit server:

```bash
streamlit run web_app.py
```

Then open your browser at:
👉 [http://localhost:8501](http://localhost:8501)

You’ll see:

* A text box for entering sales questions
* An “Analyze” button
* LLM-generated responses displayed interactively

---

## 📁 Project Structure

```
sales_insight_agent/
├── main.py             # CLI interface (ask / clear-cache)
├── llm_agent.py        # LLM logic (Groq integration, auto data fetch)
├── sales_api.py        # API integration and caching
├── web_app.py          # Streamlit web interface
├── requirements.txt
├── .env
└── README.md
```

---

## 🧪 Example Queries

| Query                                         | Example Response                     |
| --------------------------------------------- | ------------------------------------ |
| “What were our best-selling items yesterday?” | Lists top-selling items with revenue |
| “Show me the sales trend for last week”       | Returns daily revenue trend summary  |
| “What’s the total revenue today?”             | Displays current day’s total revenue |
| “What’s the average order value this month?”  | Returns AOV in USD                   |

---

## 🧱 Design Highlights

* Modular design: all logic separated into API, LLM, and UI layers
* Groq LLM chosen for performance and low latency
* Caching added to minimize redundant API calls
* Works even when `data` format varies (list or wrapped dict)
* CLI & web versions share the same backend logic

---

## 🧩 Potential Improvements

* [ ] Add OpenAI fallback when Groq API fails
* [ ] Implement visual charts (matplotlib or plotly) in Streamlit
* [ ] Add historical aggregation & daily summaries
* [ ] Enhance caching using `diskcache`

---

## 🧾 Reflection

> **Most challenging aspect:** Ensuring correct handling of variable API structures and LLM context management.
> **Improvement focus:** Add visual analytics (charts) and long-term caching.
> **Interesting choice:** Built dual-interface architecture (CLI + Streamlit) using the same core LLM logic for flexibility.

---

## 📧 Contact

**Author:** Ashant Kumar
📩 Email: [[cs24m113@iittp.ac.in](mailto:cs24m113@iittp.ac.in)]
🔗 GitHub: [Ashantfet](https://github.com/Ashantfet)

---
