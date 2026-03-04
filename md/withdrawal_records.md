# **Withdrawal Records**  


## **1. Module Overview**

The **Withdrawal Records** module serves as the **withdrawal audit center** of MIM CRM, displaying all successfully processed or failed user withdrawal requests. It supports filtering by order ID, payment method, status, time, and more, offering comprehensive transaction details and operation logs to help administrators fully understand fund outflows. Key features include:

- ✅ View all historical withdrawal records (successful / failed)  
- ✅ Quickly search for specific transactions using multiple criteria  
- ✅ Access detailed information for each transaction (e.g., payment channel, fees, IP address)  
- ✅ Support for multiple payment channels (e.g., bank transfer, USDT, cryptocurrency)  
- ✅ Real-time synchronization of wallet balance changes  

> 🔐 Access is restricted to **System Administrators** or **Finance Managers** only. All data comes from real transactions and cannot be altered, suitable for internal audits and external compliance checks.

---

## **2. Interface Layout**

### **Left Navigation Menu**
| Item | Function |
|------|----------|
| **Funds** | Enter the main funds management menu |
| - Pending Deposits | View pending deposit requests |
| - Deposit Records | View historical deposit data |
| - Pending Withdrawals | View pending withdrawal requests |
| - Withdrawal Records | View historical withdrawal data |

---

### **Top Tab Bar**
| Tab | Description |
|-----|-------------|
| **Overview** | Return to the Funds module homepage |
| **Withdrawal Records** | Current page |

---

### **Withdrawal Records List View**
| Field | Description |
|-------|-------------|
| **Order ID** | Unique identifier (e.g., `WD20260210121801870950`) – clickable to view details |
| **Withdrawal Status** | Current status: "Approved", "Payment Successful", "Pending Payment", "Rejected", "Refund Successful" |
| **User** | Associated user ID or nickname (e.g., "Akina Akiyama 16672") |
| **Source Wallet** | Wallet from which funds are withdrawn (e.g., "MT5&AQX Wallet 13345") |
| **Withdrawal Amount** | Actual amount withdrawn (e.g., `-200.00 USD`) |
| **Post-Withdrawal Balance** | Final balance after withdrawal (e.g., `100.00 USD`) |
| **Exchange Rate Converted Amount** | Final amount after currency conversion (e.g., `190.00 USD`) |
| **User IP Address** | Client IP when submitting request (e.g., `208.98.44.2`) |
| **Submission Time** | Time when user initiated the request (e.g., `10/02/2026 12:18:02`) |
| **Action** | Contains **View** button to access detail page |

> 💡 Example: Order ID `WD20260210121801870950` shows status as "Approved" and "Payment Successful", amount of -200.00 USD, and source wallet MT5&AQX Wallet 13345.

---

## **3. Core Feature Details**

### **1. View Withdrawal Details**

