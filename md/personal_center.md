# **Personal Center Module: Functionality and User Guide**  

## **1. Module Overview**

The **Personal Center** serves as a key user-facing dashboard after login, integrating three core dimensions: **identity**, **finance**, and **security**. It empowers users to independently manage daily account operations while remaining compliant with regulatory requirements.

### **Core Sub-Modules**
- ✅ **My Profile**: View and update personal identity information  
- ✅ **Funding Accounts**: Register and manage deposit/withdrawal accounts  
- ✅ **Security Settings**: Configure authentication and password policies  
- ✅ **Activity Log**: Review audit trails of critical actions  

> 🔐 All sensitive operations (e.g., modifying ID details, deleting withdrawal accounts) require secondary verification and trigger system notifications.

---

## **2. Interface Layout**

### **Left Navigation Menu**
| Item | Function |
|------|----------|
| **My Profile** | View name, nationality, contact info, KYC status, etc. |
| **Funding Accounts** | Manage bank accounts, digital wallets, and third-party payment methods |
| **Security Settings** | Change password, enable 2FA, review active sessions |
| **Activity Log** | Access operation history from the past 90 days |

---

### **Top Status Bar**
- Displays current user role (e.g., `Verified Client`, `IB Level 2`)  
- Shows real-time main wallet balance (supports multi-currency toggle)  
- Quick access: Message Center, Help Docs, Sign Out

---

## **3. Core Function Details**

### **1. My Profile**

#### **Function Description**  
Displays KYC-verified identity information and allows updates to non-critical fields (e.g., email, phone number) within compliance boundaries.

#### **Field Permissions**
| Field | Editable? | Notes |
|-------|-----------|-------|
| Full Name | ❌ | Locked to official ID; cannot be changed |
| Nationality / Residence Country | ❌ | Fixed after KYC approval |
| Phone Number | ✅ (with verification) | Requires SMS code confirmation |
| Email Address | ✅ (with verification) | Requires email link activation |
| User Tier | ❌ | Automatically assigned (based on trading volume or IB network size) |
| KYC Status | ❌ | Shows `Verified` + last review timestamp |
| Source | ❌ | Indicates `User Submitted` or `System Imported` |

#### **Workflow**
1. Click **“Edit”** (only enabled for editable fields).  
2. Enter new phone/email.  
3. System sends a verification code to the original device.  
4. User enters the code and saves changes.  
5. Update is logged, and a notification is sent.

> ⚠️ Note: To change legal name or ID documents, users must resubmit a full KYC application for manual review.

---

### **2. Funding Accounts**

#### **Function Description**  
Allows users to register and manage accounts for deposits and withdrawals, including bank cards, crypto wallets, and e-payment services.

#### **Supported Account Types**
- 💳 **Bank Accounts** (multi-currency: USD, EUR, GBP, etc.)  
- 🪙 **Digital Wallets** (USDT-TRC20, USDT-ERC20, BTC, ETH)  
- 📱 **Third-Party Payments** (Alipay, WeChat Pay, Skrill)

#### **Field Details**
| Field | Description |
|-------|-------------|
| Account Type | Auto-detected (e.g., “USDT-TRC20”) |
| Beneficiary Name | Must exactly match KYC-verified name |
| Account / Wallet Address | Partially masked for privacy (e.g., `****1234`) |
| Currency | e.g., USD, USDT |
| Country | Jurisdiction of the account |
| Status | `Pending Review` / `Verified` / `Disabled` |
| Actions | **Set as Default** / **Edit** / **Delete** |

#### **Workflow**
1. Click **“Add New Account”**.  
2. Select type and fill in details.  
3. Submit → status becomes `Pending Review`.  
4. Compliance team approves → status updates to `Verified`.  
5. User may designate any verified account as the **default withdrawal account**.

> 💡 Recommendation: Assign at least one default account per currency to avoid withdrawal failures.

---

### **3. Security Settings**

#### **Function Description**  
Enhances account protection against unauthorized access.

