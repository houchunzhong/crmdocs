# **User Tiers **  


## **1. Module Overview**

The **User Tiers** module serves as the **user segmentation hub** of MIM CRM, enabling the configuration and management of all user classification levels. It determines not only the default identity assigned upon user registration but also influences subsequent fund flows, trading permissions, and revenue-sharing logic. Key capabilities include:

- ✅ Creating or editing user tiers (e.g., “New Client”, “Verified Client”, “Platinum”)  
- ✅ Binding each tier to a dedicated **Trading Account Plan**  
- ✅ Assigning custom **Commission Plans** and **Settlement Plans**  
- ✅ Supporting independent tier hierarchies for **Clients** and **Agents**  
- ✅ Providing internal notes for documenting upgrade criteria or marketing strategies  

> 🔐 Access is restricted to **System Administrators** or **Operations Managers** only. All changes require explicit saving and are logged in the system audit trail.

---

## **2. Interface Layout**

### **Left Navigation Menu**
| Item | Function |
|------|----------|
| **Tiers & Commissions** | Enter the user tier and commission configuration center |
| - User Tiers | View and manage all user tiers |
| - Product Types | Define trading product categories |
| - Commission Plans | Configure commission structures per tier |
| - Settlement Plans | Set up fund settlement methods |

---

### **Top Tab Bar**
| Tab | Description |
|-----|-------------|
| **Overview** | Return to parent page |
| **Daily Visits** | View daily active user statistics |
| **Fund Data** | Monitor fund inflow/outflow trends |
| **Administrator List** | View all admin accounts |
| **User Tiers** | Current page |

---

### **User Tiers List View**
| Field | Description |
|-------|-------------|
| **ID** | Unique auto-increment identifier |
| **User Type** | Category: Client / Agent |
| **Display Name** | Tier name shown to users (e.g., “Platinum”) |
| **Tier Level** | Numeric value used for sorting and permission logic |
| **Account Plan** | Linked trading account template (e.g., `Blank Trading Account Plan for initial setup`) |
| **Commission Plan** | Assigned commission structure (e.g., `No Commission`, `Blank Commission Plan for initial setup`) |
| **Settlement Plan** | Fund settlement method (e.g., `No Settlement`, `sub IB`) |
| **Notes** | Internal remarks for operational or marketing reference |
| **Actions** | Contains an **Edit** button to modify the tier |

> 💡 Example: The `Platinum` tier requires a minimum deposit of $5,000 and grants access to premium support and advanced trading tools.

---

## **3. Core Feature Details**

### **1. Adding a New User Tier**

#### **Procedure**
1. Navigate to **Tiers & Commissions → User Tiers**  
2. Click the **Add New User Tier** button in the top-right corner  
3. Fill in the following required fields:
   - **User Type**: Select `Client` or `Agent`  
   - **Display Name**: Enter the front-end visible name (e.g., “VIP Gold”)  
   - **Tier Level**: Assign a numeric value (lower = more basic; higher = more privileged)  
   - **Account Plan**: Choose a pre-configured trading account template  
   - **Commission Plan**: Select applicable commission model (e.g., `No Commission`, `Fixed Spread`)  
   - **Settlement Plan**: Specify settlement method (e.g., `No Settlement`, `Sub IB`)  
4. Optionally add **Notes**, such as: “Minimum first deposit: $10,000”  
5. Click **Confirm** to save

> ⚠️ Notes:  
> - Tier Level values must be unique within the same User Type  
> - All fields are mandatory; submission will fail if any are missing

---

### **2. Editing an Existing Tier**

#### **Procedure**
1. Locate the target tier in the list (e.g., “Platinum”)  
2. Click the **Edit** button on the right  
3. Modify any field (e.g., update commission plan or notes)  
4. Click **Confirm** to apply changes

> ✅ Example: Changing the `IB` tier’s commission plan from `No Commission` to `Blank Commission Plan for initial setup` activates its referral revenue capability.

---

### **3. Tier Association Logic**

| Field | Purpose |
|-------|--------|
| **Account Plan** | Defines initial trading parameters (leverage, stop-out level, etc.) when a user creates an account |
| **Commission Plan** | Determines whether trading volume generates rebates and how they’re distributed to upstream agents |
| **Settlement Plan** | Specifies the payout path (e.g., direct payment vs. sub-agent routing) |
| **Tier Level** | Influences system privileges (e.g., API access, priority support) |

> 💡 Real-world use: A high-tier client (Platinum) may enjoy higher leverage limits and faster customer service response times.

---

## **4. Typical Use Cases**

