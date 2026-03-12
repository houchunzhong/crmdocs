# **All Withdrawal Accounts**  

## **1. Module Overview**

The **All Withdrawal Accounts** module is the **master ledger of fund movements** in MIM CRM, displaying all user withdrawal account information and review statuses. It supports multi-dimensional filtering by user ID, beneficiary name, currency, country, and more, and provides one-click navigation to user profiles and specific withdrawal records for in-depth analysis.

### ✅ Core Value:
- Enables global visualization of withdrawal data
- Supports historical tracing and trend analysis
- Provides complete audit evidence chain
- Ensures transparency in fund security and compliance

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
|   - Pending Withdrawal Accounts (0) | View pending withdrawals |
|   - **All Withdrawal Accounts** | Current page |

---

### **All Withdrawal Accounts List View**
| Field | Description |
|-------|-------------|
| **User ID** | Unique identifier; clickable to open user profile |
| **Review Status** | Shows current withdrawal result (e.g., "Approved", "Rejected") |
| **Beneficiary Name** | Name of the recipient (may differ from user name) |
| **Currency** | Withdrawal currency (e.g., USD, EUR, BTC, USDT) |
| **Type** | Withdrawal method (e.g., Bank Transfer, Crypto Wallet) |
| **Account/Wallet Address** | Specific bank account or crypto wallet address |
| **Country** | Beneficiary’s country |
| **Submission Time** | When user submitted the request |
| **Action** | Contains **View** button to access withdrawal details for review |

> 💡 Example: Displays withdrawal request from user `16672`, beneficiary `-` (not filled), currency USDT, type "Crypto Wallet", submitted at `10/02/2026 11:10:35`.

---

## **3. Core Features**

### **1. Multi-Condition Filtering & Smart Search**

#### **Available Filters**
| Condition | Description |
|---------|-------------|
| **User ID/Name/Phone/Email Search** | Quickly locate specific user’s withdrawal history |

> ✅ Pro Tips:
> - Use "User ID" to find all withdrawal records of a high-net-worth client.
> - Combine "Currency = USDT" + "Country = Hong Kong" to detect potential cross-border crypto transfers.

---

### **2. One-Click Navigation to Withdrawal Details**

#### **Workflow**
1. Find target withdrawal request (e.g., `16672`) in the **All Withdrawal Accounts** list
2. Click **View**
3. Navigate directly to the **Withdrawal Details Page**
4. Review full information, including:
   - Withdrawal amount
   - Associated trading account
   - First-time withdrawal flag
   - Risk score (if available)
5. Switch tabs to view:
   - **Current Withdrawal Account**: Currently processing withdrawal
   - **All Withdrawals for This User**: Full history of withdrawals
   - **Review History**: Audit log of past reviews

> ✅ Benefits:
> - Reduces page switching, improves analysis efficiency
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

### **4. Review Status Visualization & Trend Analysis**

#### **Key Features**
- **Color-coded status indicators**:
  - ✅ Green: "Approved"
  - ❌ Red: "Rejected"
- **Real-time count display**: Top bar shows number of withdrawals per status (e.g., "Approved: 87")
- **Supports pagination**: Up to 10 entries per page, with navigation controls

> ✅ Outcome: Visually reflects platform-wide fund flow health and compliance level.

---

## **4. Typical Use Cases**

### **Use Case 1: Finance Manager Conducting Monthly Fund Audit**

> 🎯 Goal: Ensure monthly withdrawal totals match accounting records, preventing omissions or errors

- ✅ Implementation:
  1. Log in → Go to **Users → KYC Review → All Withdrawal Accounts**
  2. Set filters:
     - Review Status: `Approved`
     - Submission Time: `01/02/2026 ~ 28/02/2026`
     - Currency: USD, EUR, USDT
  3. View matching requests (e.g., 120)
  4. Click **Download to Excel** to export list
  5. Compare with financial system records
  6. Discover 3 entries delayed → Add manually
  7. Generate monthly fund report and submit to management

> ✅ Outcome: Ensure financial accuracy and meet internal audit requirements.

---

### **Use Case 2: Compliance Officer Monitoring Suspicious Withdrawals**

> 🎯 Goal: Identify potential money laundering or fund splitting behavior

- ✅ Implementation:
  1. Go to **Users → KYC Review → All Withdrawal Accounts**
  2. Set filters:
     - Country: China
     - Currency: USDT
     - Submission Time: `01/01/2026 ~ 31/01/2026`
  3. View matching requests (e.g., 15)
  4. Notice user `16666` making multiple small withdrawals ($100 each) in short intervals
  5. Click **View** → Open details
  6. Detect frequently changing wallet addresses → Flag as "fund splitting"
  7. Mark as "High-Risk User" and report to AML team
  8. Initiate investigation process

> ✅ Outcome: Timely detect suspicious transactions and reduce regulatory risk.

---

### **Use Case 3: System Administrator Troubleshooting Technical Issues**

> 🎯 Goal: Confirm if withdrawals failed or system errors occurred

- ✅ Implementation:
  1. Receive user feedback: "Withdrawal not received" → Go to **All Withdrawal Accounts**
  2. Search User ID `16693`
  3. Check withdrawal history:
     - First submission: Approved but no settlement triggered
     - Second submission: Approved, successfully credited
  4. Determine system delay → Contact technical support
  5. Identify payment gateway caching issue → Optimize configuration
  6. Send explanatory email to user with apology

> ✅ Outcome: Rapidly identify and resolve technical issues, improving user experience.

---

## **5. Best Practices**

| Scenario | Recommendation |
|---------|----------------|
| **Data Security** | Do not save search records on public computers to prevent leaks |
| **Permission Control** | Restrict access to authorized roles only |
| **Input Standardization** | Encourage users to always provide full contact details (with country code) |
| **Error Handling** | If search fails repeatedly, contact technical support |

---

## **6. Frequently Asked Questions (FAQ)**

### **Q1: Why isn’t a withdrawal request showing up in the "All Withdrawal Accounts" list?**  
- ❌ Possible causes: Not yet submitted, deleted, or system sync delay  
- ✅ Solution: Check if user is registered, or contact support for confirmation

---

### **Q2: Can I approve multiple withdrawals at once?**  
- ❌ Not supported in current version; must review individually  
- ✅ Future version will include **batch approve/reject** functionality

---

### **Q3: How to view a user’s full withdrawal history?**  
- ✅ Go to **All Withdrawal Accounts** → Search User ID → Click **View** → Switch to **All Withdrawals for This User** tab

---

### **Q4: Can a user resubmit after being rejected?**  
- ✅ Yes. Users can re-submit after correcting information, and the request will re-enter the review process.

---

## **7. Summary**

The **All Withdrawal Accounts** module is a critical component of MIM CRM for achieving **full transparency in fund flow lifecycle management**. It provides a clear historical view and supports efficient analysis and export functions, helping teams meet regulatory requirements while optimizing customer service and risk management.

✅ **Recommended Workflow**:  
1. Go to **Users → KYC Review → All Withdrawal Accounts** → 2. Filter target requests → 3. Click **View** → 4. Analyze details and review history → 5. Perform necessary actions

> 📌 All operations are permission-controlled, ensuring data security and compliance.

---

**Version: v1.0**  
**Last Updated: February 2026**