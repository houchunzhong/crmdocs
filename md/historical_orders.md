# **Historical Orders**  

## **1. Module Overview**

The **Historical Orders** module acts as the **trading behavior analytics hub** of MIM CRM. It offers a comprehensive view of all settled and open orders from three major trading systems: **MT5**, **AQX**, and **BO**. With multi-dimensional filtering by platform, account, time, and order type, it empowers operations and compliance staff to:

- ✅ Reconstruct a user’s complete trading journey  
- ✅ Analyze profitability trends and trading cycles  
- ✅ Detect abnormal behaviors (e.g., excessive scalping, large volatility trades)  
- ✅ Support advanced data export and reporting  

> 🔐 Access is restricted to **Administrators**, **Operations Managers**, or **Compliance Officers** only. All data is synchronized in real time from live trading servers, ensuring accuracy and timeliness.

---

## **2. Interface Layout**

### **Left Navigation Menu**
| Item | Function |
|------|----------|
| **Historical Orders** | View all past trade orders |
| **BO Open Positions** | View currently held BO platform positions |

---

### **Top Tab Bar**
| Tab | Description |
|-----|-------------|
| **Overview** | Return to parent page |
| **Historical Orders** | Current page |

---

## **3. Core Feature Details**

### **1. Platform Switching**

#### **Function Description**  
Three platform tabs at the top—**MT5**, **AQX**, and **BO**—allow users to filter historical order data by trading system.

#### **Platform Definitions**
| Platform | Description |
|----------|-------------|
| **MT5** | MetaTrader 5 terminal, used for mainstream Forex, precious metals, and CFD trading |
| **AQX** | TradeWise’s proprietary algorithmic trading platform, supporting strategy automation and API integration |
| **BO** | Back Office trading system, typically used for institutional clients or internal test accounts |

> 💡 Example: To analyze a client’s MT5 trading habits, switch to the MT5 tab and apply relevant filters.

---

### **2. Main Order View (MT5 / AQX / BO)**

#### **Function Description**  
Displays all historical orders for the selected platform in a sortable, searchable table with pagination.

#### **Field Definitions**

##### **MT5 & AQX Views**
| Field | Description |
|-------|-------------|
| **Order ID** | Unique identifier (e.g., `9988`); clickable for details |
| **Trading Account** | Linked account ID (e.g., `500067`), labeled as “LIVE” or “DEMO” |
| **Instrument** | Traded symbol (e.g., `GBPUSD`, `EURUSD`, `XAUUSD`) |
| **Type** | Direction: SELL / BUY / ENTRY_IN / ENTRY_OUT |
| **Volume** | Opening lot size (e.g., `0.2`) |
| **Closed Volume** | Closed portion (e.g., `0.00` = still open) |
| **Price** | Execution price (e.g., `1.36108`) |
| **Time** | Execution timestamp (to the second) |
| **Commission Settlement** | Commission generated (usually `0.00` unless user rebate is enabled) |
| **Swap Fee** | Overnight holding cost |
| **P&L** | Floating profit/loss per trade (green = profit, red = loss) |

> ⚠️ Note: MT5 and AQX views do not include “Profit %,” but it can be derived from P&L and volume.

---

##### **BO View**
| Field | Description |
|-------|-------------|
| **Order ID** | System-generated unique ID (e.g., `1_BTCUSD_...`) |
| **Trading Account** | Account ID (e.g., `1` or `501085`) |
| **Status** | Current state:  
  - 🟩 **Profitable**: closed in profit  
  - 🔴 **Loss-making**: closed at a loss  
  - 🟨 **Pending**: not yet settled |
| **Instrument** | e.g., `BTCUSD`, `XAUUSD`, `AUDUSD` |
| **Type** | Rise / Fall (equivalent to Buy / Sell) |
| **Volume** | Lot size (e.g., `10.00`) |
| **Profit %** | Percentage return (e.g., `+88%`) |
| **P&L** | Actual monetary gain/loss (e.g., `+8.80`) |
| **Trade Duration** | Holding period (e.g., `30 s`) |
| **Order Time** | When the order was placed |
| **Open Time (Local)** | Actual opening time in local timezone |
| **Open Price** | Entry price (e.g., `67092.19`) |

