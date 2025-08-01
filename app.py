import streamlit as st
import pandas as pd
import json
import plotly.express as px

st.set_page_config(page_title="Asset Failure Dashboard", layout="wide")

st.title("📊 Asset Failure Prediction Dashboard")

# Load JSON Data
with open("predictions.json", "r") as f:
    predictions = json.load(f)

pred_df = pd.DataFrame(predictions)

# KPIs Calculation
st.header("Executive Summary")
st.write(f"Total Assets Analyzed: {len(pred_df)}")
st.write(f"Average Predicted Days to Failure: {pred_df['Days_to_Failure'].mean():.2f}")

# 1. Summarization of asset failures (counts & types)
st.subheader("1️⃣ Summarization of Asset Failures")
failures_count = pred_df["failure_mode"].value_counts().reset_index()
failures_count.columns = ["Failure Mode", "Count"]
fig1 = px.bar(failures_count, x="Failure Mode", y="Count", title="Failure Modes Count", text="Count")
st.plotly_chart(fig1, use_container_width=True)

# 2. Most problematic asset ID/type
st.subheader("2️⃣ Most Problematic Asset Type")
asset_type_counts = pred_df["asset_type"].value_counts().reset_index()
asset_type_counts.columns = ["Asset Type", "Count"]
fig2 = px.pie(asset_type_counts, names="Asset Type", values="Count", title="Most Problematic Asset Types")
st.plotly_chart(fig2, use_container_width=True)

# 3. Frequent asset usage & failure forecast
st.subheader("3️⃣ Frequent Asset Usage & Failure Forecast")
fig3 = px.histogram(pred_df, x="Days_to_Failure", nbins=20, title="Failure Forecast Distribution")
st.plotly_chart(fig3, use_container_width=True)

# 4. Most common failures in the last month
st.subheader("4️⃣ Most Common Failures in Last Month")
last_month_failures = pred_df[pred_df["Days_to_Failure"] <= 30]["failure_mode"].value_counts().reset_index()
last_month_failures.columns = ["Failure Mode", "Count"]
fig4 = px.bar(last_month_failures, x="Failure Mode", y="Count", title="Failures in Next 30 Days", text="Count")
st.plotly_chart(fig4, use_container_width=True)

# 5. Average predicted failure timeline per asset group
st.subheader("5️⃣ Average Predicted Failure Timeline per Asset Group")
asset_group_avg = pred_df.groupby("asset_type")["Days_to_Failure"].mean().reset_index()
asset_group_avg.columns = ["Asset Type", "Avg Days to Failure"]
fig5 = px.bar(asset_group_avg, x="Asset Type", y="Avg Days to Failure", title="Average Failure Timeline", text="Avg Days to Failure")
st.plotly_chart(fig5, use_container_width=True)

# 6. Highest usage frequency compared to peer assets
st.subheader("6️⃣ Highest Usage Frequency Compared to Peer Assets")
pred_df["Usage_Frequency"] = 1 / pred_df["Days_to_Failure"]
usage_freq = pred_df.groupby("asset_type")["Usage_Frequency"].mean().reset_index()
usage_freq.columns = ["Asset Type", "Avg Usage Frequency"]
fig6 = px.bar(usage_freq, x="Asset Type", y="Avg Usage Frequency", title="Usage Frequency by Asset Type", text="Avg Usage Frequency")
st.plotly_chart(fig6, use_container_width=True)

st.success("✅ Dashboard loaded with all KPIs!")