### **Use Case 1: Building a Client Pyramid Model**

> 🎯 Goal: Establish a four-tier client hierarchy: “New → Standard → Verified → Platinum”

- ✅ Implementation:
  1. Create tiers:
     - `New Client` (Level 1) → Default account, no commissions  
     - `Client` (Level 2) → Standard terms, basic service  
     - `Verified Client` (Level 3) → Requires KYC, reduced fees  
     - `Platinum` (Level 5) → Min. deposit ≥ $5,000, VIP support + API access  
  2. Link each tier to appropriate account, commission, and settlement plans  
  3. Guide users through upgrades via frontend prompts (e.g., “Deposit $5,000 to become Platinum”)

> ✅ Outcome: Improved client retention and stronger loyalty among high-value users.

---

### **Use Case 2: Structuring an Agent Distribution Network**

> 🎯 Goal: Implement a three-tier agent model: “IB → Sub IB → Agent”

- ✅ Implementation:
  1. Create agent tiers:
     - `IB` (Level 4) → Master agent, can recruit downstream partners  
     - `Sub IB` (Level 3) → Sub-agent, reports to IB  
     - `Agent` (Level 2) → Basic promoter, no recruitment rights  
  2. Bind `IB` to `Blank Commission Plan for initial setup` and `sub IB` settlement  
  3. Restrict `Sub IB` to only invite `Agent`-type users  
  4. Monitor performance and payouts across all levels in the backend

> ✅ Outcome: A clear, scalable partner ecosystem with aligned incentives.

---

### **Use Case 3: Launching Time-Limited Promotional Tiers**

> 🎯 Goal: Introduce a limited-time “Golden Member” tier to attract new clients

- ✅ Implementation:
  1. Add temporary tier: `Golden Member` (Level 6)  
  2. Configure:
     - Account Plan: High leverage + free signal service  
     - Commission Plan: 10% cashback in first month  
     - Notes: “Valid only from March 1–31, 2026”  
  3. Promote benefits in marketing campaigns  
  4. After campaign ends, either disable or archive the tier

> ✅ Outcome: Strong short-term acquisition boost without long-term cost burden.

---

## **5. Best Practices**

| Scenario | Recommendation |
|--------|----------------|
| **Tier Naming** | Use intuitive, market-friendly names (e.g., “Platinum” instead of “Level 5”) |
| **Tier Sequencing** | Use sequential integers (1, 2, 3…); avoid gaps to simplify logic |
| **Commission Design** | Start with blank templates and refine based on real-world performance |
| **Permission Mapping** | Align tier levels with functional privileges (API, withdrawal speed, etc.) |
| **Auto-Upgrades** | Integrate with deposit/trading volume triggers for seamless progression |

---

## **6. Frequently Asked Questions (FAQ)**

### **Q1: Can I delete an existing user tier?**  
- ❌ Direct deletion is not supported.  
- ✅ Workaround: Deactivate the tier (hide from new registrations) or contact technical support for database cleanup.

---

### **Q2: Why can’t some users upgrade to a higher tier?**  
- ❌ Possible reasons:  
  - Upgrade conditions not met (e.g., insufficient deposit)  
  - Tier manually locked by admin  
  - No auto-upgrade rule configured  

> ✅ Solution: Review user eligibility; if manual upgrade is needed, assign the new tier directly in the user profile.

---

### **Q3: Can multiple tiers share the same commission plan?**  
- ✅ Yes. Multiple tiers can reference the same commission plan—ideal for unified policy enforcement.

---

### **Q4: How do I ensure tier changes don’t affect existing users?**  
- ✅ Approach:  
  1. Modifying a tier’s configuration does **not** retroactively change existing users’ assignments  
  2. For bulk updates, use data export/import or scripting tools  
  3. Always test changes in a staging environment before production rollout

---

## **7. Summary**

The **User Tiers** module is a strategic enabler of precision operations in MIM CRM. It transcends simple labeling—it shapes user experience, drives engagement, and powers scalable business models. By thoughtfully designing and managing user tiers, organizations can build structured, responsive ecosystems that deliver the right value to the right user at the right time.

✅ **Recommended Workflow**:  
1. Go to **Tiers & Commissions → User Tiers** → 2. Click **Add New User Tier** → 3. Select User Type → 4. Enter Display Name, Tier Level, and Plans → 5. Add Notes → 6. Click **Confirm**

> 📌 All changes are recorded in the system logs, ensuring full auditability, transparency, and regulatory compliance.

---

**Version: v1.0**  
**Last Updated: February 2026**