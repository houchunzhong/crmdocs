# **Currency & Management**  
## **1. Module Overview**

The **Currency & Payment** module acts as the financial hub of MIM CRM, comprising two key subsystems:

- ✅ **Currency Management**: Define supported fiat and digital currencies, configure display formats, and set conversion rates  
- ✅ **Payment Channel Management**: Integrate and configure deposit/withdrawal methods, including bank transfers, third-party processors, and crypto wallets  

> 🔐 Access is restricted to **System Administrators** or **Finance Managers** only. All changes are logged in the audit trail for full traceability.

---

## **2. Interface Layout**

### **Left Navigation Menu**
| Item | Function |
|------|----------|
| **Currencies** | View and edit the list of supported currencies |
| **Payment Channels** | Configure deposit/withdrawal methods and their parameters |

---

### **Top Tab Bar**
| Tab | Description |
|-----|-------------|
| **Overview** | Return to parent page |
| **Currencies** | List all configured currencies |
| **Currency – USDT** | Enter details page for a specific currency |
| **Payment Channels** | Display all active payment channels |

---

## **3. Core Function Details**

### **1. Currency Management**

#### **Function Description**  
Add, edit, or delete supported currencies—including fiat (e.g., USD, PHP) and digital assets (e.g., USDT, BTC). Each currency can be independently configured with:
- Display format (decimal places, thousand separators)
- Pricing method (manual / auto)
- Exchange rates (for deposits and withdrawals)

#### **Field Definitions**
| Field | Description |
|-------|-------------|
| **Currency Code** | Unique identifier (e.g., `USDT`), used internally by the system |
| **Currency Name** | User-facing name (e.g., “Tether”) |
| **Currency Type** | `Digital` or `Fiat` |
| **Decimal Places** | Number of digits shown after the decimal point (e.g., 2 → $1.00) |
| **Pricing Method** | `Manual` (set by admin) or `Auto` (via real-time API) |
| **Conversion Pair** | Base quote pair (e.g., `USDT/USD`) |
| **Deposit Rate** | Exchange rate applied when users deposit (e.g., 1 USDT = 1.00003 USD) |
| **Withdrawal Rate** | Exchange rate applied when users withdraw (e.g., 1 USDT = 0.99998 USD) |
| **Edit** | Modify current currency settings |

#### **Workflow**
1. Click **“Add New”**.
2. Fill in currency details:
   - Select **Currency Code** and **Name**
   - Choose **Type** (Digital / Fiat)
   - Set **Display Format** (decimal places, separators)
   - Select **Pricing Method** (Manual/Auto)
   - Define **Conversion Pair** (e.g., USDT/USD)
   - Enter **Deposit Rate** and **Withdrawal Rate**
3. Click **“Save”** to complete setup.
4. The new currency appears in the list and can be enabled in payment channels.

> 💡 Example: To support USDC, create a new currency entry and define its exchange relationship with USD.

---

### **2. Payment Channel Management**

#### **Function Description**  
Configure and manage all available funding channels, including bank wires, third-party processors (e.g., Skrill), and crypto wallets (e.g., TRON, ERC20). Each channel supports independent settings for:
- Supported currencies
- Fee structure
- Transaction limits
- Activation status

#### **Field Definitions**
| Field | Description |
|-------|-------------|
| **ID** | Unique channel identifier |
| **Display Name** | Name shown to users (e.g., “Bank Transfer”) |
| **Sort Order** | Display priority (lower = higher) |
| **Status** | `Enabled` / `Disabled` |
| **Direction** | `Deposit` (incoming) or `Withdrawal` (outgoing) |
| **Supported Currencies** | Currencies this channel handles (e.g., BTC, USD) |
| **Platforms** | Linked trading systems (e.g., BO, MT5, AQX) |
| **Wallet** | Associated wallet account (e.g., “MT5&AQX Wallet”) |
| **Fee Rate** | Percentage-based fee (e.g., 0%) |
| **Min/Max per Transaction (USD)** | User-level transaction limits |
| **Actions** | **View** (details) / **Parameters** (advanced settings) |

