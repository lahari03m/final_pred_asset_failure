import streamlit as st
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Asset Failure Dashboard", layout="wide")

st.title("📊 Asset Failure Prediction Dashboard")

# Load predictions.json
with open("predictions.json", "r") as f:
    predictions = json.load(f)

pred_df = pd.DataFrame(predictions)

# Load summary if available
try:
    with open("predictions_summary.json", "r") as f:
        summary = json.load(f)
except:
    summary = None

# 📌 Executive Summary Section
st.header("📌 Executive Summary")
if summary:
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Assets", summary.get("Total Assets Analyzed", 0))
    col2.metric("Most Problematic Asset Type", summary.get("Most Problematic Asset Type", "-"))
    col3.metric("Most Frequent Failure", summary.get("Most Frequent Failure Mode", "-"))
    col4.metric("Avg Days to Failure", summary.get("Average Predicted Days to Failure", 0))
else:
    st.warning("Summary file not found. KPIs will be based on predictions only.")

st.markdown("---")

# KPI 1️⃣: Summarization of asset failures
st.subheader("1️⃣ Summarization of Asset Failures")
failures_count = pred_df["failure_mode"].value_counts().reset_index()
failures_count.columns = ["Failure Mode", "Count"]
fig1 = px.bar(failures_count, x="Failure Mode", y="Count", title="Failure Modes Count", text="Count", color="Count", color_continuous_scale="Reds")
st.plotly_chart(fig1, use_container_width=True)

# KPI 2️⃣: Most problematic asset type
st.subheader("2️⃣ Most Problematic Asset Type")
asset_type_counts = pred_df["asset_type"].value_counts().reset_index()
asset_type_counts.columns = ["Asset Type", "Count"]
fig2 = px.sunburst(asset_type_counts, path=["Asset Type"], values="Count", title="Problematic Asset Types")
st.plotly_chart(fig2, use_container_width=True)

# KPI 3️⃣: Frequent asset usage & failure forecast
st.subheader("3️⃣ Frequent Asset Usage & Failure Forecast")
fig3 = px.violin(pred_df, y="Days_to_Failure", box=True, points="all", title="Failure Forecast Distribution")
st.plotly_chart(fig3, use_container_width=True)

# KPI 4️⃣: Most common failures in the next 30 days
st.subheader("4️⃣ Most Common Failures in Next 30 Days")
next_month_failures = pred_df[pred_df["Days_to_Failure"] <= 30]["failure_mode"].value_counts().reset_index()
next_month_failures.columns = ["Failure Mode", "Count"]
fig4 = px.treemap(next_month_failures, path=["Failure Mode"], values="Count", title="Failures Expected in Next 30 Days")
st.plotly_chart(fig4, use_container_width=True)

# KPI 5️⃣: Average predicted failure timeline per asset group
st.subheader("5️⃣ Average Predicted Failure Timeline per Asset Group")
asset_group_avg = pred_df.groupby("asset_type")["Days_to_Failure"].mean().reset_index()
asset_group_avg.columns = ["Asset Type", "Avg Days to Failure"]
fig5 = px.bar(asset_group_avg, x="Asset Type", y="Avg Days to Failure", title="Average Failure Timeline by Asset Type", text="Avg Days to Failure", color="Avg Days to Failure", color_continuous_scale="Blues")
st.plotly_chart(fig5, use_container_width=True)

# KPI 6️⃣: Highest usage frequency compared to peer assets
st.subheader("6️⃣ Highest Usage Frequency Compared to Peer Assets")
pred_df["Usage_Frequency"] = 1 / pred_df["Days_to_Failure"]
usage_freq = pred_df.groupby("asset_type")["Usage_Frequency"].mean().reset_index()
usage_freq.columns = ["Asset Type", "Avg Usage Frequency"]
fig6 = px.bar_polar(usage_freq, r="Avg Usage Frequency", theta="Asset Type", color="Avg Usage Frequency", title="Usage Frequency by Asset Type", color_continuous_scale="Viridis")
st.plotly_chart(fig6, use_container_width=True)

# 📌 Table View
st.subheader("📄 Detailed Predictions Table")
st.dataframe(pred_df, use_container_width=True)

st.success("✅ Dashboard Loaded Successfully with Enhanced Visualizations!")
