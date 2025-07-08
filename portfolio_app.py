# portfolio_app.py

import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------------------
# App title and inputs
# ------------------------------
st.title("📊 Portfolio Manager Dashboard")
st.markdown("Simulated PMS-like interface for tracking your investments")

client_name = st.text_input("Enter your name:")
capital = st.number_input("Enter total capital (₹):", min_value=100000, step=10000)

risk_profile = st.selectbox("Choose your risk profile:", ["Conservative", "Balanced", "Aggressive"])

# ------------------------------
# Suggested Allocation based on risk
# ------------------------------
st.subheader("📌 Suggested Asset Allocation")

def suggest_allocation(risk):
    if risk == "Conservative":
        return {"Equity": 20, "Debt": 60, "Gold": 10, "Cash": 10}
    elif risk == "Balanced":
        return {"Equity": 50, "Debt": 30, "Gold": 10, "Cash": 10}
    else:
        return {"Equity": 70, "Debt": 15, "Gold": 10, "Cash": 5}

allocation = suggest_allocation(risk_profile)
alloc_df = pd.DataFrame(allocation.items(), columns=["Asset Class", "Allocation (%)"])
alloc_df["Amount (₹)"] = alloc_df["Allocation (%)"] * capital / 100

# Pie chart visualization
fig = px.pie(alloc_df, values="Amount (₹)", names="Asset Class", title="Asset Allocation")
st.plotly_chart(fig)
st.dataframe(alloc_df)

# ------------------------------
# Simulated Returns
# ------------------------------
st.subheader("📈 Portfolio Performance Simulation")

returns_map = {
    "Equity": 0.12,
    "Debt": 0.06,
    "Gold": 0.08,
    "Cash": 0.03
}

alloc_df["Expected Return (%)"] = alloc_df["Asset Class"].map(returns_map)
alloc_df["Expected Annual Return (₹)"] = alloc_df["Amount (₹)"] * alloc_df["Expected Return (%)"]

st.dataframe(alloc_df[["Asset Class", "Amount (₹)", "Expected Annual Return (₹)"]])
st.metric("💹 Total Expected Return", f"₹{alloc_df['Expected Annual Return (₹)'].sum():,.2f}")