#### **Workflow**
1. Click **“Add New”**.
2. Enter basic info:
   - Display Name
   - Sort Order
   - Status (default: Enabled)
   - Direction (Deposit/Withdrawal)
   - Supported Currencies (multi-select)
   - Platforms
   - Wallet Link
3. Set fees and limits:
   - Fee Rate (e.g., 0% for free)
   - Min/Max per Transaction (in USD)
4. Click **“Save”**. The system generates a Channel ID and opens the **Payment Channel Details** page.

---

### **3. Payment Channel Details**

#### **Function Description**  
Provides a complete configuration view for fine-tuning channel parameters.

#### **Field Definitions**
| Field | Description |
|-------|-------------|
| **Logo** | Channel icon (e.g., bank logo) |
| **Display Name** | User-facing name |
| **Sort Order** | Display sequence |
| **Status** | Enabled/Disabled |
| **Direction** | Deposit / Withdrawal |
| **Supported Currencies** | Specific currencies supported |
| **Platforms** | e.g., BO, MT5, AQX |
| **Wallet** | Linked wallet address |
| **Channel Type** | e.g., “Online”, “Offline” |
| **Payment Method** | e.g., “Bank Wire (T/T)” |
| **Estimated Settlement Time** | e.g., “0 minutes” (instant) |
| **Admin Notes** | Internal remarks (not visible to users) |
| **Fee Rate** | e.g., `-` indicates no fee |
| **Fee Bearer** | “Merchant” or “Customer” |
| **System Min/Max per Tx (USD)** | Backend transaction limits |
| **User Min/Max per Tx (USD)** | Frontend user limits |

#### **Workflow**
1. From the channel list, click **“View”** or **“Parameters”**.
2. Review or modify settings.
3. Click **“Edit”** in the top-right corner to make changes.
4. Click **“Save”** after updates.

> 📌 Note: **System Max > User Max** — backend limits must exceed user-facing limits.

---

## **4. Best Practices**

| Scenario | Recommendation |
|--------|----------------|
| **Adding Crypto** | Prioritize stablecoins (e.g., USDT, USDC); avoid highly volatile assets |
| **Rate Configuration** | Set deposit rates slightly higher than withdrawal rates to ensure margin |
| **Channel Naming** | Use clear labels (e.g., “Bank Transfer – USD”) |
| **Fee Strategy** | Waive fees on small transactions to encourage activity |
| **Access Control** | Restrict module access to finance team only to prevent misconfiguration |

---

## **5. Frequently Asked Questions (FAQ)**

### **Q1: How do I add a new payment method?**  
- Go to **Payment Channels** > **Add New**, fill in the details, and link the corresponding wallet.

### **Q2: Why can’t I select a certain currency?**  
- Ensure the currency has been created in the **Currencies** module with the correct type (Digital/Fiat).

### **Q3: Can one channel support multiple platforms?**  
- ✅ Yes. A single channel can link to multiple platforms (e.g., BO + MT5), provided APIs are compatible.

### **Q4: Does the system support auto-recharge?**  
- ❌ Not in the current version. Manual approval or scheduled jobs are required.

---

## **6. Summary**

The **Currency & Payment** module in MIM CRM delivers a flexible, secure, and compliant financial infrastructure. Through standardized workflows, administrators can rapidly deploy multi-currency and multi-channel payment solutions to serve global clients—while maintaining system stability and financial transparency.

✅ **Recommended Setup Sequence**:  
1. Add Currencies → 2. Configure Rates → 3. Create Payment Channels → 4. Set Limits & Fees → 5. Enable & Test

> 📌 All configurations require internal approval to comply with AML and local regulatory requirements.

---

**Version: v1.0**  
**Last Updated: January 2026**

---

# **Administrator Module: User Guide**  
**My Investment Markets (MIM) CRM System**

This document continues the consistent style of previous modules to provide a detailed explanation of the **Administrator** module in the MIM CRM system. Designed exclusively for system operations teams, this module enables the management of backend user accounts, role-based permission assignment, and audit logging of critical actions—serving as the core component for platform security and compliance.

