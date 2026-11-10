import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Cafe Sales Analysis Dashboard", page_icon="☕")
st.title("☕ Coffee Sales Analysis") 

@st.cache_data
def load_data():
    df = pd.read_csv("cafe_sales.csv")
    return df

cafe_sales = load_data()

# Branch selector
branches = ["All branches"] + sorted(cafe_sales["branch"].unique())
selected_branch = st.selectbox("Choose a branch:", branches)

if selected_branch == "All branches":
  filtered = cafe_sales
else:
  filtered = cafe_sales[cafe_sales["branch"] == selected_branch]

# Total revenue metric
total_revenue = filtered["total_sar"].sum()
st.metric("Total Revenue (SAR)", f"{total_revenue:,}")

# Bar chart of revenue by product
st.subheader("Revenue by Product")
revenue_by_product = filtered.groupby("product")["total_sar"].sum().sort_values(ascending=False)
st.bar_chart(revenue_by_product)
