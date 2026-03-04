# **Refund Records**  

## **1. Module Overview**

The **Refund Records** module serves as the **fund rollback audit center** of MIM CRM, displaying all completed or pending refund requests. It supports filtering by order ID, refund reason, refund wallet, time, and more, offering comprehensive transaction details and operation logs to help administrators fully understand fund return scenarios. Key features include:

- ✅ View all historical refund records (successful / pending)  
- ✅ Quickly search for specific transactions using multiple criteria  
- ✅ Access detailed information for each refund (e.g., original withdrawal order, refund amount, IP address)  
- ✅ Support for multiple refund triggers (e.g., review rejection, payment failure, system error)  
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
| - Transfer Records | View historical transfer data |
| - Refund Records | View completed or pending refund data |

---

### **Top Tab Bar**
| Tab | Description |
|-----|-------------|
| **Overview** | Return to the Funds module homepage |
| **Refund Records** | Current page |

---

### **Refund Records List View**
| Field | Description |
|-------|-------------|
| **Order ID** | Unique identifier (e.g., `R20260223154447959436`) – clickable to view details |
| **Status** | Current status: "Refund Successful", "Pending" |
| **User** | Associated user ID or nickname (e.g., "Léa Petit 16686") |
| **Refund Wallet** | Target wallet for refund (e.g., "MT5&AQX Wallet 13374") |
| **Refund Reason** | Cause of refund (e.g., "Review Rejected WD20260209185624800435") |
| **Refund Amount** | Actual refunded amount (e.g., `+200.00 USD`) |
| **Post-Refund Balance** | Final balance after refund (e.g., `500.00 USD`) |
| **Refund Time** | Time when refund was completed (e.g., `23/02/2026 15:44:48`) |
| **Action** | Contains **View** button to access detail page |

> 💡 Example: Order ID `R20260223154447959436` shows status as "Refund Successful", amount of +200.00 USD, due to "Review Rejected".

---

## **3. Core Feature Details**

### **1. View Refund Details**

#### **Procedure**
1. In the **Refund Records** list, locate the target order (e.g., `R20260223154447959436`)  
2. Click **View**  
3. Enter the detail page, divided into sections:
   - **Original Withdrawal Info**: Original withdrawal order ID, user ID, name, amount, exchange rate, fee, etc.  
   - **Recipient Account (User's)**: Bank card info (e.g., SWIFT/BIC, bank name, account name, address)  
   - **Review Details**: Reviewer ID, review time, notes (e.g., "Incomplete documents")  
   - **Related Orders**: Shows linked transactions (e.g., original withdrawal), forming a complete fund chain  

> ✅ Example: When reviewing a refund triggered by "Review Rejected", confirm if it's linked to a KYC-failed withdrawal, helping assess risk level.

---

### **2. Multi-Condition Filtering & Search**

#### **Available Filters**
- **Refund Time From ~ To**: Filter by date range  
- **Refund Wallet**: Select target wallet (e.g., MT5&AQX Wallet)  
- **ID/Name/Order ID Search**: Quickly locate specific user or order  

> ✅ Pro Tip: Combine "Refund Reason" and "Time" filters to quickly identify bulk refund events.

---

### **3. Fund Lifecycle Tracing**

#### **Function Description**
- Each refund record automatically links to the upstream withdrawal order, forming a complete fund trail  
- The **Related Orders** section clearly displays:
  - Related order IDs  
  - Status of related orders (e.g., "Rejected", "Completed")  
  - Amount change direction (+/-)  
  - Post-change wallet balance  
  - Submission time  

> ✅ Example: If a user’s withdrawal is rejected, the system automatically initiates a refund and links it to the original order, aiding audit and accountability.

---

## **4. Typical Use Cases**

### **Use Case 1: Handling User Complaints & Customer Service**

> 🎯 Goal: Resolve user complaints about "withdrawal rejected but no refund"

- ✅ Implementation:
  1. User reports: I submitted a withdrawal, but it was rejected and my money wasn’t returned  
  2. Search in **Refund Records** for user ID `16686`  
  3. Find order `R20260223154447959436` with status "Refund Successful"  
  4. Open detail page → Check "Related Orders" → Confirm original withdrawal was rejected  
  5. Verify refund has been credited back to original wallet  
  6. Notify user that funds have been returned and explain rejection reason  

> ✅ Outcome: Improve customer satisfaction and reduce repeat inquiries.

---

### **Use Case 2: Financial Reconciliation & Anomaly Monitoring**

> 🎯 Goal: Ensure all rejected withdrawals have been properly refunded

- ✅ Implementation:
  1. Log in → Go to **Funds → Refund Records**  
  2. Set filters:
     - Refund Time: `01/02/2026 ~ 28/02/2026`  
     - Refund Reason: `Review Rejected`  
  3. Review all refund details  
  4. Summarize total amount and success rate  
  5. If any refund is missing, manually initiate the refund process  

> ✅ Outcome: Ensure financial accuracy and prevent fund stagnation.

---

### **Use Case 3: Identifying High-Risk Refund Patterns**

> 🎯 Goal: Prevent malicious refunds or fraud

- ✅ Implementation:
  1. Filter refunds with amount > 1,000 USD and reason = "Review Rejected"  
  2. Analyze these users’ transaction frequency, KYC status, and behavior history  
  3. If frequent large withdrawals are repeatedly rejected, flag as high-risk  
  4. Notify compliance team for investigation  

> ✅ Outcome: Early warning of potential risks, ensuring platform safety.

---

## **5. Best Practices**

| Scenario | Recommendation |
|---------|----------------|
| **Regular Audits** | Conduct full refund record reviews monthly to ensure no omissions or anomalies |
| **Anomaly Monitoring** | Monitor "Pending" statuses closely and follow up promptly |
| **Document Archiving** | Archive important transaction evidence and notes for future reference |
| **Access Control** | Restrict sensitive data access to authorized personnel only |
| **Automated Alerts** | Future versions will include automatic alerts when large numbers of refunds occur |

---

## **6. Frequently Asked Questions (FAQ)**

### **Q1: Why does some refund show "Pending"?**  
- ❌ Possible causes: System processing in progress, or manual intervention required  
- ✅ Solution: Check "Related Orders" to confirm original order status, contact technical support

---

### **Q2: Can I modify an existing refund amount?**  
- ❌ Not allowed.  
- ✅ For adjustments, use the **Fund Operations** module to submit a manual adjustment request.

---

### **Q3: How do I find a user’s full refund history?**  
- ✅ Method: Enter user ID or name (e.g., `16686`) in the search box to retrieve all related records.

---

### **Q4: How long are refund records retained?**  
- ✅ Retained permanently unless system policy specifies otherwise.  
- ⚠️ Recommendation: Keep indefinitely to meet regulatory requirements.

---

## **7. Summary**

The **Refund Records** module is a critical component of MIM CRM for achieving **safe fund rollback and user rights protection**. It not only provides full transaction audit capabilities but also supports collaboration across finance, operations, and customer service teams. Through scientific data management and efficient query mechanisms, organizations can build a robust financial system, delivering safe and trustworthy services to users.

✅ **Recommended Workflow**:  
1. Go to **Funds → Refund Records** → 2. Use filters to locate target order → 3. Click **View** → 4. Review details → 5. Analyze or export data

> 📌 All data is immutable and supports auditing and traceability, ensuring operational transparency and compliance.

---

**Version: v1.0**  
**Last Updated: February 2026**