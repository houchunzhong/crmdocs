# **1. User List Module**

This module serves as a centralized dashboard for all registered users, enabling quick filtering and bulk management.

### **Key Features**

- **Global Search**: A top search bar supports multi-field fuzzy matching by `ID / Name / Mobile / Email`.
- **User Status Indicators**:
  - ✅ **Green checkmark**: Indicates KYC-verified users (`Verified Client`)
  - ⚠️ **Orange warning icon**: Indicates unverified or pending-review status
- **Financial Summary** (displayed per row):
  - 💵 **Account Balance (green)**: Current available funds
  - 🔴 **Trading Exposure (red)**: Total open position risk or liabilities
  - 🧾 **Total Assets (gold)**: Net worth or total equity
- **User Type Tags**:
  - `Client`: Standard customer
  - `Verified Client`: KYC-compliant customer
  - `Ordinary`: Basic user tier
- **Referral Count**: Shows the number of direct referrals under the user (e.g., `0` means no subordinates)
- **Action Button**: “View” on each row opens the detailed user profile

---

## **2. User Relationship Tree Module**

Visualizes referral and hierarchical relationships among users—essential for tracking IB (Introducing Broker) networks and agent structures.

### **Core Capabilities**

- **Tree Structure Layout**: Displays parent-child referral chains with expand/collapse functionality.
- **Country Flags**: Nationality icons next to usernames enable instant geographic identification.
- **Real-Time Data Sync**: Each node shows:
  - Total Deposit, Total Withdrawal, Total Assets, Available Balance
  - Account status and user level
- **Clear Referral Mapping**: Instantly reveals who reports to whom—critical for commission allocation and performance analysis.

---

## **3. User Detail Page (User Profile)**

Clicking any user opens their full profile for comprehensive review and administrative control.

### **Page Layout**

#### **Left Panel (Summary Snapshot)**

- Avatar and full name
- User ID and level (e.g., `Verified Client`, `Senior IB`)
- Key financial metrics:
  - Total Deposit
  - Total Withdrawal
  - Total Asset
  - Available Balance
- Basic Info:
  - Nationality, Residence, Registration Time
  - Verified mobile & email (with status badges)
  - Contact icons (phone, email)

#### **Right Panel (Editable Details)**

##### **User Profile**

| Field | Example | Editable? |
|------|--------|----------|
| First Name | Akina | ✅ Yes |
| Middle Name | - | ✅ Yes |
| Last Name | - | ✅ Yes |
| Full Name | Akina | ✅ Yes |
| Nationality | Unknown | ✅ Yes |
| Residence | Australia | ✅ Yes |
| Date of Birth | 17/11/1981 | ✅ Yes |
| Email | Aki@tradewisesoftware.com | ✅ Yes |
| Mobile | +852 51295885 | ✅ Yes |
| Two-Factor Authentication | Not Set / Set - 2FA disabled | ✅ Yes |

> ✅ **Verification Status**: Green “Verified” tags appear next to verified email and phone numbers.

##### **User Account Details**

| Field | Example | Description |
|------|--------|------------|
| User Status | Enabled / Trading Prohibited | Trading permission status |
| User Type | Client / IB | User role |
| User Level | Verified Client / Senior IB | Tier/level |
| Referrer ID | 1 | ID of referring user |
| Referrer Name | ZOEY ZHOUYI JIANG | Name of referrer |
| Number of Referrals | 18 | Direct referrals made |
| User Referral Code | 8AC73K | Unique invite code |
| User Referral Link | https://.../login/8AC73K | Shareable registration link |
| Registration Time | 13/09/2024 22:35:25 | Account creation timestamp |
| Last CRM Login | 17/07/2025 11:25:27 | Most recent login |
| First Approval Time | 26/09/2024 13:30:45 | Initial KYC approval time |
| Fund Status | Funded | Whether deposit has been made |
| First Deposit Time | 26/09/2024 13:17:53 | First funding timestamp |
| Last Review Time | 24/07/2025 09:47:20 | Latest compliance review |

> 🛠️ Each field includes an **Edit** or **Reset** button for manual administrator updates.

---

## **4. Additional Core Modules (Sidebar Navigation)**

| Module | Description |
|-------|-------------|
| **User Search** | Quick user lookup |
| **CFD User List** | View CFD platform users |
| **BO User List** | View Brokerage Office (BO) platform users |
| **Funds (400)** | Manage deposits, withdrawals, and transfers |
| **KYC Verification (155)** | Review pending/approved KYC applications |
| **Trading Accounts** | Manage MT4/MT5 and other trading accounts |
| **Agent** | Administer agents and IBs |
| **Email & Notification** | Configure system alerts and email templates |
| **System Settings** | Adjust language, timezone, and global preferences |
| **Levels & Commissions** | Define user tiers and commission structures |
| **Currency & Payment** | Configure supported currencies and payment gateways |
| **Administrator** | Manage admin roles, permissions, and audit logs |

---

## **5. Practical Use Cases**

### **Case 1: Reviewing Client "Akina"**

- **Profile**: Verified Australian client
- **Finances**: Total deposit $1,009,325.00; total assets $102,559.35
- **Network**: Referred by ZOEY ZHOUYI JIANG; has 18 direct referrals
- **Contact**: Verified email and mobile
- **Activity**: Last logged in on July 17, 2025

### **Case 2: Reviewing IB "Klaus Weber"**

- **Profile**: Senior IB from Germany (User ID: 5)
- **Status**: Trading prohibited
- **Network**: Referred 6 clients; referred by deng zhen
- **Finances**: Total deposit $43,186.00; available balance $22,663.11
- **Security**: 2FA configured but currently disabled

---

## **Conclusion**

The **MIM CRM** delivers a complete, efficient, and visual user management ecosystem with the following advantages:

✅ **Holistic User Oversight**: From basic info to finances, behavior, and referral chains—all in one place
✅ **Real-Time Synchronization**: Balances and trading statuses update automatically
✅ **Transparent Hierarchy**: Clear visualization of referral networks for incentive planning and compliance
✅ **Highly Customizable**: Supports multi-language, multi-currency, and multi-platform integration

Ideal for financial brokers requiring granular operational control, regulatory compliance, and scalable partner program management.

