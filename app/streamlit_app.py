import pandas as pd
import numpy as np
import plotly.express as px
from pathlib import Path
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

from src.features import compute_rfm

DATA = Path(__file__).resolve().parents[1] / "data"

try:
    import streamlit as st
except Exception as e:
    print("Streamlit is required to run the app: pip install streamlit")
    raise e

st.set_page_config(page_title="Marketing Analytics", layout="wide")
st.title("📊 Marketing Analytics: Segments, CLV & Uplift (Demo)")
st.write("Synthetic demo data. Replace with your own CSVs in `data/raw/` and re-run.")

tx = pd.read_csv(DATA / "raw" / "transactions.csv", parse_dates=["tx_date"])
rfm = compute_rfm(tx, snapshot_date=tx["tx_date"].max() + pd.Timedelta(days=1))

k = st.sidebar.slider("Number of clusters (KMeans on RFM)", 3, 8, 4)
X = rfm[["recency","frequency","monetary"]].replace([np.inf,-np.inf], np.nan).fillna(0.0)
scaler = StandardScaler()
Xs = scaler.fit_transform(X)
km = KMeans(n_clusters=k, n_init=10, random_state=42).fit(Xs)
rfm["segment"] = km.labels_

col1, col2 = st.columns(2)
with col1:
    fig1 = px.scatter_3d(rfm, x="recency", y="frequency", z="monetary", color="segment", title="RFM Segments (3D)")
    st.plotly_chart(fig1, use_container_width=True)
with col2:
    seg_stats = rfm.groupby("segment").agg(
        customers=("customer_id","count"),
        avg_recency=("recency","mean"),
        avg_frequency=("frequency","mean"),
        avg_monetary=("monetary","mean"),
    ).reset_index()
    st.dataframe(seg_stats)

st.subheader("Recent Campaign Readout (synthetic)")
camp = pd.read_csv(DATA / "raw" / "campaign_outcomes.csv")
st.write("Treatment vs Control conversion and revenue.")
agg = camp.groupby("treatment").agg(conv=("converted","mean"), avg_rev=("revenue","mean"), n=("converted","count")).reset_index()
st.dataframe(agg)