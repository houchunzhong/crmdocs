# **KYC Verification Module Configuration and User Guide**  
**My Investment Markets (MIM) CRM System**

This document provides a detailed overview of the **KYC Verification Module** in the MIM CRM system, including its functional architecture, operational workflows, and configuration guidelines. It is intended for administrators, compliance officers, and finance personnel responsible for managing user identity verification and withdrawal account validation—critical components of regulatory compliance.

---

## **1. Module Overview**

The **KYC Verification Module** is a core compliance component of the MIM CRM, ensuring all users complete identity verification before trading or withdrawing funds. The module supports three key functions:

- ✅ **Pending Users**: Review new user KYC submissions  
- ✅ **Pending Withdrawal Accounts**: Validate user-submitted payout account details  
- ✅ **All Users / All Withdrawal Accounts**: View complete records of approved, rejected, or pending cases

> 🔐 All verification actions must be performed by authorized administrators, and full audit logs are retained to meet regulatory requirements.

---

## **2. Interface Layout Explanation**

### **Left Sidebar Navigation**
| Item | Function |
|------|----------|
| **All Users** | View all user records (approved, rejected, pending) |
| **Pending Users (9)** | Displays users awaiting manual KYC review |
| **Pending Withdrawal Accounts (148)** | Shows withdrawal accounts pending validation |
| **All Withdrawal Accounts** | View all submitted withdrawal account records |

---

### **Top Filtering Toolbar**
Multi-dimensional filters enable rapid identification of specific review items:

| Field | Description |
|-------|-------------|
| **KYC Status** | Options: `Pending`, `Verified`, `Rejected` |
| **Nationality** | Filter by country (e.g., China, Singapore, USA) |
| **Registration Time From ～ To** | Set date range |
| **Search by ID/Name/Mobile/Email** | Supports fuzzy search |

---

## **3. Core Function Details**

### **1. Pending Users**

#### **Function Description**
Displays all users who have submitted KYC documentation but await manual verification. The system automatically collects uploaded identity documents (e.g., passport, national ID, driver’s license) and proof of address (e.g., utility bill).

#### **Field Descriptions**
| Field | Description |
|-------|-------------|
| **User** | Username + User ID (e.g., `zhizhizhi 17974`) |
| **KYC Status** | Current status:<br>🟢 `Verified`<br>🟡 `Pending`<br>🔴 `Rejected` |
| **Nationality** | User nationality (with flag icon) |
| **Residence Country** | Actual country of residence (may differ from nationality) |
| **Mobile / Email** | Contact info with verification badges:<br>✅ Verified<br>⚠️ Unverified |
| **User Level** | E.g., `Client`, `Verified Client`, `IB` |
| **Source** | Submission method: `User Submitted` or `System Imported` |
| **Registration Time** | Account creation timestamp |
| **Submission Time** | When KYC documents were uploaded |
| **Last Reviewed Time** | Timestamp of most recent review |
| **Action** | Buttons: **Review** or **View** |

#### **Operation Workflow**
1. Click **"Review"** to open the detail page.
2. Inspect uploaded documents (e.g., front/back of passport, address proof).
3. Verify authenticity:
   - Is it the user themselves?
   - Is the document within validity period?
   - Is the image clear and unaltered?
4. Select outcome:
   - ✅ **Approve** → User upgraded to `Verified Client`
   - ❌ **Reject** → Provide reason and notify user to resubmit
5. Save changes; system updates status and sends notification.

> ⚠️ Note: A clear rejection reason must be provided to avoid disputes.

---

### **2. Pending Withdrawal Accounts**

#### **Function Description**
Used to validate user-bound withdrawal accounts, including bank cards, digital wallets (e.g., USDT addresses), Alipay, WeChat Pay, etc. Ensures payee name, account number, currency, and country match to mitigate money laundering risks.

