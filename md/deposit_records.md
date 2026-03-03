# **Deposit Records**  

## **1. Module Overview**

The **Deposit Records** module serves as the **deposit audit center** of MIM CRM, displaying all successfully processed or failed user deposit requests. It supports filtering by order ID, payment method, status, time, and more, offering comprehensive transaction details and operation logs to help administrators fully understand fund flows. Key features include:

- ✅ View all historical deposit records (successful / failed)  
- ✅ Quickly search for specific transactions using multiple criteria  
- ✅ Access detailed information for each transaction (e.g., payment channel, fees, IP address)  
- ✅ Support for multiple payment channels (e.g., VISA, USDT, bank transfer)  
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

---

### **Top Tab Bar**
| Tab | Description |
|-----|-------------|
| **Overview** | Return to the Funds module homepage |
| **Deposit Records** | Current page |

---

### **Deposit Records List View**
| Field | Description |
|-------|-------------|
| **Order ID** | Unique identifier (e.g., `P20260212155654208237`) – clickable to view details |
| **Deposit Status** | Current status: "Approved", "Pending Receipt", "Failed", "Completed" |
| **User** | Associated user ID or nickname (e.g., "Akina Akiyama 16672") |
| **Receiving Wallet** | Target wallet address (e.g., "MT5&AQX Wallet 13345") |
| **Deposit Amount** | Actual amount credited (e.g., `+1,000.00 USD`) |
| **Post-Deposit Balance** | Final balance after approval (e.g., `2,500.00 USD`) |
| **Payment Amount** | Amount paid by user (e.g., `1500 USD`) |
| **User IP Address** | Client IP when submitting request (e.g., `46.19.78.201`) |
| **Submission Time** | Time when user initiated the request (e.g., `12/02/2026 15:56:54`) |
| **Action** | Contains **View** button to access detail page |

> 💡 Example: Order ID `P20260212155654208237` shows status as "Approved", amount of 1,000.00 USD, and target wallet MT5&AQX Wallet 13345.

---

## **3. Core Feature Details**

### **1. View Deposit Details**

#### **Procedure**
1. In the **Deposit Records** list, locate the target order (e.g., `P20260212155654208237`)  
2. Click **View**  
3. Enter the detail page, divided into sections:
   - **Basic Info**: Order ID, payment method (e.g., VISA - Paymentgateway), receiving wallet, amount, etc.  
   - **Deposit Details**: User ID, name, deposit amount, exchange rate, converted amount, fee, user IP, submission time  
   - **Online Deposit**: Payment channel, payment ID, submission time, processing duration  
   - **Offline Deposit (if applicable)**: Bank account info, uploaded documents, reviewer, notes  
   - **Deposit Evidence**: Scanned copies, screenshots, or proof materials (e.g., blockchain hash)  
   - **Review Details**: Reviewer ID, review time, internal/external notes  
   - **Manual Offline Deposit**: External reference number, arrival time, handler  

> ✅ Example: When reviewing a VISA deposit, confirm if it has been settled, check for delays, and determine if manual intervention is needed.

---

### **2. Multi-Condition Filtering & Search**

#### **Available Filters**
- **Submission Time From ~ To**: Filter by date range  
- **Deposit Status**: Choose "Approved", "Pending Receipt", "Failed", "Completed"  
- **Payment Channel**: e.g., "VISA", "USDT", "Bank Transfer"  
- **Operator**: Specify reviewer  
- **Wallet**: Specify wallet number (e.g., 13345)  
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

> ✅ Example: Finance team uses "Submission Time" filter to extract all "Completed" transactions from last month for monthly reporting.

---

## **4. Typical Use Cases**

### **Use Case 1: Financial Reconciliation & Month-End Preparation**

> 🎯 Goal: Prepare monthly financial statements

- ✅ Implementation:
  1. Log in → Go to **Funds → Deposit Records**  
  2. Set filters:
     - Submission Time: `01/02/2026 ~ 28/02/2026`  
     - Deposit Status: `Completed`  
     - Payment Channel: `All`  
  3. Review all transaction details  
  4. Copy data and import into accounting software  
  5. Generate monthly revenue report

> ✅ Outcome: Improves financial efficiency and reduces human error.

---

### **Use Case 2: Resolving User Complaints**

> 🎯 Goal: Address user complaints about "no credit"

- ✅ Implementation:
  1. User reports: I deposited 1000 USD, but my balance didn’t change  
  2. Search in **Deposit Records** for user ID `16672`  
  3. Find order `P20260212155654208237` with status "Approved" but "Pending Receipt"  
  4. Open detail page → Check "Online Deposit" section → No payment ID found  
  5. Contact payment gateway → Confirm settlement not completed  
  6. Manually initiate refund process and notify user

> ✅ Outcome: Rapidly identifies root cause and improves customer satisfaction.

---

### **Use Case 3: Analyzing User Deposit Behavior**

> 🎯 Goal: Identify high-value user segments

- ✅ Implementation:
  1. Filter deposits with amount > 5000 USD  
  2. Calculate percentage by payment method (e.g., VISA vs USDT)  
  3. Analyze these users’ activity level, trading frequency, product preferences  
  4. Share insights with marketing team to design exclusive services

> ✅ Outcome: Enables precision marketing and increases retention among premium users.

---

## **5. Best Practices**

| Scenario | Recommendation |
|---------|----------------|
| **Regular Audits** | Conduct full deposit record reviews monthly to ensure no omissions or anomalies |
| **Anomaly Monitoring** | Monitor "Failed" or "Pending Receipt" statuses closely and follow up promptly |
| **Document Archiving** | Archive important transaction evidence and notes for future reference |
| **Access Control** | Restrict sensitive data access to authorized personnel only |
| **Automated Alerts** | Future versions will include automatic alerts when large numbers of failed transactions occur |

---

## **6. Frequently Asked Questions (FAQ)**

### **Q1: Why does some deposit show "Pending Receipt"?**  
- ❌ Possible causes: Payment gateway hasn't completed settlement, or funds are still clearing  
- ✅ Solution: Contact payment provider to confirm status, or set up auto-retry mechanism

---

### **Q2: Can I modify an existing deposit amount?**  
- ❌ Not allowed.  
- ✅ For adjustments, use the **Fund Operations** module to submit a manual adjustment request.

---

### **Q3: How do I find a user’s full deposit history?**  
- ✅ Method: Enter user ID or name (e.g., `16672`) in the search box to retrieve all related records.

---

### **Q4: How long are deposit records retained?**  
- ✅ Retained permanently unless system policy specifies otherwise.  
- ⚠️ Recommendation: Keep indefinitely to meet regulatory requirements.

---

## **7. Summary**

The **Deposit Records** module is a critical component of MIM CRM for achieving **transparent and compliant fund flow management**. It not only provides full transaction audit capabilities but also supports collaboration across finance, operations, and customer service teams. Through scientific data management and efficient query mechanisms, organizations can build a robust financial system, delivering safe and trustworthy services to users.

✅ **Recommended Workflow**:  
1. Go to **Funds → Deposit Records** → 2. Use filters to locate target order → 3. Click **View** → 4. Review details → 5. Analyze or export data

> 📌 All data is immutable and supports auditing and traceability, ensuring operational transparency and compliance.

---

**Version: v1.0**  
**Last Updated: February 2026**