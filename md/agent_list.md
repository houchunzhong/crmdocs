# **Agent List Module: User Guide**  

## **1. Module Overview**

The **Agent List** module acts as the **agent relationship management hub** of MIM CRM. It presents structured tabular data on all agent users, including:

- ✅ Basic profile information (name, contact details)  
- ✅ Agent tier and status  
- ✅ Commission plan configuration  
- ✅ Number of referred clients and their financial activity  
- ✅ Monthly deposit/withdrawal volumes from subordinates  
- ✅ Total accrued commissions and payout status  

> 🔐 Access is restricted to **Administrators** or **Finance Managers** only. All actions are logged in the audit trail for full traceability.

---

## **2. Interface Layout**

### **Left Navigation Menu**
| Item | Function |
|------|----------|
| **Agent List** | View all agents with key performance indicators |
| **Agent Applications** | Review and approve new IB registration requests |
| **Order Commissions** | Inspect commission details generated per trade |
| **Commission Records** | View historical commission accruals per agent |
| **Commission Payout Records** | Track processed and paid commission settlements |

---

### **Top Tab Bar**
| Tab | Description |
|-----|-------------|
| **Overview** | Return to parent page |
| **Agent List** | Current page displaying all agents |
| **Agent Applications** | Pending IB applications awaiting review |

---

## **3. Core Feature Details**

### **1. Agent List Main View**

#### **Function Description**  
Displays all agent users in a sortable, filterable table for rapid performance assessment and operational oversight.

#### **Field Definitions**
| Field | Description |
|-------|-------------|
| **User** | Agent’s display name, full name, and ID (e.g., `Akina Akiyama - 16672`) |
| **Phone & Email** | Contact information with verification badges:  
  - ✅ **Green ✓**: Verified phone/email  
  - ❌ **Red !**: Unverified or flagged |
| **User Tier** | Current role level (e.g., `Verified Client`, `IB`) |
| **Commission Plan** | Assigned commission scheme (e.g., “Blank Commission Plan for initial setup”) |
| **Subordinates Count** | Number of directly referred clients (e.g., 4 = 4 direct referrals) |
| **Clients’ Monthly Deposits** | Cumulative deposits by subordinates this month (displayed in green) |
| **Clients’ Monthly Withdrawals** | Cumulative withdrawals by subordinates this month (displayed in red) |
| **Total Commission** | Total accrued commission based on defined rules (e.g., % of deposits) |
| **Paid / Unpaid Commission** | Amount already paid vs. pending payout (format: `X.XX / Y.YY`) |
| **Actions** | **View** — opens the agent’s detailed profile page |

#### **Interactive Controls**
- 🔎 **Search Bar**: Global search by `ID`, `name`, `phone`, or `email`.  
- ▼ **Filters**: Narrow results by “User Tier” (e.g., show only IBs).  
- 📊 **Sorting**: Click any column header to sort ascending/descending (e.g., rank by “Monthly Deposits”).

> 💡 Example: An IB with $12,000 in “Clients’ Monthly Deposits” demonstrates strong recruitment impact—ideal for priority support or rewards.

---

### **2. Agent Detail Page (Agent Profile)**

#### **Function Description**  
Clicking **“View”** on any agent opens their full profile, providing complete visibility into account details, hierarchy, commission history, and settlement records.

#### **Page Structure**
##### **Left Information Panel**
| Field | Description |
|-------|-------------|
| **Avatar & Name** | Profile picture and full name |
| **ID & Role** | User ID and type (e.g., `Verified Client`) |
| **Total Deposits / Withdrawals** | Lifetime funding activity |
| **Total Assets / Available Balance** | Real-time asset snapshot |
| **Nationality / Residence** | Geographic details |
| **Registration Time** | Account creation timestamp |
| **Contact Info** | Phone and email with verification status |

##### **Right Content Area (Tabbed Interface)**
| Tab | Content |
|-----|--------|
| **Agent Details** | Edit agent info, commission plan, payout method, etc. |
| **User Relationship Tree** | Visualize the agent’s full referral hierarchy |
| **Commission Records** | View per-trade commission accruals |
| **Commission Settlement Records** | Review processed commission payouts |