#### **Field Descriptions**
| Field | Description |
|-------|-------------|
| **User ID** | Unique identifier (e.g., `17753`) |
| **Review Status** | Current state:<br>🟡 `Pending`<br>🟢 `Approved`<br>🔴 `Rejected` |
| **Beneficiary Name** | Name on bank card or wallet |
| **Currency** | E.g., USD, EUR, GBP, USDT, USDC |
| **Type** | Payment method:<br>Bank Transfer<br>Digital Wallet<br>Third-Party Payment |
| **Account / Wallet Address** | Actual payout info (e.g., bank account, blockchain address) |
| **Country** | Country of the withdrawal account |
| **Submission Time** | When the account was submitted |
| **Action** | Buttons: **Review** or **View** |

#### **Operation Workflow**
1. Click **"Review"** to access details.
2. Cross-check consistency:
   - Does the beneficiary name match the user’s verified name?
   - Is the bank account format valid?
   - Is the wallet address active and correctly formatted?
3. Choose result:
   - ✅ **Approve** → Account becomes eligible for withdrawals
   - ❌ **Reject** → Specify reason and prompt user to correct
4. Save; system syncs status to user profile.

> 💡 Recommendation: Apply enhanced manual review for high-value or high-risk accounts (e.g., crypto wallets, offshore banks).

---

### **3. All Users / All Withdrawal Accounts**

#### **Function Description**
Provides a complete historical archive of user and withdrawal account records for auditing, reporting, and compliance checks.

#### **Use Cases**
- Daily reconciliation and data export
- Preparation for regulatory inspections
- Internal performance analysis (e.g., IB client KYC approval rates)

#### **Supported Actions**
- Export to Excel
- Filter by status, nationality, time range, etc.
- View historical review logs

---

## **4. KYC Status Definitions**

| Status | Meaning | Impact on User |
|--------|--------|----------------|
| **Pending** | Documents submitted, awaiting review | Cannot trade or withdraw |
| **Verified** | Approved; information confirmed valid | Full trading & withdrawal access |
| **Rejected** | Incomplete, invalid, or fraudulent submission | Must resubmit; repeated failures may lead to account suspension |

---

## **5. Best Practices**

| Item | Recommendation |
|------|----------------|
| **Access Control** | Restrict review permissions to compliance team or designated admins |
| **Dual Approval** | Enable two-person review for high-risk or high-value accounts |
| **Backlog Management** | Regularly clear aged pending applications to avoid delays |
| **Automated Alerts** | Configure email/in-app reminders for pending tasks |
| **Record Retention** | Archive all KYC records for at least 5 years per AML regulations |

---

## **6. Frequently Asked Questions (FAQ)**

### **Q1: A user submitted KYC and shows “Pending”—how long should review take?**  
- Aim to complete reviews within **24 hours** to enhance user trust and experience.

### **Q2: Can users submit photocopies of IDs?**  
- ❌ Not recommended. Only original scans or high-resolution photos showing anti-forgery features are acceptable.

### **Q3: If a user updates their withdrawal account, does it need re-verification?**  
- ✅ Yes. Every new or modified withdrawal account must undergo full review.

### **Q4: How to process multiple users efficiently?**  
- Use the “All Users” page to filter and export records to Excel, then batch-process or escalate for approval.

---

## **7. Summary**

The **KYC Verification Module** in MIM CRM delivers a standardized, transparent, and auditable workflow for identity and fund security validation across the entire user lifecycle—from registration to withdrawal. With proper configuration and disciplined execution, organizations can significantly reduce compliance risk, improve operational efficiency, and satisfy global financial regulatory standards.

✅ **Recommended Workflow**:  
1. Receive submission → 2. Inspect documents → 3. Verify accuracy → 4. Approve/Reject → 5. Notify user → 6. Archive record

> 📌 All actions must strictly adhere to your company’s **Anti-Money Laundering (AML) Policy** and applicable local laws.

---

**Version: v1.0**  
**Last Updated: January 2026**
