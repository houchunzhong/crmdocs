# Funding Data Module

## 1. Module Overview

The **Funding Data** module serves as the financial analytics hub of MIM CRM, presenting daily capital movements through structured tables and supporting the following features:

- ✅ **Daily Funding Report**: View daily metrics including new registrations, active users, deposit/withdrawal amounts, and user counts  
- ✅ **Key Ratio Calculations**: Automatically compute core indicators such as the **Withdrawal-to-Deposit Ratio** and **Successful Withdrawal Rate**  
- ✅ **Trend Insights**: Compare data across multiple days to identify growth patterns or risk signals  

📊 All data is generated from real-time system statistics and can be exported as CSV for in-depth analysis.

---

## 2. Main Interface Layout

### Left Navigation Menu

| Item | Function |
|------|----------|
| **Funding Data** | View daily funding transaction details |
| **Channel Management** | Analyze performance across marketing channels |
| **Total Visits** | Track cumulative website traffic |
| **Overall Conversion Rate** | Measure efficiency from visit to registration |
| **Daily Visits** | Count of unique daily visitors |
| **Daily Conversion Rate** | Daily registration conversion rate |

### Top Tab Bar

| Tab | Description |
|-----|-------------|
| **Overview** | Return to the parent page |
| **Payment Channels** | Review funding performance by payment method |
| **Funding Data** | Display the daily funding detail table |

---

## 3. Core Function Details

### 1. Funding Data List (Daily Funding Report)

#### Function Description  
Displays capital flow over recent days in a tabular format, with each row representing one day’s data—enabling easy cross-day comparison and trend analysis.

#### Field Definitions

| Field | Description |
|-------|-------------|
| **Date** | Date of the data (format: YYYY/MM/DD) |
| **New Registrations** | Number of new users registered that day |
| **Active Users** | Users who logged in or traded that day |
| **Deposit Amount** | Total successful deposits (in USD) |
| **Deposit Transactions** | Total number of deposit operations |
| **Depositing Users** | Number of users who made at least one deposit |
| **First-Time Deposits** | Amount contributed by users making their first deposit |
| **Repeat Deposits** | Cumulative amount from returning depositors |
| **Withdrawal Requests** | Total withdrawal amount requested that day |
| **Withdrawal Transactions** | Total number of withdrawal requests |
| **Withdrawing Users** | Number of users submitting withdrawal requests |
| **Successful Withdrawal Amount** | Total amount successfully processed |
| **Successful Withdrawal Transactions** | Number of completed withdrawal operations |
| **Successful Withdrawing Users** | Number of users who completed withdrawals |
| **Withdrawal-to-Deposit Ratio** | `Successful Withdrawal Amount / Deposit Amount` — reflects capital outflow pressure |

#### Example Interpretation  
Assume the following data for a given day:  
- **Date**: 2025/10/27  
- **Deposit Amount**: $78,900 USD  
- **Successful Withdrawal Amount**: $12,000 USD  
- **Withdrawal-to-Deposit Ratio**: 15.21%  

→ This indicates strong capital inflow and low outflow, reflecting a healthy net positive funding position for the platform.

> 💡 Tip: If the **Withdrawal-to-Deposit Ratio** exceeds 30% for multiple consecutive days, be alert to potential customer attrition or a surge in withdrawal demand.

---

### 2. Key Metrics: Definitions & Use Cases

| Metric | Meaning | Application Scenario |
|--------|---------|----------------------|
| **New Registrations** | User growth rate | Evaluate marketing campaign effectiveness |
| **Active Users** | User engagement level | Assess product stickiness |
| **Deposit Amount** | Strength of capital inflow | Monitor core revenue streams |
| **First-Time Deposits** | Contribution from new users | Measure quality of user acquisition |
| **Repeat Deposits** | Repurchase behavior of existing users | Estimate customer lifetime value (LTV) |
| **Withdrawal Requests vs. Successful Withdrawals** | Processing efficiency | Identify payment delays or technical issues |
| **Withdrawal-to-Deposit Ratio** | Liquidity risk indicator | Flag potential cash flow pressure |

---

### 3. Data Visualization Recommendations (Future Enhancement)

Although the current interface uses only tables, we recommend adding charting support in future versions:

- 📈 **Line Chart**: Show time trends for *Deposit Amount* and *Withdrawal Amount*  
- 📊 **Bar Chart**: Compare *New Registrations* and *Active Users* across dates  
- 🧩 **Heatmap**: Highlight high-volatility days (e.g., around holidays)

> 🔍 Suggestion: Set a red-alert threshold for the **Withdrawal-to-Deposit Ratio** (e.g., >30%) to trigger automated notifications.

---

## 4. Best Practices

| Scenario | Recommendation |
|----------|----------------|
| **Daily Monitoring** | Review *Deposit Amount* and *Withdrawal-to-Deposit Ratio* daily to establish baselines |
| **Anomaly Investigation** | If *Successful Withdrawal Transactions* are significantly lower than *Withdrawal Requests*, check for payment channel failures |
| **Marketing Evaluation** | Compare *New Registrations* and *First-Time Deposits* during promotions to assess ROI |
| **Risk Alerting** | Configure alerts for high *Withdrawal-to-Deposit Ratio* to prevent liquidity strain |

---

## 5. Frequently Asked Questions (FAQ)

**Q1: How often is the data updated?**  
✅ In real time. Each transaction is recorded under its respective date immediately upon completion.

**Q2: Why is “Successful Withdrawal Amount” less than “Withdrawal Requests”?**  
❌ This is normal. Some withdrawals may fail due to compliance rejection, insufficient balance, or other validation issues.

**Q3: Can I export the full dataset?**  
✅ Yes. Click the **“Export CSV”** button in the top-right corner to download all records (including hidden columns).

**Q4: How can I view data for a custom date range?**  
⚠️ The current version supports only the last 15 days. Custom date-range filtering will be available in a future release.

---

## 6. Summary

The **Funding Data** module in MIM CRM provides businesses with a transparent and precise view of capital flows. Through structured daily reports and key ratio analysis, administrators can quickly grasp business dynamics, respond promptly to market changes, and optimize funding management strategies.

✅ **Recommended Workflow**:  
1. Review *Deposit Amount* and *Withdrawal-to-Deposit Ratio* daily  
2. Periodically analyze *First-Time Deposit* trends  
3. Compare *Active Users* vs. *New Registrations*  
4. Detect anomalies and take corrective action  

📌 All data originates from real transaction records, ensuring reliable decision-making.

---

**Version: v1.0**  
**Last Updated: January 2026**