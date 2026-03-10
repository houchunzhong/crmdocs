# **Pending Users**  

## **1. Module Overview**

The **Pending Users** module is the **compliance review center** of MIM CRM, used to display all users currently in "pending review" status. It supports rapid filtering by registration time, submission time, nationality, and more, and provides one-click navigation to user profiles for comprehensive evaluation of submitted documents.

### ✅ Core Value:
- Standardizes KYC review workflows
- Provides clear visibility into pending tasks to prevent omissions
- Supports batch operations and data export
- Ensures platform compliance with AML and KYC regulations

> 🔐 Access is restricted to **System Administrators**, **Compliance Officers**, and **Finance Managers** only. Regular clients and IBs cannot access this page.

---

## **2. Interface Layout**

### **Left Navigation Menu**
| Item | Function |
|------|----------|
| **Users** | Enter user management main menu |
| - KYC Review | Expand submenu |
|   - Pending Users (0) | Current page |
|   - All Users | View full user list |
|   - Pending Withdrawal Accounts (0) | View pending withdrawal requests |

---

### **Pending Users List View**
| Field | Description |
|-------|-------------|
| **User** | User name or nickname; clickable to open profile |
| **KYC Status** | Shows current status (e.g., "Pending", "Approved", "Rejected") |
| **Nationality** | User’s nationality (e.g., 🇸🇬 Singapore) |
| **Residence Country** | User’s country of residence |
| **Phone/Email** | Contact details, copyable |
| **User Level** | User type (e.g., New Client) |
| **Source** | Registration channel (e.g., Web, App, IB Invite Code) |
| **Registration Time** | First registration timestamp |
| **Submission Time** | When user uploaded documents |
| **Action** | Contains **View** button to access user profile for review |

> 💡 Example: Displays user `David Tan`, KYC status “Pending”, nationality Singapore, submission time `09/02/2026`.

---

## **3. Core Features**

### **1. Multi-Condition Filtering & Search**

#### **Available Filters**
| Condition | Description |
|---------|-------------|
| **Registration Time From ~ To** | Filter by registration period |
| **User ID/Name/Phone/Email Search** | Quickly locate specific users |

> ✅ Pro Tips:
> - Combine "Registration Time" + "Nationality" to identify recent registrations from a specific country.
> - Use "Submission Time" to flag users who delayed uploading documents.

---

### **2. One-Click Profile Navigation**

#### **Workflow**
1. Find target user (e.g., `David Tan`) in the **Pending Users** list
2. Click **View**
3. Navigate directly to the user’s **Profile Page**
4. In the **KYC Review** tab, examine uploaded ID, passport, address proof, etc.
5. Perform review action: **Approve** or **Reject**

> ✅ Benefits:
> - Reduces page switching, improves review efficiency
> - All actions are logged for audit trail

---

### **3. Data Export & Report Generation**

#### **Function Description**
- Supports exporting current filtered results to Excel
- Export includes: Name, KYC Status, Nationality, Residence, Contact Info, Registration Time, Submission Time
- Does not include sensitive materials (e.g., ID photos)

> ⚠️ Notes:
> - Only accessible to roles with `kyc:export:excel` permission
> - Recommended to export regularly as compliance evidence

---

### **4. Automatic Reminder Mechanism (Future Version)**

> ✅ Planned Feature:
> - Send internal alerts for users awaiting review over 72 hours
> - Support priority tagging (e.g., "High Risk", "Urgent")

---

## **4. Typical Use Cases**

### **Use Case 1: Compliance Officer Conducting Daily KYC Reviews**

> 🎯 Goal: Ensure every new user meets identity verification standards

- ✅ Implementation:
  1. Log in → Go to **Users → KYC Review → Pending Users**
  2. View all pending users (e.g., 5)
  3. Click **View** to open `David Tan`’s profile
  4. In **KYC Review** tab, check:
     - Clarity of ID front/back
     - Whether photo matches ID
     - Validity of address proof
  5. If complete → Click **Approve** → User becomes "Verified Client"
  6. If incomplete → Click **Reject** and enter reason → User receives notification to resubmit

> ✅ Outcome: Ensure user identities are genuine and reduce compliance risk.

---

### **Use Case 2: Finance Manager Monitoring Review Progress**

> 🎯 Goal: Track new user activation and forecast fund inflows

- ✅ Implementation:
  1. Go to **Users → KYC Review → Pending Users**
  2. Set filters:
     - Registration Time: `01/02/2026 ~ 28/02/2026`
     - Nationality: Singapore
  3. View current pending count (e.g., 12)
  4. Click **Download to Excel** to export list
  5. Analyze trend: Expect 10 Singapore users to complete KYC and deposit funds next week

> ✅ Outcome: Provide data support for financial planning.

---

### **Use Case 3: System Administrator Investigating Abnormal Submissions**

> 🎯 Goal: Detect potential fraud or technical issues

- ✅ Implementation:
  1. Notice repeated failed submissions → Go to **Pending Users**
  2. Search User ID `16680`
  3. Check submission history:
     - First upload: blurry ID
     - Second: non-matching photo
     - Third: blank file
  4. Identify as malicious attempt → Click **Reject** and tag as "High Risk"
  5. Trigger anti-fraud process: freeze account, notify legal team

> ✅ Outcome: Proactively block potential threats and protect platform security.

---

## **5. Best Practices**

| Scenario | Recommendation |
|---------|----------------|
| **Review Timeliness** | Aim to complete reviews within 24 hours to maintain user experience |
| **Document Completeness** | Strictly verify all required fields, especially ID and address proof |
| **Rejection Reason** | Always provide clear rejection reasons to help users correct errors |
| **Permission Control** | Restrict review actions to compliance team members only |
| **Audit Trail** | Ensure all review actions are logged for traceability |

---

## **6. Frequently Asked Questions (FAQ)**

### **Q1: Why isn’t a user showing up in the "Pending Users" list?**  
- ❌ Possible causes: Already approved, rejected, or no documents submitted  
- ✅ Solution: Check user status, or go to **All Users** list to locate

---

### **Q2: Can I approve multiple users at once?**  
- ❌ Not supported in current version; must review individually  
- ✅ Future version will include **batch approve/reject** functionality

---

### **Q3: Can users trade immediately after approval?**  
- ✅ Yes, upon approval, user status changes to "Verified Client" and can log in and open trading accounts.

---

### **Q4: How to view historical review records?**  
- ✅ Go to **Users → KYC Review → All Users**, filter by "Approved" or "Rejected" status.

---

## **7. Summary**

The **Pending Users** module is a critical component of MIM CRM for achieving **compliance automation and risk control**. It provides a clear task dashboard and supports efficient review workflows, helping teams meet regulatory requirements while maintaining user experience. Whether for daily reviews, progress tracking, or anomaly detection, this module enables streamlined operations.

✅ **Recommended Workflow**:  
1. Go to **Users → KYC Review → Pending Users** → 2. Filter target users → 3. Click **View** → 4. Review documents → 5. Select **Approve** or **Reject**

> 📌 All operations are permission-controlled, ensuring data security and compliance.

---

**Version: v1.0**  
**Last Updated: February 2026**