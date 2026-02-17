# **User Relationship Tree**  

## **1. Module Overview**

The **User Relationship Tree** module acts as the **organizational visualization hub** of MIM CRM. It presents user hierarchies in an interactive tree diagram, where each node represents a user and parent-child links indicate referral or agency relationships. Beyond structure, it integrates key financial and KYC (Know Your Customer) verification data to enable:

- ✅ User relationship tracing  
- ✅ IB performance evaluation  
- ✅ KYC status tracking  
- ✅ Transaction behavior monitoring  

  - 🧾 **Total Assets**: Available + frozen balance  
  - 💵 **Available Balance**: Funds ready for trading |
| **User Type** |  
> 🔍 All data is synchronized in real time. Users can be quickly located by ID, name, phone number, or email.

---

## **2. Interface Layout**

### **Left Navigation Menu**
| Item | Function |
|------|----------|
| **User Search** | Quickly find a specific user |
| **User List** | View basic information of all users |
| **User Relationship Tree** | Visualize hierarchical user structure (core feature) |
| **CFD User List** | Display users on the CFD platform |
| **BO User List** | Display users on the BO platform |

---

### **Top Tab Bar**
| Tab | Description |
|-----|-------------|
| **Overview** | Return to parent page |
| **User Relationship Tree** | Current page |
| **User – [Name]** | Enter a specific user’s detail page |

---

## **3. Core Feature Details**

### **1. Main Relationship Tree View**

#### **Function Description**  
Displays user referral/agency relationships in a collapsible tree structure. Each node represents a user, with parent-child links showing direct reporting lines. Sub-trees can be expanded or collapsed for focused inspection.

#### **Field Definitions**
| Field | Description |
|-------|-------------|
| **Avatar / Icon** | User profile picture; special indicators include:  
  - 🟨 **Red star**: High-risk user (e.g., KYC rejected)  
  - 🟩 **Green check**: Verified account  
  - 🔴 **Red exclamation**: Rejected or anomalous status |
| **Username / Full Name** | Display name (supports multilingual input: Chinese, English, Korean, etc.) |
| **ID** | Unique system user ID (e.g., `16672`) |
| **KYC Status Icon** |  
  - ✅ **Green ✓**: Verified  
  - ⚠️ **Orange !**: Pending review  
  - ❌ **Red !**: Rejected |
| **Asset Panel** | Real-time financial snapshot:  
  - 💰 **Total Deposits**: Cumulative funding  
  - 💸 **Total Withdrawals**: Cumulative withdrawals  
  - 🏢 **IB**: Introducing Broker  
  - 👤 **Verified Client**: Fully verified customer  
  - 🆘 **New Client**: Recently registered  
  - 🧑‍💼 **Client**: Standard customer |
| **Number of Subordinates** | Count of directly referred users (e.g., “27” means 27 direct referrals) |
| **View Button** | Click to open the user’s **profile detail page** |

#### **Interactive Controls**
- 🔎 **Search Bar**: Global search by `ID`, `name`, `phone`, or `email`.
- ▼ **Expand/Collapse**: Click the triangle icon to show/hide a user’s subtree.
- 📊 **Hierarchy Navigation**: Start from top-level IBs and drill down through their networks.

> 💡 Example: An IB with 30+ subordinates can be instantly identified for performance review or support prioritization.

---

### **2. User Detail Page (User Profile)**

#### **Function Description**  
Clicking **“View”** on any user opens their full profile, providing comprehensive access to personal info, account status, transaction history, and audit logs.

#### **Page Structure**
##### **Left Information Panel**
| Field | Description |
|-------|-------------|
| **Avatar & Name** | Profile picture and full name |
| **ID & Role** | User ID and type (e.g., IB / Verified Client) |
| **Total Deposits / Withdrawals** | Lifetime funding activity |
| **Total Assets / Available Balance** | Real-time asset summary |
| **Nationality / Residence** | Geographic details |
| **Registration Time** | Account creation timestamp |
| **Contact Info** | Phone and email, with verification badges (✅ = verified) |

