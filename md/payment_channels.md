# **Payment Channels**  

## **1. Module Overview**

The **Payment Channels** module serves as the **funds flow control center** of MIM CRM. It defines and maintains all available pathways for fund inflows and outflows. It directly impacts how users deposit funds into their accounts or withdraw profits, influencing user experience, transaction efficiency, and anti-money laundering (AML) risk management. Through this module, administrators can:

- ✅ Add or edit payment methods (e.g., BankTransfer, Skrill, Crypto)  
- ✅ Configure supported currencies, fee rates, transaction limits, and settlement timeframes  
- ✅ Set payment direction (deposit/withdrawal), linked wallets, and platform compatibility  
- ✅ Optimize display order to prioritize preferred options for users  

> 🔐 Access is restricted to **Administrators** or **Finance Managers** only. All changes require explicit saving and are logged for audit purposes.

---

## **2. Interface Layout**

### **Left Navigation Menu**
| Item | Function |
|------|----------|
| **Payment Channels** | View and manage all payment method configurations |
| **Currency** | Configure supported currency types |

---

### **Top Tab Bar**
| Tab | Description |
|-----|-------------|
| **Overview** | Return to parent page |
| **Payment Channels** | Current page |
| **Payment Channels - BankTransfer - Offline** | View details of a specific channel |

---

## **3. Core Feature Details**

### **1. Payment Channels List View**

#### **Function Description**  
Displays all configured payment channels in a table for quick review and action.

#### **Field Definitions**
| Field | Description |
|-------|-------------|
| **ID** | Unique identifier (e.g., `5`) |
| **Display Name** | Name shown to users (e.g., “BankTransfer - Offline”) |
| **Sort Order** | Determines front-end display priority (lower number = higher priority) |
| **Status** | Current availability:  
  - 🟩 **Enabled**: Active and usable  
  - 🔴 **Disabled**: Temporarily suspended |
| **Direction** | Fund flow type:  
  - **Deposit**: User → Platform (inbound)  
  - **Withdrawal**: Platform → User (outbound) |
| **Supported Currencies** | Currencies accepted (e.g., USD, GBP, EUR) |
| **Supported Platforms** | Applicable trading systems (e.g., MT5, BO, AQX) |
| **Wallet** | Associated wallet type (e.g., MT5&AQX Wallet, BO Wallet) |
| **Fee Rate** | Transaction fee percentage (e.g., 1%) |
| **Min per Transaction (USD)** | Minimum allowed amount per transaction (in USD equivalent) |
| **Max per Transaction (USD)** | Maximum allowed amount per transaction (in USD equivalent) |
| **Actions** | Two buttons:  
  - **View**: Open detailed configuration  
  - **Parameters**: Access advanced field settings |

> 💡 Example: `Skrill - Paymentgateway` is a **Withdrawal** channel supporting USD and GBP on MT5, with a 1% fee and a $50,000 max limit.

---

### **2. Payment Channel Detail Page**

#### **Function Description**  
Clicking **View** opens a full configuration panel for the selected channel.

#### **Configuration Fields**
| Field | Description |
|-------|-------------|
| **Logo** | Icon displayed to users (e.g., Skrill’s purple logo) |
| **Display Name** | User-facing name (e.g., “Crypto - Payment”) |
| **Sort Order** | Front-end display sequence |
| **Status** | Enabled or Disabled |
| **Direction** | Deposit or Withdrawal |
| **Supported Currencies** | List of accepted currencies (e.g., USDT, USDC) |
| **Supported Platforms** | Compatible trading systems (MT5, BO, AQX) |
| **Wallet** | Linked wallet (e.g., MT5&AQX Wallet) |
| **Channel Type** | Classification: Online / Offline (T/T) |
| **Payment Method** | Specific mechanism (e.g., “Bank Wire (T/T)”) |
| **Estimated Settlement Time** | Expected time for funds to arrive (e.g., “1 hour”, “2 days”) |
| **Fee Rate** | Percentage charged per transaction (e.g., 2%) |
| **Fee Bearer** | Who pays the fee:  
  - User  
  - Platform |
| **Channel Min (USD)** | System-level minimum transaction amount |
| **Channel Max (USD)** | System-level maximum transaction amount |
| **User Min (USD)** | Minimum input allowed on user interface (≤ Channel Min) |
| **User Max (USD)** | Maximum input allowed on user interface (≤ Channel Max) |
| **Admin Notes (Internal Only)** | Internal remarks not visible to users (e.g., “test”, “3”) |

> ⚠️ Note:  
> - “User Min/Max” applies to front-end validation; “Channel Min/Max” enforces backend processing limits  
> - If “Fee Bearer” is **Platform**, users pay no fee

---

### **3. Parameters Configuration Page**

