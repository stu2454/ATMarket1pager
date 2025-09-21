# 📖 Narrative Guide to Dashboard Sections

## 1. 💰 Expenditure

**What this section tells us:**  
Expenditure is the most direct signal of the AT market’s scale and momentum. Tracking payments and committed supports allows us to see how much funding is flowing into AT compared to all NDIS supports, and whether budgets are being used efficiently (via utilisation).

**KPIs**

- **AT Payments** → The actual money reimbursed to providers for AT supports in the period. Derived from _Market by Total → Payments_.
- **AT Committed Supports** → The total funding allocated to participants for AT in plans. From _Market by Total → Committed supports_.
- **Utilisation** → The ratio of payments to committed supports (i.e. how much of planned funding is actually spent). From _Market by Total → Utilisation_.

**Plots**

- **Trend of AT Payments (Area Chart)** → Shows changes in AT spend across reporting periods, highlighting growth or plateau. Driven by _Market by Total → Payments_.
- **Top 10 AT Support Items (Simulated)** → Illustrates which devices drive the largest share of expenditure (wheelchairs, AAC devices, hearing aids, etc.). Currently simulated because item-level spend is not broken out in the Excel extract.

_Future needs:_ Item-level claim data, mapped to support item codes, to replace simulation with real categories.

---

## 2. 👥 Participants

**What this section tells us:**  
Participant data shows who is driving AT demand, how complex their needs are, and how usage patterns differ by spend, function, and disability.

**KPIs**

- **Active AT Participants** → Count of participants with committed AT supports. From _ActPrtpnt by Total → Active participants_.
- **Complex AT Users (Simulated, 30%)** → Participants whose needs cannot be met with a single device (e.g., those requiring combinations of wheelchairs, hoists, communication aids). Currently simulated; in future could be derived from multi-line AT claims in participant plans.
- **Median AT Spend (Simulated $3.2K)** → Midpoint of annual AT spend per participant. Currently simulated; would need claim-level participant distributions to calculate.

**Plots**

- **Complexity (Donut)** → Split between “Simple” and “Complex” AT users. Highlights that complex users consume disproportionate budget share.
- **Spend Intensity (Bar)** → Distribution of participants into low, moderate, and high spend categories.
- **Functional Domains (Bar)** → Simulated allocation of participants by functional impairment categories (Mobility, Communication, Self-care, Vision/Hearing, Cognition).
- **Primary Disability (Lollipop)** → Simulated distribution of AT users by primary disability type (Cerebral palsy, Autism, MS, Intellectual disability, Hearing impairment, Other).

_Future needs:_

- Plan/claim-level linkage of AT spend to functional assessment data.
- Standardised complexity tiers.
- AT utilisation breakdown by disability group.

---

## 3. 📈 Market Dynamics

**What this section tells us:**  
This section looks at system performance — not just how much is spent, but how well the market functions in meeting participant needs.

**KPIs (Simulated for now)**

- **Median Delivery Time (44 days)** → Time from approval/commitment to delivery of AT.
- **% Repairs <14 Days (72%)** → Share of repairs resolved within benchmark timeframe.
- **Provider Churn (4% this quarter)** → % of providers entering/exiting market.
- **Innovation Uptake (3.5%)** → Share of total AT spend using innovative pathways (subscription, connected AT, adaptive bundles).

**Plots**

- **Innovation Uptake Trend (Line)** → Simulated trend across quarters.
- **Regional Delivery Times (Bar)** → Simulated averages by metro, regional, remote.
- **Market Concentration (Donut)** → Simulated share of spend concentrated in top 5 providers.

_Future needs:_

- Time-to-delivery and repair turnaround metrics embedded in claims.
- Tracking of subscription/flexible models.
- Ongoing churn and HHI (Herfindahl–Hirschman Index) for competition monitoring.

---

## 4. 🏢 Providers

**What this section tells us:**  
Providers are the supply side of the AT market. Monitoring their scope, reach, and distribution gives insight into resilience and thin market risks.

**KPIs**

- **Active AT Providers** → From _Provider by Total → Active provider_.
- **Participants per Provider** → Derived metric: participants ÷ providers.
- **Top 5 Provider Share (Simulated 45%)** → Share of payments captured by 5 largest providers.

**Plots**

- **Provider Reach Distribution (Histogram)** → Simulated split of providers by participant reach (<10, 10–50, etc.).
- **Scope of Supply (Donut)** → Multi-line vs niche providers.
- **Regional Coverage (Bar)** → Simulated share of providers across metro, regional, remote.

_Future needs:_

- Item-level provider claims for diversification analysis.
- Regional mapping of provider activity vs demand.
- Linking provider exits to participant outcomes.

---

## 5. 📊 Key Statistics Snapshot

**What this section tells us:**  
A quick executive summary box, capturing essential signals across expenditure, participants, providers, and innovation.

**KPIs**

- **Total AT Spend** → From _Market by Total → Payments_.
- **Participants with AT** → From _ActPrtpnt by Total → Active participants_.
- **Active Providers** → From _Provider by Total → Active provider_.
- **Utilisation** → From _Market by Total → Utilisation_.
- **Avg Committed Support** → From _ActPrtpnt by Total → Average committed support_.
- **Innovation Uptake** → Simulated (3.5%).

---

## 🚀 Why This Matters

- **Expenditure** shows the scale of the AT economy.
- **Participants** reveal the human side: who uses AT, how complex their needs are.
- **Market Dynamics** measure system performance, timeliness, and innovation.
- **Providers** highlight supply resilience and thin market risks.
- **Snapshot** ties it all together for executives.
