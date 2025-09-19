# Assistive Technology Market Snapshot Dashboard

This Streamlit dashboard provides a **1-page executive snapshot** of the **Assistive Technology (AT) market** under the NDIS.  
It combines **real internal NDIA data** with **simulated placeholders** for metrics not yet captured, helping policy teams conceptualise how a comprehensive market monitoring tool could look.

---

## 📂 Data Sources

The dashboard is driven by an Excel file:  
`data/Explore_Data_2025_09_18.xlsx`

It uses the following sheets:

- **Market by Total** → AT expenditure (payments, committed supports, utilisation).
- **ActPrtpnt by Total** → participant numbers and averages.
- **Provider by Total** → provider counts and activity.

All filtering is restricted to:
- **Support Category = "Capital - Assistive Technology"**
- **State/Territory = "All Australia"**

---

## 📊 Sections

### 1. 💰 Expenditure
**KPIs**
- AT Payments → `Market by Total` → `Payments`
- AT Committed Supports → `Market by Total` → `Committed supports`
- Utilisation → `Market by Total` → `Utilisation`

**Plots**
- **Trend of AT Payments** → `Market by Total` → time series of `Payments`
- **Top 10 AT Support Items by Spend** → **Simulated data** (wheelchairs, AAC devices, hearing aids, etc.)

📌 *To populate this properly, NDIA would need access to claim-level data by **support item code**.*

---

### 2. 👥 Participants
**KPIs**
- Active AT Participants → `ActPrtpnt by Total` → `Active participants`
- Complex AT Users → **Simulated (30%)**
- Median AT Spend → **Simulated ($3.2K)**

**Plots**
- **Complexity (Donut)** → **Simulated (Simple vs Complex users)**
- **Spend Intensity (Bar)** → **Simulated** (Low < $1K, Moderate $1K–10K, High > $10K)
- **Functional Domains (Bar)** → **Simulated** (Mobility, Communication, Vision/Hearing, etc.)
- **Primary Disability (Lollipop)** → **Simulated** (Cerebral palsy, Autism, MS, etc.)

📌 *To replace simulated data, NDIA would need:*
- Breakdown of AT supports by **participant complexity tiers** (simple vs multi-device).
- AT spend distribution across **functional impairment domains**.
- AT use by **primary disability type**.

---

### 3. 📈 Market Dynamics
**KPIs**
- Median Delivery Time → **Simulated (44 days)**
- % Repairs <14 Days → **Simulated (72%)**
- Provider Churn → **Simulated (4% this quarter)**
- Innovation Uptake → **Simulated (3.5% of AT spend)**

**Plots**
- **Innovation Uptake Trend (Line)** → **Simulated (% spend using flexible/subscription codes)**
- **Regional Delivery Times (Bar)** → **Simulated (Metro = 38 days, Regional = 46, Remote = 54)**
- **Market Concentration (Donut)** → **Simulated (Top 5 providers = 45% of payments)**

📌 *To replace simulated data, NDIA would need:*
- Data from provider claims linked to **delivery and repair turnaround times**.
- **Churn analysis** of registered AT providers (entries/exits per quarter).
- Claims tagged to **flexible/subscription codes**.
- Market concentration analysis based on **provider-level payments**.

---

### 4. 🏢 Providers
**KPIs**
- Active AT Providers → `Provider by Total` → `Active provider`
- Participants per Provider → **Derived** (`participants ÷ providers`)
- Top 5 Provider Share → **Simulated (45%)**

**Plots**
- **Provider Reach Distribution (Histogram)** → **Simulated (# participants served ranges)**
- **Scope of Supply (Donut)** → **Simulated (Multi-line vs Niche providers)**
- **Regional Coverage (Bar)** → **Simulated (Metro 70%, Regional 25%, Remote 5%)**

📌 *To replace simulated data, NDIA would need:*
- Participant-to-provider matching (claims data by provider).
- Provider registration information by **registration groups / support items**.
- Provider activity by **region**.

---

### 5. 📊 Key Statistics Snapshot
**KPIs**
- Total AT Spend → `Market by Total` → `Payments`
- Participants with AT → `ActPrtpnt by Total` → `Active participants`
- Active Providers → `Provider by Total` → `Active provider`
- Utilisation → `Market by Total` → `Utilisation`
- Avg Committed Support → `ActPrtpnt by Total` → `Average committed support`
- Innovation Uptake → **Simulated (3.5%)**

---

## ⚙️ Deployment

### Requirements
Create `requirements.txt`:
```
streamlit>=1.38
pandas>=2.1
altair>=5.0
openpyxl>=3.1
```

### Run locally
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

### Streamlit Cloud
1. Push repo to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io/).
3. Select repo and set main file → `streamlit_app.py`.
4. App will build and deploy automatically.

### Render / Docker (optional)
Use a `Dockerfile` for containerised deployment (see docs).

---

## 🚧 Roadmap
- Replace simulated data with internal NDIA datasets:
  - AT item-level expenditure
  - Participant complexity tiers
  - Functional domains of AT
  - Provider activity & reach
  - Delivery / repair turnaround metrics
  - Flexible/subscription claims
- Integrate **asset register** once established, to link spend with lifecycle management.
- Add **regional breakdowns** to enhance thin-market monitoring.

---

## 📝 Notes
- **Colour themes per section**:
  - Expenditure = Blue
  - Participants = Green
  - Market Dynamics = Orange
  - Providers = Purple
- This improves quick visual separation across the dashboard.
