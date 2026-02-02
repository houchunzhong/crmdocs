# **Currency & Payment**  


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