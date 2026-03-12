# **Pending Withdrawal Accounts**  

## **1. Module Overview**

The **Pending Withdrawal Accounts** module is the **withdrawal review center** of MIM CRM, used to display all withdrawal requests currently in "pending review" status. It supports rapid filtering by user ID, beneficiary name, submission time, and more, and provides one-click navigation to user profiles for comprehensive assessment of withdrawal legitimacy and authenticity.

### ✅ Core Value:
- Standardizes withdrawal processes
- Provides clear visibility into pending tasks to prevent omissions
- Supports batch operations and data export
- Ensures platform fund security and compliance

> 🔐 Access is restricted to **System Administrators**, **Finance Managers**, and **Compliance Officers** only. Regular clients and IBs cannot access this page.

---

## **2. Interface Layout**

### **Left Navigation Menu**
| Item | Function |
|------|----------|
| **Users** | Enter user management main menu |
| - KYC Review | Expand submenu |
|   - Pending Review Users (0) | View pending users |
|   - All Users | View all users |
|   - **Pending Withdrawal Accounts (0)** | Current page |

---

### **Pending Withdrawal Accounts List View**
| Field | Description |
|-------|-------------|
| **User ID** | Unique identifier; clickable to open user profile |
| **Review Status** | Shows current withdrawal status (e.g., "Pending", "Approved", "Rejected") |
| **Beneficiary Name** | Name of the recipient (may differ from user name) |
| **Currency** | Withdrawal currency (e.g., USD, EUR, BTC) |
| **Type** | Withdrawal method (e.g., Bank Transfer, Crypto Wallet) |
| **Account/Wallet Address** | Specific bank account or crypto wallet address |
| **Country** | Beneficiary’s country |
| **Submission Time** | When user submitted the request |
| **Action** | Contains **View** button to access withdrawal details for review |

> 💡 Example: Displays withdrawal request from user `16693`, beneficiary `Matthew Lee`, currency USD, type Bank Transfer, submitted at `10/02/2026 14:45:15`.

---

## **3. Core Features**

### **1. Multi-Condition Filtering & Search**

#### **Available Filters**
| Condition | Description |
|---------|-------------|
| **User ID/Name/Phone/Email Search** | Quickly locate specific user’s withdrawal requests |

> ✅ Pro Tips:
> - Use "User ID" to find all withdrawal records of a high-net-worth client.
> - Combine "Beneficiary Name" + "Country" to detect potential cross-border fund transfers.

---

### **2. One-Click Navigation to Withdrawal Details**

#### **Workflow**
1. Find target withdrawal request (e.g., `16693`) in the **Pending Withdrawal Accounts** list
2. Click **View**
3. Navigate directly to the **Withdrawal Details Page**
4. Review full information, including:
   - Withdrawal amount
   - Associated trading account
   - First-time withdrawal flag
   - Risk score (if available)
5. Perform review action: **Approve** or **Reject**

> ✅ Benefits:
> - Reduces page switching, improves efficiency
> - All actions are logged for audit trail

---

### **3. Data Export & Report Generation**

#### **Function Description**
- Supports exporting current filtered results to Excel
- Export includes: User ID, Review Status, Beneficiary Name, Currency, Type, Account Address, Country, Submission Time
- Does not include sensitive materials (e.g., ID photos)

> ⚠️ Notes:
> - Only accessible to roles with `withdrawal:export:excel` permission
> - Recommended to export regularly as financial audit evidence

---

### **4. Automatic Reminder Mechanism (Future Version)**

> ✅ Planned Feature:
> - Send internal alerts for withdrawals awaiting review over 72 hours
> - Support priority tagging (e.g., "High Risk", "Urgent")

---

## **4. Typical Use Cases**

### **Use Case 1: Finance Manager Conducting Daily Withdrawal Reviews**

> 🎯 Goal: Ensure every withdrawal is legal and compliant, preventing fund outflow