---

## **1. Module Overview**

The **Administrator** module functions as the **permission hub** of MIM CRM, comprising two key features:

- ✅ **Administrator List**: View, add, and edit system administrator accounts  
- ✅ **System Logs**: Track all administrative actions with support for filtering by time, IP, user, and more  

> 🔐 Access is restricted to **Master-level Administrators** only. All changes are recorded in an immutable audit log for full traceability.

---

## **2. Interface Layout**

### **Left Navigation Menu**
| Item | Function |
|------|----------|
| **Administrator List** | View all admin account details |
| **System Logs** | Query historical admin activities |

---

### **Top Tab Bar**
| Tab | Description |
|-----|-------------|
| **Overview** | Return to parent page |
| **Administrator List** | Display current list of administrators |
| **System Logs** | View system-level operation records |

---

## **3. Core Function Details**

### **1. Administrator List**

#### **Function Description**  
Displays basic information for all administrator accounts in the system, supporting creation, editing, and status control. Each administrator has a unique ID and assigned role that determines their functional access scope.

#### **Field Definitions**
| Field | Description |
|-------|-------------|
| **ID** | Unique auto-incremented administrator number |
| **Name** | Display name (e.g., “Default Admin”) |
| **Phone** | Contact number (used for login verification) |
| **Email** | Login username (must be unique) |
| **Role** | Assigned role (e.g., Master, Manager, Operator) |
| **Created At** | Account creation date (DD/MM/YYYY format) |
| **Last Login** | Timestamp of most recent successful login |
| **Last Login IP** | Source IP address of last login (for security analysis) |
| **Status** | `Enabled` / `Disabled` (toggle switch) |
| **Actions** | **Edit** (modify account details) |

#### **Workflow**
1. Click **“Add Administrator”**.
2. Fill in new admin details:
   - Name
   - Phone number (requires verification)
   - Email (must be unique)
   - Role (select from dropdown)
3. Set an initial password or send a reset link.
4. Click **“Save”** to complete creation.
5. The new administrator appears in the list and will be logged in **System Logs** upon first action.

> 💡 Example: To create a finance specialist, assign the “Operator” role with access limited to funding and payment modules.

---

### **2. System Logs**

#### **Function Description**  
Records all critical actions performed by administrators—including logins, data modifications, and configuration changes. Supports multi-dimensional filtering for rapid anomaly detection.

#### **Field Definitions**
| Field | Description |
|-------|-------------|
| **Name** | Administrator’s display name |
| **Email** | Login email address |
| **Phone** | Associated phone number |
| **Action Type** | Operation category (e.g., LOGIN, UPDATE, DELETE) |
| **Object Type** | Target entity (e.g., ADMINISTRATOR, CURRENCY, PAYMENT_CHANNEL) |
| **Target Object** | Specific item affected (e.g., “Administrator”, “USDT”) |
| **Details** | Brief description (e.g., “Login”, “Updated currency rate”) |
| **Timestamp** | Time of action (DD/MM/YYYY format) |
| **IP Address** | Source IP (enables geolocation tracking) |

#### **Search & Filter Options**
- **Date Range**: Filter by start/end date  
- **Name/Phone Search**: Find specific administrators  
- **IP Address Search**: Investigate suspicious logins  

#### **Workflow**
1. Navigate to **“System Logs”**.
2. Set filters using the top toolbar.
3. Click **“Search”** to retrieve matching records.
4. Review action details to verify legitimacy.

> 📌 Note: All logs are retained for at least **180 days**, complying with financial industry regulations.

---

## **4. Role-Based Access Control (RBAC)**

| Role | Permissions |
|------|-------------|
| **Master** | Full system access; can manage all modules, create admins, and modify global settings |
| **Manager** | Can manage users, funding, trading accounts, IBs, and core business functions |
| **Operator** | Limited permissions; typically used for finance or support staff with read-only or task-specific access |

> ⚠️ Recommendation: Follow the **principle of least privilege**—avoid over-assigning permissions.

---

## **5. Best Practices**

