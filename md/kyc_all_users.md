# **All Users**  

## **1. Module Overview**

The **All Users** module is the **global user management view** of MIM CRM, displaying complete information for all users—including those with verified, pending, rejected, or incomplete KYC statuses. It offers powerful filtering, searching, and one-click navigation to user profiles, allowing teams to conduct thorough reviews of KYC documents, trading behavior, or fund movements.

### ✅ Core Value:
- Enables full visibility of user data
- Supports fine-grained classification and bulk export
- Provides historical review records and change tracking
- Ensures comprehensive control over the user lifecycle

> 🔐 Access is restricted to **System Administrators**, **Compliance Officers**, and **Finance Managers** only. Regular clients and IBs cannot access this page.

---

## **2. Interface Layout**

### **Left Navigation Menu**
| Item | Function |
|------|----------|
| **Users** | Enter user management main menu |
| - KYC Review | Expand submenu |
|   - Pending Review Users (0) | View pending users |
|   - All Users | Current page |
|   - Pending Withdrawal Accounts (0) | View pending withdrawal requests |

---

### **All Users List View**
| Field | Description |
|-------|-------------|
| **User** | User name or nickname; clickable to open profile |
| **KYC Status** | Shows current verification status (e.g., "Verified", "Pending", "Rejected", "Incomplete") |
| **Nationality** | User’s nationality (e.g., 🇺🇸 United States) |
| **Residence Country** | User’s country of residence |
| **Phone/Email** | Contact details, copyable |
| **User Level** | User type (e.g., Verified Client, New Client) |
| **Source** | Registration channel (e.g., Web, App, IB Invite Code) |
| **Registration Time** | First registration timestamp |
| **Submission Time** | When user uploaded documents |
| **Last Review Time** | Most recent KYC review time |
| **Action** | Contains **View** button to access user profile for analysis |

> 💡 Example: Displays user `Thi Hà Vũ`, KYC status “Verified”, nationality Vietnam, registration time `09/02/2026`.

---

## **3. Core Features**

### **1. Multi-Dimensional Filtering & Smart Search**

#### **Available Filters**
| Condition | Description |
|---------|-------------|
| **KYC Status** | Dropdown options: Incomplete, Pending, Verified, Rejected |
| **Nationality** | Selectable country list, supports fuzzy matching |
| **Registration Time From ~ To** | Filter by registration period |
| **User ID/Name/Phone/Email Search** | Quickly locate specific users |

> ✅ Pro Tips:
> - Use “KYC Status = Incomplete” to quickly identify users who haven’t filled out full identity info.
> - Combine “Nationality = Vietnam” + “KYC Status = Verified” to analyze compliance rate in a specific country.

---

### **2. One-Click Profile Navigation**

#### **Workflow**
1. Find target user (e.g., `Thi Hà Vũ`) in the **All Users** list
2. Click **View**
3. Navigate directly to the user’s **Profile Page**
4. In the **Latest Information** tab, examine full identity, address proof, bank details
5. In the **Review History** tab, check past review results and notes

> ✅ Benefits:
> - Reduces page switching, improves efficiency
> - All actions are logged for audit trail

---

### **3. Data Export & Report Generation**

#### **Function Description**
- Supports exporting current filtered results to Excel
- Export includes: Name, KYC Status, Nationality, Residence, Contact Info, Registration Time, Submission Time, Review Time
- Does not include sensitive materials (e.g., ID photos)

> ⚠️ Notes:
> - Only accessible to roles with `user:export:excel` permission
> - Recommended to export regularly as compliance evidence

---

### **4. User Status Visualization & Trend Analysis**

#### **Key Features**
- **Color-coded status indicators**:
  - ✅ Green: "Verified"
  - ⚠️ Yellow: "Incomplete"
  - ❌ Red: "Rejected"
  - 🔍 Gray: "Pending"
- **Real-time count display**: Top bar shows number of users per status (e.g., "Verified: 120")
- **Supports pagination**: Up to 10 entries per page, with navigation controls