> 💡 Example: Order `1_XAUUSD_...` shows “Loss -10.00,” indicating a $10 loss on gold.

---

### **3. Advanced Filtering & Search**

#### **Function Description**  
Supports complex query combinations for precise data retrieval.

#### **Filter Options**
| Control | Function |
|--------|----------|
| **Trading Server** | Filter by server type (e.g., `Options`, `Forex`, `Crypto`) |
| **Group** | Segment by account group (e.g., “VIP Clients”, “New Registrants”) |
| **LIVE / DEMO** | Distinguish real vs. simulated trading (critical for analysis) |
| **Order ID / Account Search** | Keyword search for specific orders or accounts |

> 💡 Best Practice: Combine “LIVE” + date range to focus exclusively on real-money trading behavior.

---

## **4. Data Analysis Use Cases**

### **1. Customer Trading Behavior Analysis**

#### **Use Case: Identify Active Clients**
- ✅ Method:  
  1. Go to **Historical Orders** → Select MT5 → Set time range (e.g., last 7 days)  
  2. Filter for “LIVE” orders  
  3. Group by “Trading Account” and count orders  
  4. Sort to find most frequent traders

> 📊 Output: Generate a “High-Activity Client List” for priority support or rewards.

---

#### **Use Case: Evaluate Strategy Effectiveness**
- ✅ Method:  
  1. Extract all orders for a specific user  
  2. Group by “Instrument”  
  3. Calculate average P&L and win rate per instrument  
  4. Discover preference for short-term, high-volatility assets (e.g., BTCUSD)

> 📊 Output: Determine if the user would benefit from product recommendations or risk management guidance.

---

### **2. Risk Monitoring & Compliance Review**

#### **Use Case: Detect Abnormal Patterns**
- ✅ Indicators:  
  - Excessive micro-trading (e.g., multiple entries per minute)  
  - Ultra-short durations (<10 seconds)  
  - Large losses followed immediately by reverse positions (emotional trading)

> 🔍 Procedure:  
  1. Filter for “Trade Duration” < `30s`  
  2. Check if “P&L” is consistently negative  
  3. Flag and escalate to compliance if pattern matches

---

#### **Use Case: Validate KYC Risk Controls**
- ✅ Method:  
  1. Review historical orders of a high-risk user  
  2. Check frequency of high-leverage instruments (e.g., crypto)  
  3. Cross-reference with KYC status to assess “identity mismatch” or “excessive speculation”

---

### **3. Reporting & Export Recommendations**

- ❌ Direct Excel export is not supported in the current version.  
- ✅ Workarounds:  
  - Manually copy table content into Excel  
  - Use the CRM API for bulk data extraction (requires technical support)  
  - Submit a feature request for “CSV Export” via the internal ticketing system

---

## **5. Frequently Asked Questions (FAQ)**

### **Q1: Why is there no data in the AQX platform?**  
- ❌ Possible reasons:  
  - The user hasn’t traded on AQX  
  - They only use MT5 or BO  
  - Data sync delay  

> ✅ Solution: Confirm if the user has an AQX-linked account; refresh after 5–10 minutes.

---

### **Q2: How do I view detailed information for a specific order?**  
- ✅ Steps:  
  1. Locate the target order in **Historical Orders**  
  2. Click the **Order ID**  
  3. A detail panel will appear showing full execution data, stop-loss/take-profit levels, and order type

---

### **Q3: What’s the difference between “LIVE” and “DEMO”?**  
- ✅ **LIVE**: Real-money trading with actual financial impact  
- ✅ **DEMO**: Simulated trading with virtual funds, used for practice or testing  

> 💡 Recommendation: Compliance reviews should focus exclusively on LIVE orders.

---

### **Q4: Can I view open (unrealized) positions?**  
- ✅ Yes. Navigate to the **BO Open Positions** sub-m