# **Funds Module Configuration and User Guide**  
**My Investment Markets (MIM) CRM System**

This guide provides a comprehensive overview of the **Funds Module** in the MIM CRM system, detailing its configuration, functionality, and operational procedures. It is designed for administrators, financial officers, and operations teams responsible for managing client deposits, withdrawals, transfers, and fund verification.

---

## **1. Module Overview**

The **Funds Module** is a core financial component of the MIM CRM, handling all user-related monetary transactions. It includes the following sub-functions:

- ✅ **Deposits To-do**: Pending deposit requests awaiting confirmation  
- ✅ **Deposit Records**: History of completed deposits  
- ✅ **Withdrawals To-do**: Withdrawal requests pending approval  
- ✅ **Withdrawal Records**: Completed withdrawal history  
- ✅ **Transfer Records**: Internal fund transfers between wallets/accounts  
- ✅ **Refund Records**: Refund processing for failed or erroneous transactions  
- ✅ **Funds Operations**: Manual adjustments to balances (e.g., credits, freezes)

> 🔐 All fund operations are subject to role-based access control. Only authorized personnel (e.g., finance staff, admins) can perform actions.

---

## **2. Interface Layout Explanation**

### **Left Sidebar Navigation**
| Item | Function |
|------|----------|
| **Deposits To-do (153)** | Displays pending deposit applications |
| **Deposit Records** | View all confirmed deposit history |
| **Withdrawals To-do (247)** | Shows pending withdrawal requests |
| **Withdrawal Records** | View processed withdrawal details |
| **Transfer Records** | Query internal fund transfers |
| **Refund Records** | Handle refunds due to failed or incorrect transactions |
| **Funds Operations** | Manually add or adjust funds (e.g., credit, freeze, unfreeze) |

---

### **Top Filtering Toolbar**
Provides multi-dimensional filters to quickly locate specific transactions:

| Field | Description |
|-------|-------------|
| **Submission Time From ～ To** | Filter by date range |
| **Deposit Status** | Options: `Approval Passed`, `Pending Collection`, `Rejected` |
| **Payment Gateway** | E.g., `Bank Transfer`, `Credit Card`, `Wallet`, `Offline` |
| **Operator** | Specify which operator handled the transaction |
| **Wallet** | Select wallet type (e.g., `MT5&AQX Wallet`, `BO Wallet`) |
| **ID/Name/Order Search** | Supports fuzzy search by user ID, name, or order number |

---

## **3. Core Function Details**

### **1. Deposits To-do (Pending Deposits)**

#### **Function Description**
Displays all user-submitted deposits that have passed initial approval but are still awaiting final confirmation (i.e., receipt of funds).

#### **Field Descriptions**
| Field | Description |
|-------|-------------|
| **Order** | Unique transaction ID (e.g., `P20251219171233274679`) |
| **Deposit Status** | Current status:<br>🟢 `Approval Passed`<br>🟡 `Pending Collection` (awaiting bank settlement) |
| **User** | Username + User ID (e.g., `tt 17804`) |
| **Credited Wallet** | Target wallet (e.g., `MT5&AQX Wallet`) |
| **Deposit Amount** | Deposit amount (in green, e.g., `+1,000.00 USD`) |
| **Wallet Balance After** | Estimated balance after deposit (shown as `-` if not yet settled) |
| **Payment Amount** | Actual payment amount (including fees) |
| **Payment Currency** | E.g., USD, IDR, GBP |
| **User Submission IP** | Client's IP address when submitting request (for security audit) |
| **User Submission Time** | Timestamp of submission (e.g., `19/12/2025 17:12:33`) |
| **Action** | Button: **Confirm Receipt** |

#### **Operation Flow**
1. Verify payment proof (bank statement, third-party receipt).
2. Click **"Confirm Receipt"**.
3. System automatically updates wallet balance and changes status to "Confirmed".
4. If funds do not arrive, you may ignore or mark as "Rejected".

> ⚠️ Note: Once confirmed, funds are credited to the user account and cannot be reversed.

---

### **2. Deposit Records (Deposit History)**

#### **Function Description**
View all completed deposit transactions for auditing, reconciliation, and reporting purposes.

