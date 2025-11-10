import streamlit as st
from llm_agent import analyze_sales_with_llm
from sales_api import fetch_sales_data  # ✅ Make sure this exists

st.set_page_config(page_title="Sales Insight Agent", page_icon="📊")

st.title("📊 Sales Insight Agent")
st.markdown("Ask natural language questions about your sales data.")

query = st.text_input("💬 Ask your question:", placeholder="e.g. What were our best-selling items yesterday?")

if st.button("Analyze") or query:
    with st.spinner("Analyzing... please wait"):
        try:
            # ✅ Step 1: Fetch latest data from the API
            data = fetch_sales_data()
            
            # ✅ Step 2: Pass both query and data
            answer = analyze_sales_with_llm(query, data)
            
            st.success("✅ Analysis Complete")
            st.markdown(f"### 🤖 Response:\n{answer}")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
