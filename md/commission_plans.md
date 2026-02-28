# **Commission Plans**  

## **1. Module Overview**

The **Commission Plans** module serves as the **revenue allocation engine** of MIM CRM. It defines how commissions are calculated and distributed across the agent hierarchy, with support for granular configuration by:

- Trading platform (e.g., MT5, TradeWise)  
- Trading service provider (e.g., `demo\STD:BB`)  
- Account group  
- Product type (e.g., Forex, Crypto, Index)  

Key commission models include:

- ✅ **Spread Rebate**: Upper-level agents earn a portion of the spread from their downline clients’ trades  
- ✅ **Commission Markup Rebate**: Upper-level agents receive the difference between what they charge and what their sub-agents pay  
- ✅ **Self-Trading Exclusion**: Prevents agents from earning rebates on their own trading activity  

> 🔐 Access is restricted to **System Administrators** or **Operations Managers** only. All changes require explicit saving and are logged in the system audit trail.

---

## **2. Interface Layout**

### **Left Navigation Menu**
| Item | Function |
|------|----------|
| **Tiers & Commissions** | Enter the user tier and commission configuration center |
| - Commission Plans | View and manage all commission structures |
| - Settlement Plans | Configure fund settlement methods |

---

### **Top Tab Bar**
| Tab | Description |
|-----|-------------|
| **Overview** | Return to the main dashboard |
| **Commission Plans** | Current page |

---

### **Commission Plans List View**
| Field | Description |
|-------|-------------|
| **Plan Name** | Unique identifier (e.g., “Blank Commission Plan for initial setup”) |
| **Trading Platform** | Supported platform (e.g., MT5, TradeWise) |
| **Service Provider** | Specific broker feed (e.g., `demo\STD:BB`) |
| **Group Name** | Account grouping label (e.g., `demo\ECN:B`) |
| **Product Type** | Applicable category (e.g., Forex, Crypto, Index) |
| **Spread Rebate (USD/lot)** | Amount paid per lot to the upper-level agent (in USD) |
| **Commission Rebate (USD/lot)** | Additional commission rebate per lot (in USD) |
| **Edit** | Modify plan parameters |
| **Delete** | Permanently remove the plan |

> 💡 Example: The `demo\STD:BB` provider’s `Forex` product type is set to `0.5 USD per lot`, meaning $0.50 is rebated per standard lot traded.

---

## **3. Core Feature Details**

### **1. Creating a New Commission Plan**

#### **Procedure**
1. Navigate to **Tiers & Commissions → Commission Plans**  
2. Click **New Commission Plan** in the top-right corner  
3. Enter a descriptive **Plan Name** (e.g., “High Volume IB Plan”)  
4. In the configuration table, define one or more rows with:
   - **Trading Platform**: Select MT5 or TradeWise  
   - **Service Provider**: Choose a specific feed (e.g., `demo\STD:BB`)  
   - **Group Name**: Specify account group (e.g., `demo\ECN:B`)  
   - **Product Type**: Select applicable category (e.g., `Forex`, `Crypto`)  
   - **Spread Rebate**: Enter amount per lot (e.g., 0.5)  
   - **Commission Rebate**: Enter additional rebate (e.g., 0.3)  
5. Toggle the following options as needed:
   - ✅ Upper-level agent can receive spread markup  
   - ✅ Upper-level agent can receive commission markup  
   - ⚠️ Agent does **not** earn rebates on their own trades (applies when acting as an upline)  
6. Click **Save** to finalize

> ✅ Tip: Start with a blank template like `Blank Commission Plan for initial setup`, then customize based on business goals.

---

### **2. Editing an Existing Commission Plan**

#### **Procedure**
1. Locate the target plan (e.g., “High Volume IB Plan”) in the list  
2. Click **Edit**  
3. Adjust any field (e.g., increase Crypto rebate from 0.3 to 0.7)  
4. Click **Save** to apply changes

> ✅ Example: Boosting crypto rebates incentivizes agents to promote digital asset trading during market rallies.

---

### **3. Key Configuration Options Explained**

| Option | Meaning | Use Case |
|--------|--------|----------|
| **Upper-level agent can receive spread markup** | Enables hierarchical spread sharing across agent levels | Standard in multi-tier IB networks |
| **Upper-level agent can receive commission markup** | Allows profit capture from sub-agent commission payments | Ideal for master IBs charging service fees |
| **Agent does not earn rebates on their own trades** | Blocks self-trading from generating rebates | Prevents internal arbitrage and ensures compliance |

