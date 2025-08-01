# 📊 Asset Failure Prediction Dashboard

This project predicts asset failures using machine learning and a free LLM for problem/solution suggestions. It also provides an interactive Streamlit dashboard for visualizing key KPIs.

---

## 📂 Project Structure
```
📦 asset_failure_dashboard/
 ┣ 📜 app.py                      # Streamlit dashboard code
 ┣ 📜 asset_failure_prediction.ipynb  # Colab notebook for generating predictions
 ┣ 📜 summarize_predictions.ipynb     # Script to create summary JSON
 ┣ 📜 requirements.txt            # List of dependencies
 ┣ 📜 predictions.json            # Example output JSON
 ┣ 📜 README.md                   # Project description & instructions
```

---

## 🚀 How to Use

### 1️⃣ Generate Predictions
- Open **asset_failure_prediction.ipynb** in Google Colab.
- Upload your work order CSV file.
- Run all cells to generate **predictions.json**.

### 2️⃣ Summarize Predictions
- Open **summarize_predictions.ipynb**.
- It reads `predictions.json` and creates `predictions_summary.json`.

### 3️⃣ Run the Dashboard
#### 🔹 Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

#### 🔹 On Streamlit Cloud
1. Push the repo to GitHub.
2. Go to [https://share.streamlit.io/](https://share.streamlit.io/).
3. Deploy app → Select your repo → Choose **app.py**.

---

## 📊 KPIs in Dashboard
✅ Summarization of asset failures (counts & types)  
✅ Most problematic asset ID/type  
✅ Frequent asset usage & failure forecast  
✅ Most common failures in the last month  
✅ Average predicted failure timeline per asset group  
✅ Highest usage frequency compared to peer assets  

---

## 📌 Example Workflow
1. Upload raw asset CSV → `asset_failure_prediction.ipynb` → get `predictions.json`
2. Run dashboard (`app.py`) → Visualize KPIs
3. Optionally, run `summarize_predictions.ipynb` → Get summarized JSON file

---

👨‍💻 **Developed using:** Python, Pandas, Scikit-learn, Transformers, Plotly, and Streamlit.
