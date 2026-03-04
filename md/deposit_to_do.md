# **Deposit To-do**  

## **1. Module Overview**

The **Deposit To-do** module serves as the **deposit review center** of MIM CRM, displaying all unverified user deposit applications. It supports filtering by order ID, payment method, status, time, and more, offering complete transaction details and approval tools to help administrators quickly decide whether to approve or reject deposits. Key features include:

- ✅ View all pending deposit records (e.g., cryptocurrencies, fiat currencies)  
- ✅ Approve or reject deposit requests manually  
- ✅ Record audit notes (admin-only visible / user-visible)  
- ✅ Real-time synchronization of wallet balance changes  
- ✅ Support for multiple payment channels (e.g., USDC, TRON, bank transfer)  

> 🔐 Access is restricted to **System Administrators** or **Finance Managers** only. All actions require manual intervention and are reflected immediately in user accounts.

---

## **2. Interface Layout**

### **Left Navigation Menu**
| Item | Function |
|------|----------|
| **Funds** | Enter the main funds management menu |
| - Pending Deposits | View all pending deposit requests |
| - Deposit Records | View historical deposit data |
| - Deposit to-do | View pending withdrawal requests |

---

### **Top Tab Bar**
| Tab | Description |
|-----|-------------|
| **Overview** | Return to the Funds module homepage |
| **Pending Deposits** | Current page |

---

### **Pending Deposits List View**
| Field | Description |
|-------|-------------|
| **Order ID** | Unique identifier (e.g., `P20260209202640974372`) – clickable to view details |
| **Deposit Status** | Current status: "Pending Review", "Approved", "Rejected" |
| **User** | Associated user ID or nickname (e.g., "Unknown 16670") |
| **Receiving Wallet** | Target wallet address (e.g., "BO Wallet 13342") |
| **Deposit Amount** | Actual amount to be credited (e.g., `+555.00 USD`) |
| **Post-Deposit Balance** | Estimated balance after approval (currently shown as "-" until calculated) |
| **Payment Amount** | Amount paid by user (e.g., `560.61 USDC`) |
| **User IP Address** | Client IP when submitting request (e.g., `171.223.184.189`) |
| **Submission Time** | Time when user initiated the request (e.g., `09/02/2026 20:26:41`) |
| **Action** | Contains **Review** button to start approval process |

> 💡 Example: Order ID `P20260209202640974372` shows status as "Pending Review", payment amount of 560.61 USDC, and target wallet BO Wallet 13342.

---

## **3. Core Feature Details**

### **1. View Deposit Details**

#### **Procedure**
1. In the **Pending Deposits** list, locate the target order (e.g., `P20260209202640974372`)  
2. Click the **Order ID** or **Review** button  
3. Enter the detail page, divided into sections:
   - **Basic Info**: Order ID, payment method (e.g., Crypto - Tron), receiving wallet, amount, etc.  
   - **Deposit Details**: Payment method, pre-deposit balance, post-deposit balance, transaction hash (e.g., `Tc...YwKuJ`)  
   - **Payer Account (Client Side)**: User’s wallet address, transaction time, type  
   - **Recipient Account (Our Side)**: Platform’s receiving wallet address  
   - **Original Details**: Raw transaction data (e.g., API parameters)  
   - **Offline Payment Documents** (if applicable): Uploaded files like bank transfer receipts  

> ✅ Example: When reviewing a USDC deposit, verify the transaction hash matches on-chain records and check for delays.

---

### **2. Perform Deposit Review**

#### **Procedure**
1. Click **Review**  
2. A pop-up window appears with two options:
   - 🔵 **Approve**: Credit funds to user wallet  
   - 🔴 **Reject**: Decline request; funds may be refunded if supported  
3. Enter review notes:
   - **Admin Notes (visible only to admins)**: Internal reason (e.g., "Transaction hash invalid")  
   - **User Notes (visible to users)**: Explanation for user (e.g., "Your transaction is being processed, please wait")  
4. Click **Confirm** to submit

> ⚠️ Note:  
> - Once approved, the system automatically updates the wallet balance  
> - If rejected, provide clear feedback to avoid customer complaints

---

### **3. Review Status & Impact**

| Action | System Response | User Experience |
|--------|------------------|------------------|
| **Approve** | Funds credited immediately; deposit record created; user notified | Receives "Deposit Successful" message; available balance increases |
| **Reject** | Marked as "Rejected"; no balance update; rejection notification sent | Receives "Deposit Failed" message with reason |

> ✅ Example: A user deposits 560.61 USDC; upon review, the transaction hash is found invalid. Select **Reject**, and note: "Please resubmit your transaction."