> 💡 Recommendation: Test all combinations in a staging environment before production deployment.

---

## **4. Typical Use Cases**

### **Use Case 1: Building a Three-Tier Agent Incentive Structure**

> 🎯 Goal: Implement an “IB → Sub IB → Agent” hierarchy with cascading rebates

- ✅ Implementation:
  1. Create three plans:
     - `IB Commission Plan`: Spread rebate = $0.8/lot, Commission rebate = $0.5/lot  
     - `Sub IB Commission Plan`: Spread rebate = $0.5/lot, Commission rebate = $0.3/lot  
     - `Agent Commission Plan`: Spread rebate = $0.3/lot, Commission rebate = $0.2/lot  
  2. Bind each plan to its corresponding user tier  
  3. Enable “spread markup” to allow flow-through earnings

> ✅ Outcome: Clear, motivating incentives at every level drive organic network growth.

---

### **Use Case 2: Launching a Premium Client Rebate Program**

> 🎯 Goal: Attract high-net-worth clients with enhanced rebates

- ✅ Implementation:
  1. Create `Platinum Client Commission Plan`  
  2. Set all product types to $1.0/lot spread rebate  
  3. Enable “upper-level agent can receive spread markup”  
  4. Assign only to “Platinum” tier clients  
  5. Market it as: “Deposit $10,000+ and enjoy double rebates!”

> ✅ Outcome: Higher conversion and retention among premium clients.

---

### **Use Case 3: Running Targeted Product Promotion Campaigns**

> 🎯 Goal: Incentivize agents to focus on high-potential assets (e.g., cryptocurrencies)

- ✅ Implementation:
  1. Create two plans:
     - `Standard Commission Plan`: Uniform $0.3/lot across all products  
     - `Crypto Boost Plan`: $0.8/lot for `Crypto`, $0.3/lot for others  
  2. Assign `Crypto Boost Plan` to select agents specializing in digital assets  
  3. Monitor performance weekly

> ✅ Outcome: Strategic resource allocation accelerates growth in priority segments.

---

## **5. Best Practices**

| Scenario | Recommendation |
|--------|----------------|
| **Naming Convention** | Use descriptive names (e.g., “High Volume IB Plan” instead of “Plan 1”) |
| **Tier Alignment** | Map plans clearly to user tiers or agent roles to avoid confusion |
| **Monthly Audits** | Review actual rebate payouts vs. expected values |
| **Risk Mitigation** | Always enable “no self-trade rebates” unless explicitly required |
| **Version Control** | Archive or duplicate critical plans before major edits |

---

## **6. Frequently Asked Questions (FAQ)**

### **Q1: Can multiple agents use the same commission plan?**  
- ✅ Yes. A single plan can be assigned to multiple user tiers or individual agent accounts.

---

### **Q2: Do changes to a commission plan affect historical trades?**  
- ❌ No. Past trades are settled under the rules active at the time of execution.  
- ✅ Future trades will follow the updated plan.

---

### **Q3: Can I set zero rebate for a specific product type?**  
- ✅ Yes. Simply set both **Spread Rebate** and **Commission Rebate** to `0` for that row.

---

### **Q4: Why isn’t my agent receiving rebates?**  
- ❌ Possible causes:  
  - “Spread/Commission markup” options are disabled  
  - Downline client isn’t using the correct account group or provider  
  - Trade was canceled or not fully executed  

> ✅ Solution: Verify plan settings, account bindings, and trade status; consult **System Logs** if needed.

---

## **7. Summary**

The **Commission Plans** module is the financial backbone of MIM CRM’s partner ecosystem. It transforms abstract business incentives into precise, automated payout logic—fueling agent motivation, ensuring transparency, and enabling scalable growth. By thoughtfully designing commission structures, organizations can align partner success with platform success.

✅ **Recommended Workflow**:  
1. Go to **Tiers & Commissions → Commission Plans** → 2. Click **New Commission Plan** → 3. Enter name → 4. Configure rebates per product type → 5. Toggle key options → 6. Click **Save**

> 📌 All changes are recorded in the system logs, ensuring full auditability, regulatory compliance, and operational integrity.

---

**Version: v1.0**  
**Last Updated: February 2026**