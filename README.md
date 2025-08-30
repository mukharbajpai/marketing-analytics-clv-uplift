# Marketing Analytics: Customer Lifetime Value & Campaign Uplift Analysis

## Project Overview
This project combines **data analytics and marketing insights** to analyze customer behavior and evaluate the effectiveness of marketing campaigns. The analysis demonstrates how transaction patterns and campaign treatments impact **customer conversions**, providing actionable insights for business decisions.

---

## Dataset
- **Transactions Data**: Contains customer purchase records with columns like `customer_id`, `tx_date`, `amount`, `category`, `channel`.  
- **Campaign Data**: Contains marketing campaign results with columns like `customer_id`, `treatment`, `converted`, `revenue`.  

> All sensitive or large raw data files are excluded from this repo for privacy and size considerations.

---

## Key Analysis Performed
1. **Exploratory Data Analysis (EDA)**
   - Distribution of transaction amounts
   - Transactions per customer
   - Campaign response rates
   - Visualizations using Matplotlib and Seaborn

2. **Campaign Uplift Analysis**
   - Compared **treatment vs control** group conversions
   - Calculated **conversion rates, 95% confidence intervals**, and **p-values**
   - Found statistically significant uplift in the treatment group

3. **Insights**
   - The campaign treatment **significantly increased conversions** (p-value ≈ 2.85e-8)
   - Visualized key metrics for quick interpretation
   - Can be extended to **compute incremental revenue** and **predictive modeling for CLV**

---

## How to Run
1. Clone the repository:

```bash
git clone https://github.com/<your-username>/marketing-analytics-clv-uplift.git