##### **Right Content Area (Tabbed Interface)**
| Tab | Content |
|-----|--------|
| **User Profile** | Edit name, nationality, DOB, email, phone, etc. |
| **User Assets** | View balances by currency and deposit/withdrawal history |
| **Trading Accounts** | List linked MT5, BO, AQX accounts |
| **Withdrawal Accounts** | View bound bank accounts or crypto wallets |
| **Logs** | Record of logins, edits, fund movements, etc. |

#### **Key Fields**
| Field | Description |
|-------|-------------|
| **Two-Factor Authentication (2FA)** | Indicates if Google Authenticator or similar is enabled |
| **Referrer ID / Name** | Identifies the user who referred this account (i.e., superior) |
| **Number of Subordinates** | Total direct referrals |
| **Referral Code** | Unique code generated for promotions |
| **Referral Link** | Copyable URL for sharing |

> ✅ Example: In Akina Akiyama’s profile, you can see she was referred by User ID:1 and has 6 subordinates—typical of an active IB.

---

### **3. KYC Verification Status Indicators**

#### **Function Description**  
Color-coded icons provide instant visibility into KYC review outcomes, enabling rapid risk assessment.

| Icon | Meaning | Risk Level |
|------|--------|------------|
| 🟩 **Green ✓** | Verified | ✅ Low |
| ⚠️ **Orange !** | Pending | ⚠️ Medium |
| ❌ **Red !** | Rejected | 🔴 High |

> 🔍 Note: Red-exclamation users may involve fake documents, mismatched IDs, or blacklist matches—requiring immediate compliance review.

---

### **4. Agency Hierarchy & Commission Logic (Implicit Functionality)**

Though not displayed directly, the **User Relationship Tree** underpins **commission calculations**. The system applies rules such as:

- **Superior IBs** earn a percentage (e.g., 1%) of their subordinates’ **deposits**
- **Multi-tier commissions**: Some plans support 2nd- or 3rd-level rebates (configured in the “Tiers & Commissions” module)
- **Settlement cycles**: Typically daily/weekly/monthly, paid to the IB’s withdrawal account

> 💡 Example: If IB Akina Akiyama’s subordinate deposits $1,000, she may receive $10 in commission (at 1% rate).

---

## **4. Best Practices**

| Scenario | Recommendation |
|--------|----------------|
| **New Registration** | Verify the referrer’s validity in the tree to prevent fraudulent referrals |
| **KYC Review** | Prioritize orange-exclamation users to reduce compliance exposure |
| **IB Performance Review** | Monitor “Subordinates” count and “Total Deposits” to assess recruitment effectiveness |
| **Risk Control** | Immediately suspend red-exclamation users and alert legal/compliance teams |
| **Client Engagement** | Use profile data to personalize communication and service |

---

## **5. Frequently Asked Questions (FAQ)**

### **Q1: How do I find a user’s referrer?**  
- In the **User Relationship Tree**, click the user → go to their detail page → check **“Referrer ID”** and **“Referrer Name”**.

### **Q2: Why do some users have no subordinates?**  
- They are end clients (not IBs), or haven’t successfully referred anyone yet.

### **Q3: Can I export the relationship tree?**  
- ❌ Not directly. However, you can export the **User List** as CSV and reconstruct the hierarchy in Excel.

### **Q4: Is bulk user management supported?**  
- ❌ No. Use the **User List** for filtering, then process users individually.

### **Q5: Does the tree update automatically?**  
- ✅ Yes. It refreshes in real time upon registration, referral, or status changes.

---

## **6. Summary**

The **User Relationship Tree** transforms complex referral networks into an intuitive visual hierarchy, significantly enhancing client management efficiency and regulatory compliance. By integrating KYC status, financial data, and agency links, administrators can not only locate users instantly but also analyze IB ecosystems, optimize incentive structures, and enforce risk controls.

✅ **Recommended Workflow**:  
1. Use search to locate a user → 2. Inspect their position in the tree → 3. Open profile for verification → 4. Take action based on status (approve, contact, suspend)

> 📌 All actions are logged in the system audit trail, ensuring full traceability and accountability.

---

**Version: v1.0**  
**Last Updated: Febuary 2026**