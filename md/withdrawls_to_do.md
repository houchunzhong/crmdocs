# **Withdrawls to-do**  


This document continues the consistent style of previous modules to provide a detailed explanation of the **Withdrawls to-do** sub-module within the **Funds** module in the MIM CRM system. Designed for operations and finance teams, this module is the core component for **user withdrawal review, fund outflow control, and compliance management**. It provides administrators with a centralized view and payment execution tools for all pending withdrawal requests, enabling efficient approval and disbursement while ensuring fund security and regulatory compliance.

---

## **1. Module Overview**

The **Withdrawls to-do** module serves as the **withdrawal review center** of MIM CRM, displaying all submitted but unprocessed user withdrawal requests. It supports filtering by order ID, payment method, status, time, and more, offering complete transaction details and payment tools to help administrators quickly decide whether to approve payments. Key features include:

- ✅ View all pending withdrawal records (e.g., bank transfers, cryptocurrencies)  
- ✅ Review and execute withdrawal payments  
- ✅ Record payment notes (admin-only visible / user-visible)  
- ✅ Real-time synchronization of wallet balance changes  
- ✅ Support for multiple payment channels (e.g., USD bank transfer, USDT TRON)  

> 🔐 Access is restricted to **System Administrators** or **Finance Managers** only. All actions require manual intervention and are reflected immediately in user accounts.

---

## **2. Interface Layout**

### **Left Navigation Menu**
| Item | Function |
|------|----------|
| **Funds** | Enter the main funds management menu |
| - Pending Deposits | View pending deposit requests |
| - Deposit Records | View historical deposit data |
| - Withdrawls to-do | View pending withdrawal requests |

---

### **Top Tab Bar**
| Tab | Description |
|-----|-------------|
| **Overview** | Return to the Funds module homepage |
| **Withdrawls to-do** | Current page |

---

### **Withdrawls to-do List View**
| Field | Description |
|-------|-------------|
| **Order ID** | Unique identifier (e.g., `WD20260209185654894638`) – clickable to view details |
| **Withdrawal Status** | Current status: "Approved", "Pending Payment", "Failed" |
| **User** | Associated user ID or nickname (e.g., "Unknown 16670") |
| **Source Wallet** | Wallet from which funds are withdrawn (e.g., "MT5&AQX Wallet 13341") |
| **Withdrawal Amount** | Actual amount to be withdrawn (e.g., `-200.00 USD`) |
| **Post-Withdrawal Balance** | Estimated balance after withdrawal (e.g., `2,800.00 USD`) |
| **Exchange Rate Converted Amount** | Final amount after currency conversion (e.g., `190.00 USD`) |
| **User IP Address** | Client IP when submitting request (e.g., `171.223.184.189`) |
| **Submission Time** | Time when user initiated the request (e.g., `09/02/2026 18:56:55`) |
| **Action** | Contains **Pay** button to initiate payment |

> 💡 Example: Order ID `WD20260209185654894638` shows status as "Approved", amount of -200.00 USD, and source wallet MT5&AQX Wallet 13341.

---

## **3. Core Feature Details**

### **1. View Withdrawal Details**