#### **Function Description**  
Clicking **Parameters** opens an advanced form to define custom fields and values used during payment processing.

#### **Typical Use Cases**
- **Bank Transfer (T/T)**: Configure recipient account details (bank name, account number, SWIFT/BIC)  
- **Cryptocurrency Payments**: Set wallet address, network type (ERC-20, TRC-20), etc.

#### **Field Example (Crypto - Payment)**
| Order | Field | Value |
|-------|-------|-------|
| 1 | Bank Name | Bank of America |
| 2 | Account Number | 1234567890 |
| 3 | SWIFT/BIC | BOFAUS3N |
| 4 | Beneficiary Name | TradeWise Limited |

> 💡 Operation: Add, delete, or modify fields as needed. Click **Confirm** to save.

---

## **4. Operational Workflow Examples**

### **Scenario: Adding a New Channel — “Crypto - Tron”**

1. Go to **Payment Channels** → Click **Add New**  
2. Fill in basic info:
   - Display Name: `Crypto - Tron`  
   - Sort Order: `7`  
   - Status: `Enabled`  
   - Direction: `Deposit`  
   - Supported Currencies: `USDC`, `USDT`  
   - Supported Platforms: `BO`  
   - Wallet: `MT5&AQX Wallet`  
   - Fee Rate: `0%`  
   - User Min: `500`  
   - User Max: `10,000`  
3. Click **Save**  
4. Go to **Parameters** and configure TRON network details:
   - Field: `Wallet Address` → Value: `TJ...abc123`  
   - Field: `Network Type` → Value: `TRC-20`  
5. Click **Confirm** to complete setup  

> ✅ Users can now select “Crypto - Tron” to deposit USDC/USDT via the BO platform.

---

### **Scenario: Updating Skrill Withdrawal Fee**

1. Locate `Skrill - Paymentgateway` → Click **View**  
2. On detail page, change **Fee Rate** to `1.5%`  
3. Click **Edit** → **Save**  
4. All future Skrill withdrawals will apply the new rate

---

## **5. Best Practices**

| Scenario | Recommendation |
|--------|----------------|
| **Multi-Currency Support** | Prioritize major fiat (USD, EUR, GBP) and stablecoins (USDT, USDC) |
| **Fee Strategy** | Offer “Platform Pays Fee” for high-value clients to enhance experience |
| **Settlement Clarity** | Clearly state expected arrival times to reduce user inquiries |
| **Security** | Bind all offline payments to verified, real-name bank accounts to mitigate AML risk |
| **Regulatory Compliance** | Ensure all channels comply with local financial regulations (e.g., no unlicensed virtual assets) |

---

## **6. Frequently Asked Questions (FAQ)**

### **Q1: Why is a payment channel unavailable?**  
- ❌ Possible reasons:  
  - Status is **Disabled**  
  - Not available in the user’s region  
  - Missing valid wallet or API credentials  

> ✅ Solution: Verify status, geo-restrictions, and wallet/API setup.

---

### **Q2: What’s the difference between “Deposit” and “Withdrawal”?**  
- ✅ **Deposit**: User sends funds **to** the platform (inbound)  
- ✅ **Withdrawal**: Platform sends funds **to** the user (outbound)  

> 💡 Example: Skrill is typically a **Withdrawal** channel; BankTransfer is often a **Deposit** channel.

---

### **Q3: Can multiple payment methods be active at once?**  
- ✅ Yes. The system supports concurrent channels, allowing users to choose their preferred option.

---

### **Q4: How do I set a cryptocurrency wallet address?**  
- ✅ Steps:  
  1. Go to the channel → Click **Parameters**  
  2. Add field: `Wallet Address` → Enter valid address  
  3. Optional: Add `Network Type` (e.g., ERC-20, TRC-20)  
  4. Save

---

### **Q5: Do payment channels affect commission calculations?**  
- ✅ Yes. If a channel is used for **deposits**, its fees may reduce the net deposited amount, which in turn affects agent commission accruals. Consider cost implications during configuration.

---

## **7. Summary**

The **Payment Channels** module is the cornerstone of MIM CRM’s global, diversified fund flow infrastructure. By enabling granular control over each payment method’s attributes and rules, it meets diverse user needs while balancing efficiency, security, and compliance. Whether integrating traditional bank wires, third-party gateways, or cryptocurrency networks, this module delivers robust flexibility and governance.

✅ **Recommended Workflow**:  
1. Go to **Payment Channels** → 2. Click **Add New** → 3. Enter basic info → 4. Set currencies, fees, and limits → 5. Click **Save** → 6. Go to **Parameters** to configure custom fields → 7. Click **Confirm**

> 📌 All changes are logged in the system audit trail, supporting transparency, compliance, and financial integrity.

---

**Version: v1.0**  
**Last Updated: February 2026**