# **Agent Applications Module: User Guide**  

## **1. Module Overview**

The **Agent Applications** module functions as the **agent onboarding control center** of MIM CRM. It captures and manages all “Become an Agent” requests submitted by users. The system automatically populates a pending-review list with complete profile and KYC data, enabling administrators to assess eligibility before granting IB status. This ensures only qualified, trustworthy users are authorized as agents—mitigating fraud risks and regulatory exposure.

> 🔐 Access is restricted to **Administrators** or **Operations Managers** only. All approval actions are logged for full auditability and transparency.

---

## **2. Interface Layout**

### **Left Navigation Menu**
| Item | Function |
|------|----------|
| **Agent Applications** | View all pending IB applications |
| **Agent List** | Manage approved agents |
| **Order Commissions** | Inspect per-trade commission details |
| **Commission Records** | Review historical commission accruals |
| **Commission Payout Records** | Track processed commission settlements |

---

### **Top Tab Bar**
| Tab | Description |
|-----|-------------|
| **Overview** | Return to parent page |
| **Pending Withdrawals** | View withdrawal orders awaiting processing |
| **Agent Applications** | Current page |

---

## **3. Core Feature Details**

### **1. Agent Applications Main View**

#### **Function Description**  
Displays all unprocessed agent applications in a sortable, filterable table for efficient batch management and prioritization.

#### **Field Definitions**
| Field | Description |
|-------|-------------|
| **User ID** | Unique system identifier (e.g., `16686`) |
| **Name** | Display name (e.g., `Léa Petit`), with status indicators:  
  - ✅ **Green ✓**: Profile fully completed  
  - ⚠️ **Orange !**: Incomplete information (e.g., “Not filled”) |
| **Nationality** | Country declared during registration |
| **Residence** | Current place of residence (may differ from nationality) |
| **Phone** | Contact number, with verification badge:  
  - ✅ **Green ✓**: Verified phone |
| **Email** | Registered email, with verification badge:  
  - ✅ **Green ✓**: Verified email |
| **User Tier** | Current account type (e.g., `Verified Client`) |
| **Registration Time** | When the user first created their account |
| **Application Time** | Exact timestamp of IB application submission |
| **Actions** |  
  - **View**: Open user’s full profile  
  - **Set as Agent**: Initiate approval workflow |

#### **Interactive Controls**
- 🔎 **Search Bar**: Global search by `ID`, `name`, `phone`, or `email`.  
- 📆 **Date Filter**: Set “Submission From” to “To” to narrow by time range.  
- 📊 **Sorting**: Click column headers to sort ascending/descending (e.g., newest applications first).

> 💡 Example: A user registered in France with verified contact info demonstrates higher credibility—ideal for priority review.

---

### **2. “Set as Agent” Approval Workflow**

#### **Function Description**  
Clicking **“Set as Agent”** opens a configuration modal where administrators assign the applicant’s agent role, tier, and commission plan—completing formal authorization.

#### **Configuration Fields**
| Field | Description |
|-------|-------------|
| **User Type** | Fixed as “Agent” (non-editable) |
| **User Tier** | Required selection:  
  - `IB` (Introducing Broker) — standard entry-level agent  
  - Higher tiers (e.g., Master IB) can be assigned later |
| **Plan Type** | Determines commission logic:  
  - `Inherit from User Tier`: Uses system-default or superior’s plan  
  - `Custom Plan`: Applies a pre-configured bespoke rebate scheme |

#### **Approval Steps**
1. Locate target applicant (e.g., Léa Petit) in the **Agent Applications** list  
2. Click **“Set as Agent”**  
3. In the modal:  
   - Select **User Tier** (e.g., `IB`)  
   - Choose **Plan Type** (e.g., `Inherit from User Tier`)  
4. Click **“Confirm”** to finalize

> ✅ Upon success, the user will:  
- Be upgraded to **IB** role  
- Appear in the **Agent List**  
- Receive a unique **referral code** and **referral link**  
- Begin earning commissions from referred clients

---

### **3. User Detail Page (For Review Reference)**

#### **Function Description**  
Clicking **“View”** opens the applicant’s full profile, providing comprehensive background data to support approval decisions.

#### **Key Information Categories**
| Category | Content |
|--------|--------|
| **Basic Info** | Name, nationality, residence, registration time |
| **Contact Details** | Phone and email (with verification status) |
| **Financial Activity** | Total deposits, withdrawals, assets, available balance |
| **KYC Status** | Whether identity documents (e.g., passport) have been verified |
| **Two-Factor Authentication (2FA)** | Indicates if enhanced security is enabled |
| **Referrer Info** | If applicable, shows who introduced this user |
| **Referral Code / Link** | Unique promotional identifiers |

> 📌 Example: Léa Petit’s profile shows she is from France, has verified contacts, $500 in deposits, and passed KYC—making her a strong IB candidate.

---

## **4. Best Practices**

| Scenario | Recommendation |
|--------|----------------|
| **New Application Review** | Prioritize applicants with complete profiles, verified contacts, and deposit history |
| **Risk Identification** | Delay approval for users with missing names, no deposits, or unverified KYC |
| **Batch Processing** | Conduct daily reviews to prevent backlog |
| **Compliance Requirement** | Enforce KYC completion as mandatory for all agents |
| **Onboarding Engagement** | Send a welcome email post-approval explaining IB benefits and commission mechanics |

---

## **5. Frequently Asked Questions (FAQ)**

### **Q1: Why is the “Set as Agent” button missing for some users?**  
- ❌ Possible reasons:  
  - User hasn’t submitted an application (not in this list)  
  - Already approved (appears in “Agent List”)  
  - Flagged as high-risk (e.g., blacklisted, KYC rejected)

### **Q2: Can I change a confirmed agent’s commission plan later?**  
- ✅ Yes. Go to **Agent List** → Open agent profile → Edit “Commission Plan” in the **Agent Details** tab.

### **Q3: Can users reapply after rejection?**  
- ✅ Yes. The system allows resubmission. Recommend guiding users to improve their profile before reapplying.

### **Q4: How to prevent fake agent applications?**  
- ✅ Recommended measures:  
  - Enforce mandatory KYC  
  - Require real-name registration  
  - Verify trading activity  
  - Set minimum deposit threshold (e.g., $100)

### **Q5: Do applications expire automatically?**  
- ❌ No. Pending applications remain indefinitely. Regular cleanup is advised.

---

## **6. Summary**

The **Agent Applications** module standardizes the journey from “user request” to “authorized agent,” ensuring a secure, auditable, and scalable onboarding process. By evaluating applicants through the lens of identity, financial behavior, and compliance status, businesses can selectively recruit high-quality partners and build a sustainable IB ecosystem.

✅ **Recommended Workflow**:  
1. Log in → 2. Navigate to **Agent Applications** → 3. Search/filter applicants → 4. Click **“View”** to verify details → 5. Click **“Set as Agent”** → 6. Configure tier & plan → 7. Click **“Confirm”** to approve

> 📌 Every action is logged, ensuring full traceability and alignment with internal governance and regulatory standards.

---

**Version: v1.0**  
**Last Updated: February 2026**