#### **Features**
- Automatically logs every successful deposit with timestamp, amount, channel, etc.
- Supports filtering by time, user, wallet type, etc.
- Exportable to Excel for financial reconciliation.

---

### **3. Withdrawals To-do (Pending Withdrawals)**

#### **Function Description**
Displays user-submitted withdrawal requests that require administrator approval before processing.

#### **Operation Flow**
1. Review withdrawal request (ensure sufficient balance, meets minimum threshold, etc.).
2. Click **"Approve"** or **"Reject"**.
3. Upon approval, system initiates payment process (e.g., bank transfer, wallet payout).
4. Rejection requires reason input and notification to user.

> 💡 Recommended: Enable dual-approval for large withdrawals (e.g., > $10,000).

---

### **4. Withdrawal Records (Withdrawal History)**

#### **Function Description**
Tracks all processed withdrawal transactions for traceability and compliance audits.

#### **Fields Include**
- Order ID, User, Amount, Payment Method, Processing Time, Status (Success/Failure), etc.
- Supports export to Excel for financial reporting.

---

### **5. Transfer Records (Internal Transfers)**

#### **Function Description**
Monitors fund transfers between different wallets or accounts within the same user or across users.

#### **Common Use Cases**
- Moving funds from MT5 Wallet to BO Wallet
- IB transferring commissions to personal account
- Internal fund reallocation

#### **Fields**
- Transfer direction (From → To)
- Amount
- Time
- Operator
- Status (Success/Failure)

---

### **6. Refund Records (Refund Processing)**

#### **Function Description**
Handles refunds triggered by failed transactions, duplicate charges, or errors.

#### **Use Cases**
- User accidentally made duplicate payment
- Third-party gateway failed to deduct
- Refund issued due to dispute resolution

---

### **7. Funds Operations (Manual Fund Adjustments)**

#### **Function Description**
Allows administrators to manually adjust user account balances for exceptional cases.

#### **Operation Types**
| Type | Description |
|------|-------------|
| **Increase Balance** | Credit user for compensation, rewards, etc. |
| **Decrease Balance** | Deduct funds for penalties, corrections |
| **Freeze/Unfreeze** | Control high-risk accounts |
| **Transfer to Other Wallets** | Internal fund allocation |

> ⚠️ This feature requires special permissions and logs all actions for accountability.

---

## **4. Best Practices**

| Item | Recommendation |
|------|----------------|
| **Access Control** | Grant "Funds Operations" access only to finance managers or above |
| **Dual Approval** | Require two-level review for large deposits/withdrawals |
| **Regular Reconciliation** | Perform daily/weekly reconciliation of fund records with bank statements |
| **IP Monitoring** | Monitor suspicious IPs (e.g., frequent changes) for fraud detection |
| **Automated Alerts** | Set up email/in-app notifications to remind admins of pending tasks |

---

## **5. Frequently Asked Questions (FAQ)**

### **Q1: What’s the difference between "Approval Passed" and "Pending Collection"?**
- ✅ **Approval Passed**: The system has verified the information; waiting for actual funds.
- 🟡 **Pending Collection**: Funds have not yet been received; manual follow-up required.

### **Q2: Can I edit a confirmed deposit record?**
- ❌ No direct editing is allowed. If an error occurs, contact technical support for reversal or correction.

### **Q3: A user submitted a withdrawal but didn’t receive the funds—what should I do?**
- Check payment gateway status, bank processing time, and fee deductions.
- If delayed beyond expected time, check "Withdrawal Records" for failure reasons and re-initiate if needed.

---

## **6. Summary**

The **Funds Module** in MIM CRM offers a full-featured, secure, and auditable solution for managing all aspects of user financial transactions—from initial deposit to final withdrawal. With proper configuration and standardized workflows, organizations can significantly improve financial efficiency, reduce operational risk, and meet regulatory requirements.

✅ **Recommended Workflow**:
1. Review → 2. Confirm Receipt → 3. Update Status → 4. Export Record → 5. Archive for Audit

> 📌 Always comply with company financial policies and Anti-Money Laundering (AML) regulations during operations.

---

**Version: v1.0**  
**Last Updated: April 2025**