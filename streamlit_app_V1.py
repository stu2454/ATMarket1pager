# streamlit_app.py
# AT Market Snapshot - Glossy Style (AT-only, All Australia data from ./data/Explore_Data_2025_09_18.xlsx)

import streamlit as st
import pandas as pd
import altair as alt

# -----------------------------
# Load data
# -----------------------------
DATA_PATH = "data/Explore_Data_2025_09_18.xlsx"

market_total = pd.read_excel(DATA_PATH, sheet_name="Market by Total")
participants_total = pd.read_excel(DATA_PATH, sheet_name="ActPrtpnt by Total")
providers_total = pd.read_excel(DATA_PATH, sheet_name="Provider by Total")

# -----------------------------
# Normalise column names
# -----------------------------
for df in [market_total, participants_total, providers_total]:
    df.columns = df.columns.str.strip()
    df["Support Category"] = df["Support Category"].astype(str).str.strip()
    df["State/Territory"] = df["State/Territory"].astype(str).str.strip()

# -----------------------------
# Filter: AT only + All Australia
# -----------------------------
market_at_all = market_total[
    (market_total["Support Category"] == "Capital - Assistive Technology") &
    (market_total["State/Territory"] == "All Australia")
].copy()

participants_at_all = participants_total[
    (participants_total["Support Category"] == "Capital - Assistive Technology") &
    (participants_total["State/Territory"] == "All Australia")
].copy()

providers_at_all = providers_total[
    (providers_total["Support Category"] == "Capital - Assistive Technology") &
    (providers_total["State/Territory"] == "All Australia")
].copy()

# Also get ALL supports for comparison
market_all_supports = market_total[
    (market_total["Support Category"] == "All") &
    (market_total["State/Territory"] == "All Australia")
].copy()

# -----------------------------
# Latest period
# -----------------------------
latest_period = market_at_all["Period"].unique().max()

market_at = market_at_all[market_at_all["Period"] == latest_period]
participants_at = participants_at_all[participants_at_all["Period"] == latest_period]
providers_at = providers_at_all[providers_at_all["Period"] == latest_period]
market_all_supports_latest = market_all_supports[market_all_supports["Period"] == latest_period]

# -----------------------------
# Extract latest values
# -----------------------------
payments = market_at["Payments"].iloc[0]
committed = market_at["Committed supports"].iloc[0]
utilisation = f"{market_at['Utilisation'].iloc[0]}%"

active_participants = participants_at["Active participants"].iloc[0]
avg_committed = participants_at["Average committed support"].iloc[0]
avg_payments = participants_at["Average payments"].iloc[0]

active_providers = providers_at["Active provider"].iloc[0]

# -----------------------------
# Clean numeric fields for charts
# -----------------------------
def clean_currency(series):
    return series.replace('[\$,]', '', regex=True).astype(float)

market_at_all["Payments_num"] = clean_currency(market_at_all["Payments"])
market_at_all["Committed_num"] = clean_currency(market_at_all["Committed supports"])
market_all_supports["Payments_num"] = clean_currency(market_all_supports["Payments"])
market_all_supports["Committed_num"] = clean_currency(market_all_supports["Committed supports"])
participants_at_all["Active_num"] = participants_at_all["Active participants"].astype(float)
providers_at_all["Providers_num"] = providers_at_all["Active provider"].astype(float)

# % share of total
at_share_payments = (
    clean_currency(market_at["Payments"]).iloc[0] /
    clean_currency(market_all_supports_latest["Payments"]).iloc[0] * 100
)
at_share_committed = (
    clean_currency(market_at["Committed supports"]).iloc[0] /
    clean_currency(market_all_supports_latest["Committed supports"]).iloc[0] * 100
)

# Derived participants per provider
ppp = round(active_participants / active_providers, 1) if active_providers > 0 else 0

# -----------------------------
# HEADER
# -----------------------------
st.markdown(
    "<h1 style='color:#4B2E83;'>Assistive Technology Market Snapshot</h1>",
    unsafe_allow_html=True
)
st.caption(f"{latest_period} | Source: NDIA internal data (Capital – Assistive Technology, All Australia)")