> ✅ Outcome: Visually reflects platform-wide compliance level and user health.

---

## **4. Typical Use Cases**

### **Use Case 1: Compliance Officer Conducting Quarterly Audit**

> 🎯 Goal: Ensure platform complies with AML and KYC regulations

- ✅ Implementation:
  1. Log in → Go to **Users → KYC Review → All Users**
  2. Set filters:
     - KYC Status: `Rejected`
     - Nationality: Singapore
  3. View list of rejected users (e.g., 3)
  4. Click **View** to open each profile
  5. Check if rejection reasons are valid (e.g., "False information", "Expired ID")
  6. If no issues → Archive as audit report appendix
  7. If misclassified → Re-review and correct status

> ✅ Outcome: Meet regulatory audit requirements and reduce legal risk.

---

### **Use Case 2: Finance Manager Analyzing High-Net-Worth Clients**

> 🎯 Goal: Identify potential high-value clients for targeted marketing

- ✅ Implementation:
  1. Go to **Users → KYC Review → All Users**
  2. Set filters:
     - KYC Status: `Verified`
     - Registration Time: `01/01/2026 ~ 31/01/2026`
     - Nationality: Hong Kong, Singapore, Malaysia
  3. View matching users (e.g., 87)
  4. Click **Download to Excel** to export list
  5. Analyze deposit amounts, trade frequency
  6. Identify 12 users with deposits > $10,000 → Flag as "High-Net-Worth"

> ✅ Outcome: Provide data support for precision marketing.

---

### **Use Case 3: System Administrator Investigating Suspicious Accounts**

> 🎯 Goal: Detect potential fraud or technical issues

- ✅ Implementation:
  1. Notice frequent profile changes → Go to **All Users**
  2. Search User ID `16684`
  3. Check **Review History**:
     - First review: Approved
     - Second: Rejected, note: "False information"
     - Third submission: Again rejected
  4. Determine malicious attempt → Click **View** → Open profile
  5. Discover email reused across multiple countries → Tag as "High Risk"
  6. Trigger anti-fraud process: Freeze account, notify legal team

> ✅ Outcome: Proactively block threats and protect platform security.

---

## **5. Best Practices**

| Scenario | Recommendation |
|---------|----------------|
| **Data Security** | Do not save search records on public computers to prevent leaks |
| **Permission Control** | Restrict access to authorized roles only |
| **Input Standardization** | Encourage users to always provide full contact details (with country code) |
| **Error Handling** | If search fails repeatedly, contact technical support |

---

## **6. Frequently Asked Questions (FAQ)**

### **Q1: Why isn't a user showing up in the "All Users" list?**  
- ❌ Possible causes: Account deleted, suspended, or data sync delay  
- ✅ Solution: Check user status, or contact support for confirmation

---

### **Q2: Can I approve multiple users at once?**  
- ❌ Not supported in current version; must review individually  
- ✅ Future version will include **batch approve/reject** functionality

---

### **Q3: How to view a user's historical review records?**  
- ✅ Go to user profile → Switch to **Review History** tab to see all past results and notes

---

### **Q4: What does KYC status "Incomplete" mean?**  
- ✅ Indicates the user has registered but hasn't submitted complete identity information (e.g., missing birth date, address), requiring supplementation before final approval.

---

## **7. Summary**

The **All Users** module is a critical component of MIM CRM for achieving **global user governance and compliance oversight**. It provides a clear, comprehensive view of all users and supports efficient filtering, analysis, and export functions, helping teams meet regulatory requirements while optimizing customer service and risk management.

✅ **Recommended Workflow**:  
1. Go to **Users → KYC Review → All Users** → 2. Filter target users → 3. Click **View** → 4. Analyze information and review history → 5. Perform necessary actions

> 📌 All operations are permission-controlled, ensuring data security and compliance.

---

**Version: v1.0**  
**Last Updated: February 2026**