#### **Sub-Features**
| Feature | Description |
|--------|-------------|
| **Change Password** | Requires old password + new password (8+ chars, upper/lower/digit) |
| **Two-Factor Authentication (2FA)** | Supports Google Authenticator or SMS |
| **Active Sessions** | View and remotely log out devices |
| **Security Questions** | (Optional) Set recovery questions |

#### **Example: Enabling 2FA**
1. Click **“Enable Google Authenticator”**.  
2. Scan QR code with Authenticator app.  
3. Enter the 6-digit code.  
4. System confirms: “2FA Enabled.” Future logins require this code.

> 🔒 Policy: 2FA is **mandatory** for all IBs and admin-level accounts.

---

### **4. Activity Log**

#### **Function Description**  
Provides transparent, auditable records of user actions for self-review and compliance.

#### **Log Fields**
| Field | Example |
|-------|---------|
| Action Type | `Login`, `Email Updated`, `Withdrawal Requested` |
| Timestamp | `2026-01-27 14:30:22` |
| IP Address | `114.242.xxx.xxx (Beijing, CN)` |
| Device | `Chrome on Windows` |
| Status | `Success` / `Failed (Invalid Password)` |

#### **Use Cases**
- Suspect account breach? → Check for unfamiliar IPs  
- Forgot if withdrawal was submitted? → Search “Withdrawal”  
- Support investigation? → Export logs as CSV  

> 📌 Retention: Logs are stored for **180 days**, aligning with financial industry standards.

---

## **4. Design Principles & UX Guidelines**

### **1. Consistency**
- Follows MIM CRM’s global design system:
  - Primary color: Navy (#0A2540) + Tech Blue (#007BFF)
  - Icons: Minimalist line style (👤, 💳, 🔒)
  - Buttons: Rounded rectangles with clear primary actions

### **2. Security-First**
- Sensitive data auto-masked (e.g., card numbers as `****1234`)
- Critical actions require double confirmation (modal + OTP)
- All pages enforce HTTPS + session timeout (auto-logout after 15 mins of inactivity)

### **3. Self-Service Focus**
- 90% of routine tasks require no support ticket
- Each page includes a **“?” help icon** linking to relevant FAQs
- Error messages are user-friendly (e.g., “Invalid phone format. Please enter an 11-digit number starting with +86.”)

### **4. Multilingual Support**
- UI language auto-switches based on user preference (EN, ZH, JA, ID, etc.)
- Date/number formats localized (e.g., `1,000.00` vs `1.000,00`)

---

## **5. Best Practices**

| Scenario | Recommendation |
|--------|----------------|
| **First Login** | Immediately bind phone + email + enable 2FA |
| **New Device** | Log out old sessions to prevent conflicts |
| **Adding Withdrawal Account** | Use only accounts under your legal name |
| **Suspicious Activity** | Change password immediately + contact support to freeze account |

---

## **6. Frequently Asked Questions (FAQ)**

### **Q1: Why can’t I edit my name?**  
- Your name is locked after KYC approval. To change it, you must resubmit official ID documents for manual review.

### **Q2: Can I recover a deleted withdrawal account?**  
- ❌ No. Deletion is permanent. You must re-register and undergo review again.

### **Q3: Can I export my activity log?**  
- ✅ Yes. Click **“Export CSV”** to download an encrypted ZIP file (requires transaction password to unzip).

### **Q4: I lost access to my 2FA device—what now?**  
- Contact support with ID proof and recent transaction records. After manual verification, they can reset your 2FA.

---

## **7. Summary**

The **Personal Center** module in MIM CRM embodies the principles of **security, transparency, and efficiency**. By transforming complex compliance requirements into intuitive self-service workflows, it gives users full control over their account lifecycle while meeting global regulatory standards for data sovereignty and auditability.

✅ **Recommended Onboarding Flow**:  
1. Complete contact info → 2. Set default funding accounts → 3. Enable 2FA → 4. Regularly review activity log

> 📌 All features comply with GDPR, AML directives, and local data protection laws.

---

**Version: v1.0**  
**Last Updated: January 2026**