---

### **4. Multi-Condition Filtering & Search**

#### **Available Filters**
- **Submission Time From ~ To**: Filter by date range  
- **Deposit Status**: Choose "Pending", "Approved", "Rejected"  
- **Payment Channel**: e.g., "Crypto - Tron", "USDT", "Bank Transfer"  
- **Operator**: Specify reviewer  
- **Wallet**: Specify wallet number (e.g., 13342)  
- **ID/Name/Order ID Search**: Quickly locate specific user or order  

> ✅ Pro Tip: Combine "Payment Channel" and "Status" filters to prioritize high-priority crypto deposits.

---

## **4. Typical Use Cases**

### **Use Case 1: Processing Cryptocurrency Deposits**

> 🎯 Goal: Safely handle TRON-USDC deposits from users

- ✅ Implementation:
  1. Log in → Go to **Funds → Pending Deposits**  
  2. Filter by "Payment Channel": "Crypto - Tron"  
  3. Locate order `P20260209202640974372`  
  4. Click **Review** → Verify transaction hash on blockchain  
  5. Confirm valid → Select **Approve**, add note: "Transaction hash verified"  
  6. User wallet balance increases from 0 to 555.00 USD

> ✅ Outcome: Achieves dual verification (automated + manual), ensuring fund security.

---

### **Use Case 2: Rejecting Suspicious Transactions**

> 🎯 Goal: Prevent fraudulent deposits from entering the system

- ✅ Implementation:
  1. Identify a large deposit (e.g., 10,000 USDT) from a newly registered account  
  2. Click **Review** → Check IP address, transaction history  
  3. Find no prior trades and IP flagged as high-risk  
  4. Select **Reject**, and write in "User-visible" note: "For security reasons, your transaction has been paused. Please contact support."  
  5. Add internal note: "Suspected fraud, reported to risk team"

> ✅ Outcome: Effectively blocks potential threats, protecting platform assets.

---

### **Use Case 3: Handling High-Volume Holiday Deposits**

> 🎯 Goal: Manage surge of deposits during holidays (e.g., Chinese New Year)

- ✅ Implementation:
  1. Set up rotating shifts for daily reviews  
  2. Use "Submission Time" filter to focus on last 24 hours  
  3. Prioritize large or urgent transactions  
  4. Enable "Fast-Approval Mode" for recurring normal transactions (future version support)  
  5. Generate daily review reports for finance department

> ✅ Outcome: Improves processing efficiency, reduces backlog, enhances UX.

---

## **5. Best Practices**

| Scenario | Recommendation |
|---------|----------------|
| **Review Timeliness** | Aim to complete within 2 hours to minimize user waiting |
| **Note Standards** | Internal notes should be concise; external notes should be professional and friendly |
| **Risk Detection** | Combine IP, device fingerprint, and transaction frequency for anomaly detection |
| **Automation Support** | Future versions will include AI-assisted review to flag suspicious transactions |
| **Audit Trail** | All actions are logged for full traceability and compliance |

---

## **6. Frequently Asked Questions (FAQ)**

### **Q1: Why doesn't some deposit show a transaction hash?**  
- ❌ Possible causes: User didn’t fill it correctly or system failed to parse  
- ✅ Solution: Contact user to resubmit, or manually query blockchain

---

### **Q2: Will funds be automatically refunded after rejection?**  
- ❌ No automatic refund.  
- ✅ Requires manual refund process by finance team or depends on third-party gateway.

---

### **Q3: Can I set auto-approval rules?**  
- ❌ Not supported in current version.  
- ✅ Workaround: Implement a "whitelist" mechanism for trusted users (future version support).

---

### **Q4: When do users see their balance after approval?**  
- ✅ Real-time update.  
- Users can see the new balance immediately upon login without refresh.

---

## **7. Summary**

The **Pending Deposits** module is a critical component of MIM CRM for achieving **secure, efficient, and compliant fund inflow management**. It enhances both operational professionalism and user trust through transparent, auditable processes. By following structured review workflows and maintaining detailed logs, organizations can balance speed and safety, delivering reliable financial services.

✅ **Recommended Workflow**:  
1. Go to **Funds → Pending Deposits** → 2. Use filters to locate target order → 3. Click **Review** → 4. View details → 5. Select **Approve** or **Reject** → 6. Add notes → 7. Click **Confirm**

> 📌 All actions are recorded in system logs, ensuring full auditability, transparency, and regulatory readiness.

---

**Version: v1.0**  
**Last Updated: February 2026**