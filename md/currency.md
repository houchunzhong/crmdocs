# **Currency**  

## **1. Module Overview**

The **Currency** module serves as the **multi-currency management hub** of MIM CRM. It defines and maintains the fundamental properties and behavioral rules for every currency used in the system. As the foundational unit for user account balances, trade settlements, and commission payouts, it also underpins cross-currency conversions and financial reconciliation. Through this module, administrators can:

- ✅ Add or edit currency details (name, symbol, type)  
- ✅ Configure exchange rate mechanisms (manual input or automatic fetch)  
- ✅ Set display formatting (decimal places, thousand separators)  
- ✅ Define conversion bases (e.g., USD/GBP, USD/BTC)  

> 🔐 Access is restricted to **Administrators** or **Finance Managers** only. All changes require explicit saving and are logged for audit purposes.

---

## **2. Interface Layout**

### **Left Navigation Menu**
| Item | Function |
|------|----------|
| **Currency** | View and manage all currency configurations |
| **Payment Channels** | Configure third-party payment gateways (e.g., banks, PayPal, Stripe) |

---

### **Top Tab Bar**
| Tab | Description |
|-----|-------------|
| **Overview** | Return to parent page |
| **Currency** | Current page |
| **Currency - EUR** | Edit Euro currency settings |
| **Payment Channels** | Navigate to payment gateway configuration |

---

## **3. Core Feature Details**

### **1. Currency List View**

#### **Function Description**  
Displays all configured currencies in a table for quick review and editing.

#### **Field Definitions**
| Field | Description |
|-------|-------------|
| **Currency Code** | Short code (e.g., `EUR`, `BTC`), with icon indicator |
| **Currency Name** | Full name (e.g., “Euro”, “Bitcoin”) |
| **Currency Type** | Classification:  
  - **Fiat Currency**: e.g., EUR, USD, GBP  
  - **Digital Currency**: e.g., BTC, USDT, USDC |
| **Display Decimal Places** | Number of decimals shown to users (e.g., 2 → $1.00) |
| **Quotation Method** | How exchange rates are updated:  
  - **Manual**: Admin-entered values  
  - **Automatic**: Fetched in real time from external APIs (for crypto) |
| **Conversion Pair** | Base pair for conversion (e.g., `EUR/USD` means USD is the base) |
| **Deposit Rate** | Exchange rate applied during deposits (e.g., 1 EUR = 1.1917 USD) |
| **Withdrawal Rate** | Exchange rate applied during withdrawals (e.g., 1 EUR = 1.1896 USD) |
| **Edit** | Opens the configuration form for this currency |

> 💡 Example: BTC uses “Automatic” quotation, meaning its price syncs in real time from a crypto market data API.

---

### **2. Adding or Editing a Currency**

#### **Function Description**  
Click **Add New** or **Edit** to open a detailed configuration form.

#### **Configuration Fields**
| Field | Description |
|-------|-------------|
| **Currency Code** | Required, unique identifier (e.g., `USDT`) |
| **Currency Name** | Display name (e.g., “Tether”) |
| **Currency Type** | Select: Fiat or Digital Currency |
| **Thousand Separator** | Symbol for grouping thousands (e.g., `,` or `.`) |
| **Storage Precision** | Internal decimal precision (usually matches display setting) |
| **Display Decimal Places** | Minimum display unit for end users (e.g., 2 → two decimals) |
| **Decimal Point Symbol** | Character used for decimals (e.g., `.` or `,`) |
| **Conversion Pair** | Base conversion pair (e.g., `USDT/USD`) |
| **Quotation Method** | Choose: Manual or Automatic |
| **Deposit Rate** | Must be > 0; used when users deposit funds |
| **Withdrawal Rate** | Must be ≤ Deposit Rate; used when users withdraw |

> ⚠️ Notes:  
> - If **Quotation Method** is “Automatic,” the deposit/withdrawal rates are ignored—real-time rates apply.  
> - The **Conversion Pair** determines how this currency links to others (e.g., EUR → USD → BTC).

---

### **3. Operational Workflow Examples**

#### **Scenario: Adding USDT as a New Currency**
1. Go to **Currency** → Click **Add New**  
2. Fill in:
   - Currency Code: `USDT`  
   - Currency Name: `Tether`  
   - Type: `Digital Currency`  
   - Display Decimals: `2`  
   - Quotation Method: `Manual`  
   - Conversion Pair: `USDT/USD`  
   - Deposit Rate: `1.00003`  
   - Withdrawal Rate: `0.99998`  
3. Click **Save**  
4. USDT now appears in the list and becomes available for deposits, withdrawals, and settlements

---

#### **Scenario: Switching BTC to Automatic Pricing**
1. Find `BTC` in the currency list → Click **Edit**  
2. Change **Quotation Method** to **Automatic**  
3. Save  
4. System now pulls live BTC/USD prices from the configured API  
5. All future BTC transactions use real-time market rates

---

## **4. Best Practices**

| Scenario | Recommendation |
|--------|----------------|
| **Multi-Currency Support** | Prioritize major fiat (EUR, USD, GBP) and stablecoins (USDT, USDC) |
| **Rate Management** | Use **Manual** for fiat (to control costs); **Automatic** for crypto (to reflect market value) |
| **UI Consistency** | Standardize thousand separators and decimal symbols globally |
| **Risk Control** | Maintain a small spread between deposit/withdrawal rates (e.g., 0.1%–0.5%) to prevent arbitrage |
| **Regulatory Compliance** | Only enable currencies permitted under local financial regulations |

---

## **5. Frequently Asked Questions (FAQ)**

### **Q1: Why is the “Withdrawal Rate” missing for some currencies?**  
- ❌ Possible reasons:  
  - Withdrawals are not enabled for this currency  
  - The field was left blank during setup  

> ✅ Solution: Edit the currency and enter a valid withdrawal rate.

---

### **Q2: How does “Automatic” quotation work?**  
- ✅ The system calls a pre-configured external API (e.g., CoinGecko, Binance) to fetch real-time prices.  
- Requires prior setup in **System Settings → External Services** with valid API keys.

---

### **Q3: Can I delete an existing currency?**  
- ❌ Direct deletion is not allowed.  
- ✅ Workaround: Disable the currency (stop accepting deposits/withdrawals) or contact technical support for database-level cleanup.

---

### **Q4: How to ensure consistent exchange rates across accounts?**  
- ✅ Best approach:  
  1. Align all **Conversion Pairs** to a single base currency (e.g., USD)  
  2. Use **Automatic** quotation where possible  
  3. Regularly audit deposit/withdrawal rates for reasonableness

---

## **6. Summary**

The **Currency** module is the cornerstone of MIM CRM’s global, multi-currency operations. By enabling granular control over each currency’s attributes and behavior, it ensures accurate handling of cross-border fund flows, dynamic settlement logic, and consistent user experiences. Whether expanding into new markets, integrating stablecoins, or refining financial models, this module delivers both flexibility and governance.

✅ **Recommended Workflow**:  
1. Go to **Currency** → 2. Click **Add New** → 3. Enter basic info → 4. Configure rates & quotation method → 5. Click **Save** → 6. Link to relevant **Payment Channels**

> 📌 All changes are logged in the system audit trail, supporting transparency, compliance, and financial integrity.

---

**Version: v1.0**  
**Last Updated: February 2026**