| Scenario | Recommendation |
|--------|----------------|
| **Initial Deployment** | Create one Master account as the primary controller; use sub-accounts for all other personnel |
| **Employee Offboarding** | Immediately disable the account to prevent unauthorized access |
| **Sensitive Operations** | Require dual approval for critical changes to prevent errors |
| **Regular Audits** | Review system logs monthly to detect anomalous behavior |

---

## **6. Frequently Asked Questions (FAQ)**

### **Q1: How do I add a new administrator?**  
- Go to **Administrator List** > **Add Administrator**, fill in the details, and assign a role.

### **Q2: Why can’t I see a certain action in the logs?**  
- Verify your filter criteria or check if you have sufficient permissions to view that module’s logs.

### **Q3: Can system logs be exported?**  
- ✅ Yes. Click **“Export CSV”** in the top-right corner to download an encrypted ZIP file (requires transaction password to unzip).

### **Q4: Can administrator accounts be deleted?**  
- ❌ No. Accounts can only be **disabled**. Deletion would break audit integrity and is not permitted.

---

## **7. Summary**

The **Administrator** module in MIM CRM delivers robust permission control and comprehensive operational auditing. Through clear role segmentation and immutable logging, it ensures both backend security and regulatory compliance.

✅ **Recommended Workflow**:  
1. Create Master account → 2. Add sub-administrators → 3. Assign roles → 4. Conduct regular log reviews → 5. Disable accounts when necessary

> 📌 All actions must align with internal security policies to maintain system stability and data integrity.

---

**Version: v1.0**  
**Last Updated: January 2026**

---

# **Funding Data Module: User Guide**  
**My Investment Markets (MIM) CRM System**

This document continues the consistent style of previous modules to provide a detailed explanation of the **Funding Data** module in the MIM CRM system. Designed for administrators, this module offers a comprehensive view of daily capital flows, covering key metrics such as registrations, active users, deposits, and withdrawals—serving as a critical tool for assessing business health and optimizing operational strategies.

---

## **1. Module Overview**

The **Funding Data** module serves as the **financial analytics hub** of MIM CRM, presenting daily capital movements through structured tables and supporting the following features:

- ✅ **Daily Funding Report**: View daily metrics including new registrations, active users, deposit/withdrawal amounts, and user counts  
- ✅ **Key Ratio Calculations**: Automatically compute core indicators such as the **Withdrawal-to-Deposit Ratio** and **Successful Withdrawal Rate**  
- ✅ **Trend Insights**: Compare data across multiple days to identify growth patterns or risk signals  

> 📊 All data is generated from real-time system statistics and can be exported as CSV for in-depth analysis.

---

## **2. Main Interface Layout**

### **Left Navigation Menu**
| Item | Function |
|------|----------|
| **Funding Data** | View daily funding transaction details |
| **Channel Management** | Analyze performance across marketing channels |
| **Total Visits** | Track cumulative website traffic |
| **Overall Conversion Rate** | Measure efficiency from visit to registration |
| **Daily Visits** | Count of unique daily visitors |
| **Daily Conversion Rate** | Daily registration conversion rate |

---

### **Top Tab Bar**
| Tab | Description |
|-----|-------------|
| **Overview** | Return to parent page |
| **Payment Channels** | Review funding performance by payment method |
| **Funding Data** | Display the daily funding detail table |

---

## **3. Core Function Details**

### **1. Funding Data List (Daily Funding Report)**

#### **Function Description**  
Displays capital flow over recent days in a tabular format, with each row representing one day’s data—enabling easy cross-day comparison and trend analysis.