---

### **3. Key Sub-Module Descriptions**

#### **① Agent Details**
- **User Type**: e.g., “Agent”, “Verified Client”  
- **User Tier**: Current permission level  
- **Status**: Active / Inactive  
- **Became Agent On**: Date first authorized as an IB  
- **Plan Type**: e.g., “Inherit from User Tier” (auto-applies parent policy)  
- **Account Opening Template**: Default trading account configuration  
- **Commission Plan**: Active rebate rule (e.g., “No Commission” or “1% Deposit Rebate”)  
- **Settlement Plan**: Payout method (e.g., “Manual Settlement”)  
- **Referrer ID / Name**: Identifies the superior who introduced this agent  
- **Referral Code / Link**: Unique code and URL for promotions  

> ✅ Example: Akina Akiyama’s profile shows she was referred by User ID:1 and currently uses a “No Commission” plan—indicating her rebate structure hasn’t been activated yet.

#### **② Commission Records**
- Lists every transaction that triggered a commission.
- Includes:
  - Trade Order ID  
  - Commission Type (e.g., “Deposit Commission”)  
  - Agent Commission Amount  
  - Referred User  
  - Trading Account  
  - Instrument Traded  
  - Trade Volume  
  - Calculated Commission  

> ⚠️ Empty records indicate no qualifying transactions have occurred yet.

#### **③ Commission Settlement Records**
- Logs completed commission payout cycles.
- Includes:
  - Settlement ID  
  - Status (e.g., “Settled”, “Pending Review”)  
  - Approval Method (e.g., “System Auto”, “Manual Review”)  
  - Settlement Plan  
  - Total Agent Commission  
  - Post-Settlement CRM Balance  

> 📌 Note: This module supports financial reconciliation and payment verification.

---

## **4. Best Practices**

| Scenario | Recommendation |
|--------|----------------|
| **Agent Recruitment** | Promptly review new applications in **Agent Applications** to retain high-potential partners |
| **Performance Review** | Sort by “Clients’ Monthly Deposits” to identify top-performing IBs for rewards or coaching |
| **Commission Setup** | Assign competitive plans (e.g., 1%–3%) to active agents to boost motivation |
| **Risk Management** | Flag or deactivate agents with zero referrals or deposits over extended periods |
| **Financial Reconciliation** | Regularly cross-check **Commission Settlement Records** to ensure accurate payouts |

---

## **5. Frequently Asked Questions (FAQ)**

### **Q1: How do I add a new agent?**  
- Go to **Agent Applications** → Approve the request → The user is automatically upgraded to IB status.

### **Q2: Why is an agent’s “Total Commission” showing as 0?**  
- Possible reasons:  
  - No valid commission plan assigned  
  - Subordinates haven’t made deposits  
  - Plan is set to “No Commission”  

### **Q3: Can I change an agent’s commission plan?**  
- ✅ Yes. In the **Agent Details** tab, click **“Edit”** to update the commission plan.

### **Q4: What does “Subordinates Count” include?**  
- Only **direct referrals** (first-level downlines). It excludes second- or third-tier indirect users.

### **Q5: When are commissions settled?**  
- Default: **Manual settlement**, requiring admin action in **Commission Payout Records**.  
- Optional: Configure **daily automatic settlement** via system settings.

---

## **6. Summary**

The **Agent List** module delivers a transparent and scalable framework for managing partner relationships. By consolidating performance data, financial metrics, and commission status, administrators can accurately identify high-value agents, optimize incentive structures, and ensure fair, timely payouts.

✅ **Recommended Workflow**:  
1. Open **Agent List** → 2. Sort by “Clients’ Monthly Deposits” → 3. Click **“View”** on target agent → 4. Review commission plan and settlement history → 5. Adjust configuration or initiate payout as needed

> 📌 All actions are audited, ensuring compliance, accountability, and operational integrity.

---

**Version: v1.0**  
**Last Updated: January 2026**