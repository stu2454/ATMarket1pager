# streamlit_app.py
# Assistive Technology Market Snapshot - Wide Layout with Section Dividers

import streamlit as st
import pandas as pd
import altair as alt

# -----------------------------
# Page Config (wide layout)
# -----------------------------
st.set_page_config(page_title="AT Market Snapshot", layout="wide")

# -----------------------------
# Helpers: Format numbers nicely
# -----------------------------
def format_currency(value):
    try:
        value = float(str(value).replace(",", "").replace("$", ""))
    except:
        return str(value)
    if abs(value) >= 1_000_000_000:
        return f"${value/1_000_000_000:.2f}B"
    elif abs(value) >= 1_000_000:
        return f"${value/1_000_000:.2f}M"
    elif abs(value) >= 1_000:
        return f"${value/1_000:.2f}K"
    else:
        return f"${value:.2f}"

def format_number(value):
    try:
        value = int(value)
        return f"{value:,}"
    except:
        return str(value)

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
market_all_supports["Payments_num"] = clean_currency(market_all_supports["Payments"])
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
# Section divider
# -----------------------------
def divider():
    st.markdown("<hr style='border:1px solid #ccc; margin:20px 0;'>", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown(
    "<h1 style='color:#4B2E83; text-align:center;'>Assistive Technology Market Snapshot</h1>",
    unsafe_allow_html=True
)
st.caption(f"{latest_period} | Source: NDIA internal data (Capital – Assistive Technology, All Australia)")

divider()

# -----------------------------
# ROW 1: Expenditure + Participants
# -----------------------------
row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.markdown("### 💰 Expenditure")
    col1, col2, col3 = st.columns(3)
    col1.metric("AT Payments", format_currency(payments), f"{at_share_payments:.1f}% of total")
    col2.metric("AT Committed Supports", format_currency(committed), f"{at_share_committed:.1f}% of total")
    col3.metric("Utilisation", utilisation)

    spend_chart = alt.Chart(market_at_all).mark_area(opacity=0.6).encode(
        x="Period",
        y=alt.Y("Payments_num", title="AT Payments ($)"),
        tooltip=["Period", "Payments"]
    ).properties(height=200)
    st.altair_chart(spend_chart, use_container_width=True)

    st.write("**Top 10 AT Support Items by Spend (simulated)**")
    item_data = pd.DataFrame({
        "Support Item": [
            "Power wheelchairs", "Manual wheelchairs", "Communication devices (AAC)",
            "Hearing aids", "Prosthetics", "Orthotics", "Home automation / smart tech",
            "Beds & mattresses", "Hoists & transfer equipment", "Vision aids"
        ],
        "Spend": [580, 420, 360, 310, 290, 250, 200, 180, 150, 120]
    })
    item_chart = alt.Chart(item_data).mark_bar().encode(
        x="Spend", y=alt.Y("Support Item", sort="-x"), tooltip=["Support Item", "Spend"]
    ).properties(height=300)
    st.altair_chart(item_chart, use_container_width=True)

with row1_col2:
    st.markdown("### 👥 Participants")
    complex_share = 30  # simulated %
    median_spend = "$3.2K"  # simulated

    col1, col2, col3 = st.columns(3)
    col1.metric("Active AT Participants", format_number(active_participants))
    col2.metric("Complex AT Users", f"{complex_share}%", "share of AT participants")
    col3.metric("Median AT Spend", median_spend)

    comp_data = pd.DataFrame({"Type": ["Simple Users", "Complex Users"], "Share": [70, 30]})
    comp_chart = alt.Chart(comp_data).mark_arc(innerRadius=50).encode(
        theta="Share", color="Type", tooltip=["Type", "Share"]
    ).properties(title="AT User Complexity (simulated)")
    st.altair_chart(comp_chart, use_container_width=True)

    spend_data = pd.DataFrame({
        "Level": ["Low (<$1K)", "Moderate ($1K–10K)", "High (>$10K)"],
        "Participants": [50000, 30000, 10000]
    })
    spend_chart = alt.Chart(spend_data).mark_bar().encode(
        x="Participants", y=alt.Y("Level", sort=["Low (<$1K)", "Moderate ($1K–10K)", "High (>$10K)"]),
        tooltip=["Level", "Participants"]
    ).properties(title="AT Spend Intensity (simulated)", height=200)
    st.altair_chart(spend_chart, use_container_width=True)

    func_data = pd.DataFrame({
        "Domain": ["Mobility", "Communication", "Self-care", "Vision/Hearing", "Cognition", "Combined"],
        "Participants": [35000, 20000, 15000, 10000, 5000, 5300]
    })
    func_chart = alt.Chart(func_data).mark_bar().encode(
        x="Participants", y=alt.Y("Domain", sort="-x"), tooltip=["Domain", "Participants"]
    ).properties(title="Functional Domains of AT Use (simulated)", height=200)
    st.altair_chart(func_chart, use_container_width=True)

    dis_data = pd.DataFrame({
        "Disability": ["Cerebral palsy", "Autism", "MS", "Intellectual disability", "Hearing impairment", "Other"],
        "Participants": [20000, 15000, 8000, 12000, 9000, 26300]
    })
    dis_chart = alt.Chart(dis_data).mark_circle(size=100).encode(
        x="Participants", y=alt.Y("Disability", sort="-x"), tooltip=["Disability", "Participants"]
    ) + alt.Chart(dis_data).mark_rule().encode(
        x="Participants", y=alt.Y("Disability", sort="-x")
    )
    st.altair_chart(dis_chart.properties(title="AT Participants by Primary Disability (simulated)"),
                    use_container_width=True)

divider()

# -----------------------------
# ROW 2: Market Dynamics + Providers
# -----------------------------
row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    st.markdown("### 📈 Market Dynamics")
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Median Delivery Time", "44 days", "-2 vs last year")
    k2.metric("% Repairs <14 Days", "72%", "+5pp")
    k3.metric("Provider Churn", "4%", "this quarter")
    k4.metric("Innovation Uptake", "3.5%", "↑ trend")

    uptake_data = pd.DataFrame({"Quarter": ["Q1", "Q2", "Q3", "Q4"], "Uptake": [2.1, 2.9, 3.2, 3.5]})
    uptake_chart = alt.Chart(uptake_data).mark_line(point=True).encode(
        x="Quarter", y=alt.Y("Uptake", title="% of AT Spend"), tooltip=["Quarter", "Uptake"]
    ).properties(title="Innovation Uptake Trend", height=200)
    st.altair_chart(uptake_chart, use_container_width=True)

    regional_times = pd.DataFrame({"Region": ["Metro", "Regional", "Remote"], "Days": [38, 46, 54]})
    reg_chart2 = alt.Chart(regional_times).mark_bar().encode(
        x="Days", y="Region", tooltip=["Region", "Days"]
    ).properties(title="Average Delivery Times by Region (days)", height=200)
    st.altair_chart(reg_chart2, use_container_width=True)

    top5_data = pd.DataFrame({"Group": ["Top 5 Providers", "All Others"], "Share": [45, 55]})
    top5_chart = alt.Chart(top5_data).mark_arc(innerRadius=50).encode(
        theta="Share", color="Group", tooltip=["Group", "Share"]
    ).properties(title="Market Concentration: Top 5 Providers")
    st.altair_chart(top5_chart, use_container_width=True)

with row2_col2:
    st.markdown("### 🏢 Providers")
    col1, col2, col3 = st.columns(3)
    col1.metric("Active AT Providers", format_number(active_providers))
    col2.metric("Participants per Provider", format_number(ppp))
    col3.metric("Top 5 Provider Share", "45% (simulated)")

    reach_data = pd.DataFrame({
        "Range": ["<10", "10-50", "51-100", "101-500", "500+"],
        "Providers": [400, 250, 150, 80, 20]
    })
    reach_chart = alt.Chart(reach_data).mark_bar().encode(
        x="Providers", y=alt.Y("Range", sort=["<10", "10-50", "51-100", "101-500", "500+"]),
        tooltip=["Range", "Providers"]
    ).properties(title="Provider Reach Distribution", height=300)
    st.altair_chart(reach_chart, use_container_width=True)

    scope_data = pd.DataFrame({"Type": ["Multi-line Providers", "Niche Providers"], "Share": [40, 60]})
    scope_chart = alt.Chart(scope_data).mark_arc(innerRadius=50).encode(
        theta="Share", color="Type", tooltip=["Type", "Share"]
    ).properties(title="Scope of Supply (simulated)")
    st.altair_chart(scope_chart, use_container_width=True)

    regional_data = pd.DataFrame({"Region": ["Metro", "Regional", "Remote"], "Providers": [70, 25, 5]})
    reg_chart = alt.Chart(regional_data).mark_bar().encode(
        x="Providers", y="Region", color="Region", tooltip=["Region", "Providers"]
    ).properties(title="Regional Coverage (simulated)", height=200)
    st.altair_chart(reg_chart, use_container_width=True)

divider()

# -----------------------------
# ROW 3: Key Statistics Snapshot
# -----------------------------
with st.container():
    st.markdown("### 📊 Key Statistics Snapshot")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total AT Spend", format_currency(payments))
    col2.metric("Participants with AT", format_number(active_participants))
    col3.metric("Active Providers", format_number(active_providers))
    col1.metric("Utilisation", utilisation)
    col2.metric("Avg Committed Support", format_currency(avg_committed))
    col3.metric("Innovation Uptake", "3.5% (simulated)")