#### **Field Definitions**
| Field | Description |
|-------|-------------|
| **Date** | Date of the data (format: YYYY/MM/DD) |
| **New Registrations** | Number of new users registered that day |
| **Active Users** | Users who logged in or traded that day |
| **Deposit Amount** | Total successful deposits (in USD) |
| **Deposit Transactions** | Total number of deposit operations |
| **Depositing Users** | Number of users who made at least one deposit |
| **First-Time Deposits** | Amount contributed by users making their first deposit |
| **Repeat Deposits** | Cumulative amount from returning depositors |
| **Withdrawal Requests** | Total withdrawal amount requested that day |
| **Withdrawal Transactions** | Total number of withdrawal requests |
| **Withdrawing Users** | Number of users submitting withdrawal requests |
| **Successful Withdrawal Amount** | Total amount successfully processed |
| **Successful Withdrawal Transactions** | Number of completed withdrawal operations |
| **Successful Withdrawing Users** | Number of users who completed withdrawals |
| **Withdrawal-to-Deposit Ratio** | `Successful Withdrawal Amount / Deposit Amount` — reflects capital outflow pressure |

#### **Example Interpretation**  
Assume the following data for a given day:  
- **Date**: 2025/10/27  
- **Deposit Amount**: $78,900 USD  
- **Successful Withdrawal Amount**: $12,000 USD  
- **Withdrawal-to-Deposit Ratio**: 15.21%  

→ This indicates strong capital inflow and low outflow, reflecting a healthy net positive funding position for the platform.

> 💡 Tip: If the **Withdrawal-to-Deposit Ratio** exceeds 30% for multiple consecutive days, be alert to potential customer attrition or a surge in withdrawal demand.

---

### **2. Key Metrics: Definitions & Use Cases**

| Metric | Meaning | Application Scenario |
|--------|---------|----------------------|
| **New Registrations** | User growth rate | Evaluate marketing campaign effectiveness |
| **Active Users** | User engagement level | Assess product stickiness |
| **Deposit Amount** | Strength of capital inflow | Monitor core revenue streams |
| **First-Time Deposits** | Contribution from new users | Measure quality of user acquisition |
| **Repeat Deposits** | Repurchase behavior of existing users | Estimate customer lifetime value (LTV) |
| **Withdrawal Requests vs. Successful Withdrawals** | Processing efficiency | Identify payment delays or technical issues |
| **Withdrawal-to-Deposit Ratio** | Liquidity risk indicator | Flag potential cash flow pressure |

---

### **3. Data Visualization Recommendations (Future Enhancement)**

Although the current interface uses only tables, we recommend adding charting support in future versions:

- 📈 **Line Chart**: Show time trends for *Deposit Amount* and *Withdrawal Amount*  
- 📊 **Bar Chart**: Compare *New Registrations* and *Active Users* across dates  
- 🧩 **Heatmap**: Highlight high-volatility days (e.g., around holidays)

> 🔍 Suggestion: Set a red-alert threshold for the **Withdrawal-to-Deposit Ratio** (e.g., >30%) to trigger automated notifications.

---

## **4. Best Practices**

| Scenario | Recommendation |
|----------|----------------|
| **Daily Monitoring** | Review *Deposit Amount* and *Withdrawal-to-Deposit Ratio* daily to establish baselines |
| **Anomaly Investigation** | If *Successful Withdrawal Transactions* are significantly lower than *Withdrawal Requests*, check for payment channel failures |
| **Marketing Evaluation** | Compare *New Registrations* and *First-Time Deposits* during promotions to assess ROI |
| **Risk Alerting** | Configure alerts for high *Withdrawal-to-Deposit Ratio* to prevent liquidity strain |

---

## **5. Frequently Asked Questions (FAQ)**

**Q1: How often is the data updated?**  
✅ In real time. Each transaction is recorded under its respective date immediately upon completion.

**Q2: Why is “Successful Withdrawal Amount” less than “Withdrawal Requests”?**  
❌ This is normal. Some withdrawals may fail due to compliance rejection, insufficient balance, or other validation issues.

**Q3: Can I export the full dataset?**  
✅ Yes. Click the **“Export CSV”** button in the top-right corner to download all records (including hidden columns).

**Q4: How can I view data for a custom date range?**  
⚠️ The current version supports only the last 15 days. Custom date-range filtering will be available in a future release.

---

## **6. Summary**

The **Funding Data** module in MIM CRM provides businesses with a transparent and precise view of capital flows. Through structured daily reports and key ratio analysis, administrators can quickly grasp business dynamics, respond promptly to market changes, and optimize funding management strategies.

