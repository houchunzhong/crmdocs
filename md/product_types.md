# **Product Types**  


## **1. Module Overview**

The **Product Types** module serves as the **trading instrument organization hub** of MIM CRM. It structures all available financial instruments into meaningful categories (e.g., Forex, Crypto, Commodities), enabling better navigation, targeted marketing, and permission-based access. Key capabilities include:

- ✅ Creating custom product types (e.g., “Forex”, “Crypto”, “Index”)  
- ✅ Assigning specific trading instruments (e.g., `EURUSD`, `BTC/USD:Imax`) to each type  
- ✅ Supporting bulk operations and intuitive drag-and-drop or selection workflows  
- ✅ Integrating with User Tiers and Commission Plans for differentiated access  
- ✅ Offering automatic synchronization with upstream data sources (e.g., MT5, BO, AQX)  

> 🔐 Access is restricted to **System Administrators** or **Operations Managers** only. All changes require explicit saving and are logged in the system audit trail.

---

## **2. Interface Layout**

### **Left Navigation Menu**
| Item | Function |
|------|----------|
| **Tiers & Commissions** | Enter the user tier and commission configuration center |
| - Product Types | View and manage all product categories |
| - Commission Plans | Configure commission structures per tier |
| - Settlement Plans | Set up fund settlement methods |

---

### **Top Action Bar**
| Button | Function |
|--------|----------|
| **New Product Type** | Create a new product category |
| **Sync Products** | Pull the latest list of tradable instruments from connected trading platforms |

---

### **Product Types List View**
| Field | Description |
|-------|-------------|
| **Product Type Name** | Category name (e.g., “Forex”, “Crypto”) |
| **Included Instruments** | Lists all assigned trading symbols (e.g., `EURUSD, GBPUSD`) |
| **Edit** | Modify the contents of this type |
| **Delete** | Remove the type permanently |

> 💡 Example: The `Crypto` type includes instruments like `ETH/USD:Imax` and `BTC/USD:Imax`.

---

## **3. Core Feature Details**

### **1. Synchronize Product Data**

#### **Procedure**
1. Navigate to **Tiers & Commissions → Product Types**  
2. Click the **Sync Products** button in the top-right corner  
3. The system automatically fetches the latest instrument list from connected platforms (e.g., MT5, BO, AQX)  
4. All newly detected or unclassified instruments are grouped under an “Unclassified Products” section for manual assignment

> ⚠️ Notes:  
> - Recommend syncing once daily to avoid redundant loads  
> - If expected instruments are missing, verify platform connectivity or contact support

---

### **2. Create a New Product Type**

#### **Procedure**
1. Click **New Product Type**  
2. In the pop-up window:
   - Enter **Product Type Name** (e.g., “Index”, “Commodities”, “Options”)  
3. From the left panel, select relevant instruments (use search to filter)  
4. Move selected items to the right **Selected Instruments** panel  
5. Click **Confirm** to save

> ✅ Example: When creating an `Index` type, include `JPN225.Imax`, `HK30.Imax`, and `FR40.Imax`.

---

### **3. Edit an Existing Product Type**

#### **Procedure**
1. Locate the target type (e.g., “Crypto”) in the list  
2. Click **Edit**  
3. You may:
   - Add new instruments  
   - Remove existing ones  
   - Rename the type (note: affects front-end display)  
4. Click **Confirm** to apply changes

> ✅ Pro Tip: Use the **search box** to quickly find specific symbols (e.g., type “BTC” to locate Bitcoin pairs).

---

### **4. Delete a Product Type**

#### **Procedure**
1. Click **Delete** next to the target type  
2. Confirm the irreversible deletion in the prompt  
3. Click **Confirm** to complete

> ⚠️ Warning:  
> - All instruments in the deleted type will revert to “Unclassified” status  
> - Existing user accounts remain unaffected, but the category will disappear from front-end menus

---

## **4. Typical Use Cases**

### **Use Case 1: Building a Multi-Asset Trading Portal**

> 🎯 Goal: Offer users a unified platform covering forex, crypto, commodities, and indices