- ✅ Implementation:
  1. Log in → Go to **Users → KYC Review → Pending Withdrawal Accounts**
  2. View all pending requests (e.g., 5)
  3. Click **View** to open `16693`’s withdrawal details
  4. Check:
     - Is the amount reasonable? (e.g., > $10,000 requires extra approval)
     - Does beneficiary name match user?
     - Is the account known and valid?
     - Are there abnormal patterns? (e.g., frequent small withdrawals)
  5. If complete and low-risk → Click **Approve** → Funds enter settlement
  6. If suspicious → Click **Reject** and enter reason → User receives notification to resubmit

> ✅ Outcome: Protect platform funds and reduce fraud risk.

---

### **Use Case 2: Compliance Officer Monitoring Cross-Border Flows**

> 🎯 Goal: Identify potential money laundering or fund transfer activities

- ✅ Implementation:
  1. Go to **Users → KYC Review → Pending Withdrawal Accounts**
  2. Set filters:
     - Country: China
     - Currency: USD
     - Submission Time: `01/02/2026 ~ 28/02/2026`
  3. View matching requests (e.g., 8)
  4. Notice 3 from same user, total $15,000
  5. Click **View** → Open details
  6. Find beneficiary name differs from user, address in offshore financial center
  7. Flag as high-risk → Click **Reject** and mark as "Suspicious Transaction"
  8. Initiate AML reporting process

> ✅ Outcome: Timely block potential violations and meet regulatory requirements.

---

### **Use Case 3: System Administrator Investigating Abnormal Submissions**

> 🎯 Goal: Detect potential fraud or technical issues

- ✅ Implementation:
  1. Notice repeated failed submissions → Go to **Pending Withdrawal Accounts**
  2. Search User ID `16684`
  3. Check withdrawal history:
     - First: Incorrect beneficiary name
     - Second: Invalid wallet address
     - Third: Amount exceeds limit
  4. Determine malicious attempt → Click **View** → Open details
  5. Discover IP frequently changes → Tag as "High-Risk User"
  6. Trigger anti-fraud process: Freeze account, notify legal team

> ✅ Outcome: Proactively block threats and protect platform security.

---

## **5. Best Practices**

| Scenario | Recommendation |
|---------|----------------|
| **Review Timeliness** | Aim to complete reviews within 24 hours to maintain user experience |
| **Data Completeness** | Strictly verify beneficiary information and account validity |
| **Rejection Reason** | Always provide clear rejection reasons to help users correct errors |
| **Permission Control** | Restrict review actions to finance and compliance teams only |
| **Audit Trail** | Ensure all review actions are logged for traceability |

---

## **6. Frequently Asked Questions (FAQ)**

### **Q1: Why isn’t a withdrawal request showing up in the "Pending Withdrawal Accounts" list?**  
- ❌ Possible causes: Already approved, rejected, or not submitted  
- ✅ Solution: Check withdrawal status, or go to **All Withdrawal Accounts** list

---

### **Q2: Can I approve multiple withdrawals at once?**  
- ❌ Not supported in current version; must review individually  
- ✅ Future version will include **batch approve/reject** functionality

---

### **Q3: How long does it take for funds to arrive after approval?**  
- ✅ Typically 1–3 business days after approval, depending on payment method and bank processing speed.

---

### **Q4: How to view historical withdrawal records?**  
- ✅ Go to **Users → KYC Review → All Withdrawal Accounts**, filter by "Approved" or "Rejected" status.

---

## **7. Summary**

The **Pending Withdrawal Accounts** module is a critical component of MIM CRM for achieving **fund security and compliance automation**. It provides a clear task dashboard and supports efficient review workflows, helping teams meet regulatory requirements while maintaining user experience. Whether for daily reviews, cross-border monitoring, or anomaly detection, this module enables streamlined operations.

✅ **Recommended Workflow**:  
1. Go to **Users → KYC Review → Pending Withdrawal Accounts** → 2. Filter target requests → 3. Click **View** → 4. Review details → 5. Select **Approve** or **Reject**

> 📌 All operations are permission-controlled, ensuring data security and compliance.

---

**Version: v1.0**  
**Last Updated: February 2026**