# -----------------------------
# TOTAL EXPENDITURE
# -----------------------------
with st.container():
    st.markdown("### 💰 Total Expenditure")
    col1, col2, col3 = st.columns(3)
    col1.metric("AT Payments", payments, f"{at_share_payments:.1f}% of total")
    col2.metric("AT Committed Supports", committed, f"{at_share_committed:.1f}% of total")
    col3.metric("Utilisation", utilisation)

    spend_chart = alt.Chart(market_at_all).mark_line(point=True).encode(
        x="Period",
        y=alt.Y("Payments_num", title="AT Payments ($)"),
        tooltip=["Period", "Payments"]
    ).properties(height=200)
    st.altair_chart(spend_chart, use_container_width=True)

    # Simulated breakdown charts
    st.write("#### Where is AT spend happening?")
    placeholder1, placeholder2 = st.columns(2)

    with placeholder1:
        st.write("**Top 10 AT Support Items by Spend (simulated)**")
        item_data = pd.DataFrame({
            "Support Item": [
                "Power wheelchairs", "Manual wheelchairs", "Communication devices (AAC)",
                "Hearing aids", "Prosthetics", "Orthotics", "Home automation / smart tech",
                "Beds & mattresses", "Hoists & transfer equipment", "Vision aids"
            ],
            "Spend": [580, 420, 360, 310, 290, 250, 200, 180, 150, 120]  # $M simulated
        })
        item_chart = alt.Chart(item_data).mark_bar().encode(
            x=alt.X("Spend", title="Spend ($M)"),
            y=alt.Y("Support Item", sort="-x"),
            tooltip=["Support Item", "Spend"]
        ).properties(height=300)
        st.altair_chart(item_chart, use_container_width=True)

    with placeholder2:
        st.write("**AT Spend by Disability Group (simulated)**")
        disability_data = pd.DataFrame({
            "Disability": [
                "Cerebral palsy", "Autism", "Intellectual disability", "Hearing impairment",
                "Vision impairment", "Multiple sclerosis", "Spinal cord injury",
                "Stroke", "Motor neurone disease", "Other"
            ],
            "Spend": [800, 650, 600, 500, 400, 300, 250, 200, 150, 180]  # $M simulated
        })
        dis_chart = alt.Chart(disability_data).mark_bar().encode(
            x=alt.X("Spend", title="Spend ($M)"),
            y=alt.Y("Disability", sort="-x"),
            tooltip=["Disability", "Spend"]
        ).properties(height=300)
        st.altair_chart(dis_chart, use_container_width=True)

# -----------------------------
# PARTICIPANTS
# -----------------------------
with st.container():
    st.markdown("### 👥 Participants")
    col1, col2, col3 = st.columns(3)
    col1.metric("Active Participants", active_participants)
    col2.metric("Avg Committed Support", avg_committed)
    col3.metric("Avg Payments", avg_payments)

    participant_chart = alt.Chart(participants_at_all).mark_line(point=True).encode(
        x="Period",
        y=alt.Y("Active_num", title="Active Participants"),
        tooltip=["Period", "Active participants"]
    ).properties(height=200)
    st.altair_chart(participant_chart, use_container_width=True)

# -----------------------------
# PROVIDERS
# -----------------------------
with st.container():
    st.markdown("### 🏢 Providers")
    col1, col2 = st.columns(2)
    col1.metric("Active AT Providers", active_providers)
    col2.metric("Participants per Provider", ppp)

    provider_chart = alt.Chart(providers_at_all).mark_line(point=True).encode(
        x="Period",
        y=alt.Y("Providers_num", title="Active Providers"),
        tooltip=["Period", "Active provider"]
    ).properties(height=200)
    st.altair_chart(provider_chart, use_container_width=True)

# -----------------------------
# MARKET DYNAMICS (placeholder KPIs for now)
# -----------------------------
with st.container():
    st.markdown("### 📈 Market Dynamics")
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("Median Delivery Time", "44 days", "+4 vs last year")
    kpi2.metric("Repair Turnaround", "8 days", "-2 vs last year")
    kpi3.metric("Budget Utilisation", utilisation, "+3pp vs last year")

# -----------------------------
# KEY STATISTICS (SNAPSHOT BOX)
# -----------------------------
with st.container():
    st.markdown("### 📊 Key Statistics Snapshot")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total AT Spend", payments)
    col2.metric("Participants with AT", active_participants)
    col3.metric("Active Providers", active_providers)
    col1.metric("Utilisation", utilisation)
    col2.metric("Avg Committed Support", avg_committed)
    col3.metric("Innovation Uptake", "3.5% (simulated)")