- ✅ Implementation:
  1. Sync all instruments → obtain 220+ unclassified symbols  
  2. Create the following types:
     - `Forex`: `EURUSD`, `GBPUSD`, `USDJPY`  
     - `Crypto`: `BTC/USD:Imax`, `ETH/USD:Imax`  
     - `Commodities`: `XNGUSD`, `XBRUSD`, `XAGUSD`  
     - `Index`: `JPN225.Imax`, `GER30.Imax`, `UK100.Imax`  
  3. Display these categories prominently on the trading dashboard

> ✅ Outcome: A professional, one-stop multi-asset trading experience that boosts platform appeal.

---

### **Use Case 2: Implementing Tiered Access Control**

> 🎯 Goal: Restrict basic clients to major pairs, while granting premium clients access to exotic or volatile assets

- ✅ Implementation:
  1. Create two product types:
     - `Basic Trading`: `EURUSD`, `GBPUSD`, `USDJPY`  
     - `Advanced Trading`: `XAUUSD`, `BTCUSD`, `JPN225`  
  2. In User Tiers settings:
     - `New Client` → granted access only to `Basic Trading`  
     - `Platinum` → granted access to both `Basic` and `Advanced Trading`  
  3. Upon upgrade, the system dynamically expands the user’s available instruments

> ✅ Outcome: Risk-controlled exposure with strong incentive for user progression.

---

### **Use Case 3: Enabling Agent-Customized Promotions**

> 🎯 Goal: Allow IBs to curate specific product sets for their sub-agents or clients

- ✅ Implementation:
  1. Define pre-packaged bundles:
     - `FX Only`: Major currency pairs  
     - `Crypto Focus`: High-volatility digital assets  
     - `Commodity Bundle`: Energy and precious metals  
  2. In the agent portal, add a “Select Recommended Products” feature  
  3. IBs assign a default product type to their recruits  
  4. Sub-agents see only authorized instruments during onboarding

> ✅ Outcome: Greater agent autonomy, higher conversion rates, and improved satisfaction.

---

## **5. Best Practices**

| Scenario | Recommendation |
|--------|----------------|
| **Naming Convention** | Use concise, standard terms (e.g., “Forex” instead of “Currency Pairs”) |
| **Classification Logic** | Group by asset class; avoid overlaps (e.g., don’t place BTC in Forex) |
| **Maintenance Cadence** | Review monthly; archive delisted or inactive instruments |
| **Sync Strategy** | Schedule automated syncs (e.g., nightly) to ensure data freshness |
| **Permission Integration** | Deeply link product types with User Tiers and Agent Levels for dynamic control |

---

## **6. Frequently Asked Questions (FAQ)**

### **Q1: Why don’t some instruments appear in “Unclassified Products”?**  
- ❌ Possible reasons:  
  - Already manually classified  
  - Failed to sync due to platform downtime  
  - Marked as “disabled” or “hidden” in source system  

> ✅ Solution: Re-run **Sync Products**; if still missing, contact technical support.

---

### **Q2: Can one instrument belong to multiple product types?**  
- ❌ No. Each instrument can be assigned to **only one** product type.  
- ✅ Workaround: Create a composite category (e.g., “Popular FX & Crypto”) or use API-level overrides for special cases.

---

### **Q3: Does renaming a product type affect existing users?**  
- ✅ No impact on account functionality or trading permissions.  
- ⚠️ However, the display name changes immediately in the UI—consider notifying users if rebranding.

---

### **Q4: How can I import a large number of products at once?**  
- ✅ Methods:  
  1. Use **Sync Products** to pull the full instrument list  
  2. Future versions will support CSV import/export  
  3. For now, leverage the API to batch-assign instruments programmatically

---

## **7. Summary**

The **Product Types** module is a strategic enabler of **structured product management and personalized trading experiences** in MIM CRM. It transforms a flat list of instruments into an organized, business-aligned taxonomy that powers everything from frontend UX to compliance controls. By thoughtfully designing and maintaining product categories, organizations can deliver clarity, reduce cognitive load, and unlock new operational efficiencies.

✅ **Recommended Workflow**:  
1. Go to **Tiers & Commissions → Product Types** → 2. Click **Sync Products** → 3. Click **New Product Type** → 4. Enter name → 5. Select instruments → 6. Click **Confirm**

> 📌 All changes are recorded in the system logs, ensuring full traceability, transparency, and regulatory readiness.

---

**Version: v1.0**  
**Last Updated: February 2026**