✅ **Recommended Workflow**:  
1. Review *Deposit Amount* and *Withdrawal-to-Deposit Ratio* daily  
2. Periodically analyze *First-Time Deposit* trends  
3. Compare *Active Users* vs. *New Registrations*  
4. Detect anomalies and take corrective action  

📌 All data originates from real transaction records, ensuring reliable decision-making.

---

**Version: v1.0**  
**Last Updated: January 2026**

---

# **渠道管理模块使用说明书**  
**My Investment Markets (MIM) CRM 系统**

本文档延续前序模块的统一风格，详细说明 MIM CRM 中“渠道管理”模块的功能架构与操作方法。该模块专为市场与运营团队设计，用于创建、跟踪和分析用户获取渠道，通过分配唯一追踪代码，精准衡量各营销活动的效果。

---

## **一、模块概览**

“渠道管理”模块是 MIM CRM 内部**营销归因与效果分析的核心工具**，支持以下功能：

- ✅ 创建并管理数字营销渠道（如 Google Ads、TikTok、Facebook）
- ✅ 为每个渠道分配唯一的追踪代码
- ✅ 监控关键指标：访问量、注册转化数、转化率等
- ✅ 通过 JavaScript 代码片段与外部网站集成

> 🔍 所有数据实时自动采集与同步，确保 ROI 分析准确可靠。

---

## **二、主界面布局说明**

### **左侧导航菜单**
| 项目 | 功能 |
|------|------|
| **渠道管理** | 查看并管理所有营销渠道 |
| **总访问数** | 统计网站累计访问量 |
| **总转化率** | 显示整体注册转化率 |
| **日访问数** | 跟踪每日独立访客数量 |
| **日转化率** | 监控每日注册转化效率 |

---

### **顶部标签页**
| 标签 | 说明 |
|------|------|
| **总览** | 返回上级页面 |
| **资金数据** | 查看每日资金流水报表 |
| **渠道管理** | 管理营销渠道及追踪代码 |

---

## **三、核心功能详解**

### **1. 渠道列表（渠道仪表盘）**

#### **功能描述**  
展示所有已配置的营销渠道，包括渠道类型、落地页 URL、状态及最近活跃时间。每个渠道拥有唯一 ID 和追踪代码，用于精准归因。

#### **字段说明**
| 字段 | 说明 |
|------|------|
| **渠道ID** | 系统内部唯一编号 |
| **渠道代码** | 用于网页嵌入的追踪标识（如 `K9L4X`） |
| **渠道名称** | 显示名称（如 “官方网站”、“TikTok”） |
| **渠道类型** | 渠道分类（如 线上-官网、线上-媒体、线上-广告） |
| **网站URL** | 对应的落地页或广告目标地址 |
| **状态** | `启用` / `停用` — 控制是否记录用户来源 |
| **创建日期** | 渠道创建时间 |
| **最后活跃日期** | 该渠道最近一次产生访问的日期 |
| **操作** | **查看代码** — 弹出追踪脚本窗口 |

#### **示例条目**
| 渠道ID | 代码  | 名称         | 类型         | URL                          | 状态   | 最后活跃日期 |
|--------|-------|--------------|--------------|------------------------------|--------|----------------|
| 1      | K9L4X | 官方网站     | 线上-官网    | www.tradewisesoftware.com    | 启用   | 2025/10/27     |

> 💡 小贴士：建议使用清晰命名，如 “Google Ads – 外汇推广”，便于团队协作。

---

### **2. 追踪代码集成**

#### **功能描述**  
每个营销渠道对应一段唯一的 JavaScript 代码片段，需嵌入到对应的落地页 HTML 中，使 MIM CRM 能将新注册用户及入金行为准确归因至该渠道。

#### **操作流程**
1. 在渠道列表中点击 **“查看代码”**。
2. 弹窗显示追踪脚本：
   ```html
   <script id="crm-snippet" src="https://client.tradewisesoftware.com/externalScript/index.js" />