#### **Procedure**
1. In the **Withdrawls to-do** list, locate the target order (e.g., `WD20260209185654894638`)  
2. Click **View**  
3. Enter the detail page, divided into sections:
   - **Basic Info**: Order ID, payment method (e.g., Bank Transfer), source wallet, amount, etc.  
   - **Withdrawal Details**: User ID, name, withdrawal amount, exchange rate, converted amount, fee, user IP, submission time  
   - **Recipient Account (User's)**: Account type (e.g., Bank Card), recipient name, account number, bank name, address  
   - **Review Details**: Reviewer ID, reviewer name, review time, internal/external notes  
   - **Payment Details**: Payment ID, operator, payment time, completion time, processing duration  

> ✅ Example: When reviewing a bank transfer withdrawal, confirm if the recipient account is valid, KYC-compliant, and free of risk.

---

### **2. Execute Withdrawal Payment**

#### **Procedure**
1. Click **Pay**  
2. A confirmation window appears with:
   - Payment amount (e.g., 190.00 USD)  
   - Recipient account info (auto-filled)  
   - Payment channel (e.g., Bank Transfer)  
   - Optional payment note  
3. Enter payment note (e.g., "Successfully sent to banking system")  
4. Click **Confirm** to initiate payment

> ⚠️ Note:  
> - Once paid, the system automatically updates the wallet balance  
> - If failed, retry or contact payment gateway

---

### **3. Multi-Condition Filtering & Search**

#### **Available Filters**
- **Submission Time From ~ To**: Filter by date range  
- **Payment Channel**: e.g., "Bank Transfer", "USDT", "Crypto - Tron"  
- **Withdrawal Status**: Choose "Approved", "Pending Payment", "Failed"  
- **Operator**: Specify reviewer  
- **Source Wallet**: Specify wallet number (e.g., 13341)  
- **ID/Name/Order ID Search**: Quickly locate specific user or order  

> ✅ Pro Tip: Combine "Payment Channel" and "Status" filters to prioritize high-priority bank transfers.

---

## **4. Typical Use Cases**

### **Use Case 1: Processing Bank Transfer Withdrawals**

> 🎯 Goal: Safely handle user USD bank transfer withdrawals

- ✅ Implementation:
  1. Log in → Go to **Funds → Withdrawls to-do**  
  2. Filter by "Payment Channel": "Bank Transfer"  
  3. Locate order `WD20260209185654894638`  
  4. Click **View** → Verify recipient account is complete and KYC-compliant  
  5. Click **Pay** → Add note: "Sent to banking system"  
  6. Click **Confirm** → System deducts balance and logs payment

> ✅ Outcome: Achieves dual verification (automated + manual), ensuring fund security.

---

### **Use Case 2: Rejecting Suspicious Withdrawals**

> 🎯 Goal: Prevent fraudulent withdrawals from entering the system

- ✅ Implementation:
  1. Identify a large withdrawal (e.g., 50,000 USD) from a newly registered account  
  2. Click **View** → Check IP address, transaction history  
  3. Find no prior trades and IP flagged as high-risk  
  4. Do not pay; instead notify customer support team for investigation  
  5. Add note in "Review Remarks": "Suspected fraud, reported to risk team"

> ✅ Outcome: Effectively blocks potential threats, protecting platform assets.

---

### **Use Case 3: Handling High-Volume Holiday Withdrawals**

> 🎯 Goal: Manage surge of withdrawals during holidays (e.g., Chinese New Year)

- ✅ Implementation:
  1. Set up rotating shifts for daily payments  
  2. Use "Submission Time" filter to focus on last 24 hours  
  3. Prioritize large or urgent transactions  
  4. Enable "Fast-Payment Mode" for recurring normal transactions (future version support)  
  5. Generate daily payment reports for finance department

> ✅ Outcome: Improves processing efficiency, reduces backlog, enhances UX.

---

## **5. Best Practices**

| Scenario | Recommendation |
|---------|----------------|
| **Payment Timeliness** | Aim to complete within 2 hours to minimize user waiting |
| **Note Standards** | Internal notes should be concise; external notes should be professional and friendly |
| **Risk Detection** | Combine IP, device fingerprint, and transaction frequency for anomaly detection |
| **Automation Support** | Future versions will include AI-assisted payment to flag suspicious transactions |
| **Audit Trail** | All actions are logged for full traceability and compliance |

---

## **6. Frequently Asked Questions (FAQ)**

### **Q1: Why doesn't some withdrawal show a recipient account?**  
- ❌ Possible causes: User didn’t fill it correctly or system failed to parse  
- ✅ Solution: Contact user to resubmit, or manually verify account info

---

### **Q2: Can I retry a failed payment?**  
- ✅ Yes.  
- ✅ Method: Click **Pay** again, or manually initiate refund process via finance team.

---

### **Q3: Can I set auto-payment rules?**  
- ❌ Not supported in current version.  
- ✅ Workaround: Implement a "whitelist" mechanism for trusted users (future version support).

---

### **Q4: When do users see their balance change after payment?**  
- ✅ Real-time update.  
- Users can see the reduced balance immediately upon login, though actual bank arrival depends on processing speed.

---

## **7. Summary**

The **Withdrawls to-do** module is a critical component of MIM CRM for achieving **secure, efficient, and compliant fund outflow management**. It enhances both operational professionalism and user trust through transparent, auditable processes. By following structured review workflows and maintaining detailed logs, organizations can balance speed and safety, delivering reliable financial services.

✅ **Recommended Workflow**:  
1. Go to **Funds → Withdrawls to-do** → 2. Use filters to locate target order → 3. Click **View** → 4. Review details → 5. Click **Pay** → 6. Add note → 7. Click **Confirm**

> 📌 All actions are recorded in system logs, ensuring full auditability, transparency, and regulatory readiness.

---

**Version: v1.0**  
**Last Updated: February 2026**