#### **Procedure**
1. In the **Withdrawal Records** list, locate the target order (e.g., `WD20260210121801870950`)  
2. Click **View**  
3. Enter the detail page, divided into sections:
   - **Basic Info**: Order ID, payment method (e.g., Bank Transfer), source wallet, amount, etc.  
   - **Withdrawal Details**: User ID, name, withdrawal amount, exchange rate, converted amount, fee, user IP, submission time  
   - **Recipient Account (User's)**: Account type (e.g., Bank Card), recipient name, account number, bank name, address  
   - **Review Details**: Reviewer ID, reviewer name, review time, internal/external notes  
   - **Payment Details**: Payment ID, operator, payment time, completion time, processing duration  

> ✅ Example: When reviewing a bank transfer withdrawal, confirm if it has been settled, check for delays, and determine if manual intervention is needed.

---

### **2. Multi-Condition Filtering & Search**

#### **Available Filters**
- **Submission Time From ~ To**: Filter by date range  
- **Payment Channel**: e.g., "Bank Transfer", "USDT", "Crypto - Tron"  
- **Withdrawal Status**: Choose "Approved", "Payment Successful", "Pending Payment", "Rejected", "Refund Successful"  
- **Operator**: Specify reviewer  
- **Source Wallet**: Specify wallet number (e.g., 13345)  
- **ID/Name/Order ID Search**: Quickly locate specific user or order  

> ✅ Pro Tip: Combine "Payment Channel" and "Status" filters to prioritize high-priority anomalies.

---

### **3. Data Export & Reconciliation Support**

#### **Function Description**
- While the current version does not have a direct "Export" button, data can be obtained via:
  - Copying table content after filtering  
  - Future versions will support CSV/Excel export  
- All data can be used for:
  - Internal financial reconciliation  
  - Third-party audit reports  
  - User dispute investigations  

> ✅ Example: Finance team uses "Submission Time" filter to extract all "Payment Successful" transactions from last month for monthly reporting.

---

## **4. Typical Use Cases**

### **Use Case 1: Financial Reconciliation & Month-End Preparation**

> 🎯 Goal: Prepare monthly financial statements

- ✅ Implementation:
  1. Log in → Go to **Funds → Withdrawal Records**  
  2. Set filters:
     - Submission Time: `01/02/2026 ~ 28/02/2026`  
     - Withdrawal Status: `Payment Successful`  
     - Payment Channel: `All`  
  3. Review all transaction details  
  4. Copy data and import into accounting software  
  5. Generate monthly expense report

> ✅ Outcome: Improves financial efficiency and reduces human error.

---

### **Use Case 2: Resolving User Complaints**

> 🎯 Goal: Address user complaints about "no credit"

- ✅ Implementation:
  1. User reports: I withdrew 200 USD, but my bank hasn't received it  
  2. Search in **Withdrawal Records** for user ID `16672`  
  3. Find order `WD20260210121801870950` with status "Payment Successful"  
  4. Open detail page → Check "Payment Details" section → Payment ID exists  
  5. Contact bank → Confirm delay due to holiday  
  6. Notify user of expected arrival time and reassure them

> ✅ Outcome: Rapidly identifies root cause and improves customer satisfaction.

---

### **Use Case 3: Analyzing User Withdrawal Behavior**

> 🎯 Goal: Identify high-value user segments

- ✅ Implementation:
  1. Filter withdrawals with amount > 5000 USD  
  2. Calculate percentage by payment method (e.g., VISA vs USDT)  
  3. Analyze these users’ activity level, trading frequency, product preferences  
  4. Share insights with marketing team to design exclusive services

> ✅ Outcome: Enables precision marketing and increases retention among premium users.

---

## **5. Best Practices**

| Scenario | Recommendation |
|---------|----------------|
| **Regular Audits** | Conduct full withdrawal record reviews monthly to ensure no omissions or anomalies |
| **Anomaly Monitoring** | Monitor "Rejected" or "Refund Successful" statuses closely and follow up promptly |
| **Document Archiving** | Archive important transaction evidence and notes for future reference |
| **Access Control** | Restrict sensitive data access to authorized personnel only |
| **Automated Alerts** | Future versions will include automatic alerts when large numbers of failed transactions occur |

---

## **6. Frequently Asked Questions (FAQ)**

### **Q1: Why does some withdrawal show "Pending Payment"?**  
- ❌ Possible causes: Payment gateway hasn't completed settlement, or funds are still clearing  
- ✅ Solution: Contact payment provider to confirm status, or set up auto-retry mechanism

---

### **Q2: Can I modify an existing withdrawal amount?**  
- ❌ Not allowed.  
- ✅ For adjustments, use the **Fund Operations** module to submit a manual adjustment request.

---

### **Q3: How do I find a user’s full withdrawal history?**  
- ✅ Method: Enter user ID or name (e.g., `16672`) in the search box to retrieve all related records.

---

### **Q4: How long are withdrawal records retained?**  
- ✅ Retained permanently unless system policy specifies otherwise.  
- ⚠️ Recommendation: Keep indefinitely to meet regulatory requirements.

---

## **7. Summary**

The **Withdrawal Records** module is a critical component of MIM CRM for achieving **transparent and compliant fund outflow management**. It not only provides full transaction audit capabilities but also supports collaboration across finance, operations, and customer service teams. Through scientific data management and efficient query mechanisms, organizations can build a robust financial system, delivering safe and trustworthy services to users.

✅ **Recommended Workflow**:  
1. Go to **Funds → Withdrawal Records** → 2. Use filters to locate target order → 3. Click **View** → 4. Review details → 5. Analyze or export data

> 📌 All data is immutable and supports auditing and traceability, ensuring operational transparency and compliance.

---

**Version: v1.0**  
**Last Updated: February 2026**