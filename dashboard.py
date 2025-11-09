import streamlit as st
from sales_api import fetch_recent_orders

data = fetch_recent_orders()
st.title("📊 Sales Insight Dashboard")
st.metric("Total Orders", len(data))
