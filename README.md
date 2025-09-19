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
**What this section tells us**  
Expenditure is the most direct signal of the AT market’s scale and momentum. Tracking payments and committed supports allows us to see how much funding is flowing into AT compared to all NDIS supports, and whether budgets are being used efficiently (via utilisation).

**KPIs**
- AT Payments → `Market by Total` → `Payments`
- AT Committed Supports → `Market by Total` → `Committed supports`
- Utilisation → `Market by Total` → `Utilisation`

**Plots**
- **Trend of AT Payments (Area Chart)** → Shows changes in AT spend across reporting periods. Driven by *Market by Total → Payments*.
- **Top 10 AT Support Items by Spend** → **Simulated** (wheelchairs, AAC devices, hearing aids, etc.).

📌 *Future needs: claim-level data by support item code.*

---

### 2. 👥 Participants
**What this section tells us**  
Participant data shows **who** is driving AT demand, how complex their needs are, and how usage patterns differ by spend, function, and disability.

**KPIs**
- Active AT Participants → `ActPrtpnt by Total` → `Active participants`
- Complex AT Users → **Simulated (30%)**. Refers to participants needing multiple/high-cost devices.
- Median AT Spend → **Simulated ($3.2K)**

**Plots**
- **Complexity (Donut)** → Simple vs Complex users (simulated).  
- **Spend Intensity (Bar)** → Simulated split: Low (<$1K), Moderate ($1K–10K), High (>$10K).  
- **Functional Domains (Bar)** → Simulated split across Mobility, Communication, Self-care, Vision/Hearing, Cognition.  
- **Primary Disability (Lollipop)** → Simulated distribution across Cerebral palsy, Autism, MS, etc.

📌 *Future needs: plan-level data on AT complexity tiers, spend by functional domains, and disability group breakdown.*

---

### 3. 📈 Market Dynamics
**What this section tells us**  
This section looks at **system performance** — not just how much is spent, but how well the market functions in meeting participant needs.

**KPIs (all simulated currently)**
- Median Delivery Time (44 days) → access speed.  
- % Repairs <14 Days (72%) → continuity measure.  
- Provider Churn (4%) → market stability.  
- Innovation Uptake (3.5%) → share of spend using flexible/subscription codes or digital AT.  

**Plots**
- **Innovation Uptake Trend (Line)** → Simulated % spend growth via innovative pathways.  
- **Regional Delivery Times (Bar)** → Simulated averages: Metro = 38, Regional = 46, Remote = 54.  
- **Market Concentration (Donut)** → Simulated: top 5 providers = 45% of spend.

📌 *Future needs: turnaround times in claims, provider churn tracking, claims flagged to flexible/subscription codes, HHI calculations.*

---

### 4. 🏢 Providers
**What this section tells us**  
Providers are the supply side of the AT market. Monitoring scope, reach, and distribution shows market resilience and thin market risks.

**KPIs**
- Active AT Providers → `Provider by Total` → `Active provider`
- Participants per Provider → Derived: participants ÷ providers  
- Top 5 Provider Share → **Simulated (45%)**

**Plots**
- **Provider Reach Distribution (Histogram)** → Simulated buckets of participants served.  
- **Scope of Supply (Donut)** → Simulated split: Multi-line vs Niche providers.  
- **Regional Coverage (Bar)** → Simulated split: Metro 70%, Regional 25%, Remote 5%.

📌 *Future needs: provider-claim linkage, registration groups vs supply, regional mapping of activity.*

---

### 5. 📊 Key Statistics Snapshot
**What this section tells us**  
A quick **executive summary card**, pulling key data points into one glance.

**KPIs**
- Total AT Spend → `Market by Total` → `Payments`
- Participants with AT → `ActPrtpnt by Total` → `Active participants`
- Active Providers → `Provider by Total` → `Active provider`
- Utilisation → `Market by Total` → `Utilisation`
- Avg Committed Support → `ActPrtpnt by Total` → `Average committed support`
- Innovation Uptake → **Simulated (3.5%)**

---

## 📋 KPI & Plot Mapping

| Section        | KPI / Plot                         | Source                               | Real / Simulated | Data Needs |
|----------------|-------------------------------------|--------------------------------------|------------------|------------|
| Expenditure    | AT Payments                        | Market by Total → Payments           | Real             | – |
|                | AT Committed Supports              | Market by Total → Committed supports | Real             | – |
|                | Utilisation                        | Market by Total → Utilisation        | Real             | – |
|                | Trend of AT Payments (area)        | Market by Total → Payments           | Real             | – |
|                | Top 10 AT Items                    | –                                    | Simulated        | Item-level claim data |
| Participants   | Active AT Participants             | ActPrtpnt by Total → Active participants | Real        | – |
|                | Complex AT Users                   | –                                    | Simulated        | Complexity tiers |
|                | Median AT Spend                    | –                                    | Simulated        | Distributional data |
|                | Complexity (Donut)                 | –                                    | Simulated        | Complexity tiers |
|                | Spend Intensity (Bar)              | –                                    | Simulated        | Plan-level spend |
|                | Functional Domains (Bar)           | –                                    | Simulated        | Assessment-linked AT |
|                | Primary Disability (Lollipop)      | –                                    | Simulated        | Disability-linked AT |
| Market Dynamics| Median Delivery Time               | –                                    | Simulated        | Delivery times data |
|                | % Repairs <14 Days                 | –                                    | Simulated        | Repair turnaround |
|                | Provider Churn                     | –                                    | Simulated        | Provider entry/exit |
|                | Innovation Uptake                  | –                                    | Simulated        | Flexible/subscription claims |
|                | Innovation Uptake Trend (Line)     | –                                    | Simulated        | Flexible claims trend |
|                | Regional Delivery Times (Bar)      | –                                    | Simulated        | Regional service data |
|                | Market Concentration (Donut)       | –                                    | Simulated        | Provider-level payments |
| Providers      | Active AT Providers                | Provider by Total → Active provider  | Real             | – |
|                | Participants per Provider          | Derived                              | Real             | – |
|                | Top 5 Provider Share               | –                                    | Simulated        | Provider-level payments |
|                | Provider Reach Distribution        | –                                    | Simulated        | Participants per provider |
|                | Scope of Supply (Donut)            | –                                    | Simulated        | Provider registration/supply |
|                | Regional Coverage (Bar)            | –                                    | Simulated        | Regional activity |
| Snapshot       | All above key figures              | Mixed                                | Mixed            | Replace simulated with NDIA data |

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
