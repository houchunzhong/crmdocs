# **User List**  

## **1. Module Overview**

The **User List** module serves as the **customer asset overview center** of MIM CRM, displaying summarized information of all registered users. It supports rapid filtering and searching by nationality, level, registration time, contact details, and more. Its core value lies in:

- ✅ Enabling full lifecycle management (registration → KYC → trading → withdrawal)  
- ✅ Supporting multi-condition combination queries to precisely target audiences  
- ✅ Providing Excel export functionality for offline analysis and report generation  
- ✅ Integrating permission controls to ensure secure access to sensitive data  

> 🔐 Access is restricted to **System Administrators**, **Finance Managers**, and **IB Supervisors** only. Regular clients cannot view others' information.

---

## **2. Interface Layout**

### **Left Navigation Menu**
| Item | Function |
|------|----------|
| **Users** | Enter user management main menu |
| - User Search | Search users by criteria |
| - User List | View all users (default page) |
| - User Relationship Tree | View hierarchical structure (for IBs) |
| - CFD User List | View users exclusive to CFD products |

---

### **Top Tab Bar**
| Tab | Description |
|-----|-------------|
| **Overview** | Return to homepage |
| **User List** | Current page |
| **User - David Tan** | View detailed profile of a specific user |

---

### **User List View**
| Field | Description |
|-------|-------------|
| **User ID** | Unique identifier (e.g., `16680`) – clickable to view details |
| **Name** | Display name or real name, with status icons (e.g., verified, incomplete KYC) |
| **Nationality** | Country name + flag icon (e.g., 🇸🇬 Singapore) |
| **Residence** | User's city or country of residence |
| **Phone** | Phone number + verification status (green ✅ means verified) |
| **Email** | Email address + verification status |
| **User Level** | Customer type (e.g., Client, Verified Client, New Client) |
| **Registration Time** | First registration time |
| **Last CRM Login** | Most recent login to CRM system |
| **Action** | Contains **View** button to access detailed profile |

> 💡 Example: In the list, find user `David Tan` (ID: 16680), nationality Singapore, email verified, registered on `09/02/2026`.

---

## **3. Core Features**

### **1. Multi-Condition Filtering & Search**

#### **Available Filters**
| Condition | Description |
|---------|-------------|
| **Last CRM Login From ~ To** | Filter by last login time range |
| **Registration Time From ~ To** | Filter by registration time range |
| **Nationality** | Dropdown selection with flags + codes (e.g., +65 Singapore) |
| **User Level** | Select customer level (e.g., Verified Client, New Client) |
| **ID/Name/Phone/Email Search** | Quickly search by any field |

> ✅ Pro Tips:
> - Combine "Nationality" + "User Level" to quickly identify high-value clients.
> - Use "Registration Time" to filter new users for welcome email campaigns.

---

### **2. Bulk Export to Excel**

#### **Procedure**
1. Select target users in the list (single or multiple)  
2. Click **Download to Excel**  
3. Pop-up appears: “Are you sure you want to export user data to Excel? Exported data may contain sensitive information.”  
4. Click **Confirm** to generate and download `.xlsx` file  

> ⚠️ Notes:
> - Export includes: User ID, Name, Nationality, Residence, Phone, Email, Level, Registration Time, Last Login Time  
> - Does not include trading accounts, fund flows, KYC documents, etc.  
> - Only accessible to roles with `user:export:excel` permission

---

### **3. View User Details**

#### **Workflow**
1. Click on a user in the list (e.g., `David Tan`)  
2. Navigate to **User Profile Page**, divided into sections:
   - **User Profile**:
     - First, Middle, Last Name, Full Name
     - Nationality, Residence, Birthday
     - Email, Phone (verified status)
     - Two-Factor Authentication Status
   - **User Account Details**:
     - Status (Enabled/Disabled), User Type (Client/IB)
     - Parent User ID, Number of Subordinates
     - Invite Code, Login Link
     - Registration Time, First Verification Time, Registration IP, Last Login IP
   - **Other Tabs**:
     - User Assets, Trading Accounts, Withdrawal Accounts, Logs (audit trail)

> ✅ Example: Viewing `David Tan`’s profile reveals registration IP `171.223.184.189`, useful for fraud analysis.

---

## **4. Typical Use Cases**

### **Use Case 1: Customer Service Handling Inquiries**

> 🎯 Goal: Quickly locate users and provide personalized support

- ✅ Implementation:
  1. CS receives call: “I’m David Tan, I’d like to check my account status.”
  2. In **User List**, search `David Tan` or `16680`
  3. Click **View** to open profile
  4. Check assets, trading accounts, last login time
  5. If further help needed, create internal ticket or contact tech support

> ✅ Outcome: Improve response speed and reduce redundant communication.

---

### **Use Case 2: IB Supervisor Analyzing Team Performance**

> 🎯 Goal: Count subordinate clients and assess activity

- ✅ Implementation:
  1. Log in → Go to **Users → User List**
  2. Set filters:
     - Parent User ID = Own ID (e.g., `16680`)
     - User Level = "Client"
     - Registration Time: `01/02/2026 ~ 28/02/2026`
  3. View total count (e.g., 37)
  4. Click **Download to Excel**
  5. In Excel, calculate:
     - Total number
     - Verified client count
     - 30-day login rate

> ✅ Outcome: Support performance evaluation.

---

### **Use Case 3: Compliance Team Identifying High-Risk Users**

> 🎯 Goal: Identify users who haven’t completed KYC or logged in recently

- ✅ Implementation:
  1. Go to **User List**
  2. Set filters:
     - User Level = "New Client" (unverified)
     - Last CRM Login < `01/02/2026`
  3. View results (e.g., 12 users)
  4. Select all → **Download to Excel**
  5. Send reminder email: “Please complete KYC verification; otherwise, your account will be restricted.”

> ✅ Outcome: Reduce compliance risk and improve KYC completion rate.

---

### **Use Case 4: Marketing Team Launching Targeted Campaigns**

> 🎯 Goal: Push coupons to users from specific countries

- ✅ Implementation:
  1. Go to **User List**
  2. Set filters:
     - Nationality = "Singapore"
     - Registration Time > `01/02/2026`
     - User Level = "Verified Client"
  3. View results (e.g., 87 users)
  4. **Download to Excel**
  5. Import into email system, send “Singapore Exclusive Offer” campaign

> ✅ Outcome: Increase conversion and user retention.

---

## **5. Best Practices**

| Scenario | Recommendation |
|---------|----------------|
| **Data Security** | Always remind users about sensitive data before exporting |
| **Permission Control** | Only allow authorized roles to export data to prevent misuse |
| **Regular Cleanup** | Flag users inactive for over 1 year as “dormant” for future handling |
| **Automated Alerts** | Future versions will include automatic reminders when users don’t complete KYC |
| **Data Masking** | For external sharing, pre-process fields like email/phone to mask sensitive info |

---

## **6. Frequently Asked Questions (FAQ)**

### **Q1: Why do some users show "Unknown"?**  
- ❌ Possible cause: Incomplete profile or uncompleted KYC  
- ✅ Solution: Click **View** → Edit profile or guide them to complete verification

---

### **Q2: Can I export trading account details?**  
- ❌ Not available by default.  
- ✅ For trading account info, go to **Trading Accounts** module separately.

---

### **Q3: How to find a user’s parent IB?**  
- ✅ Method: In the user profile’s “Account Details”, check the “Parent User ID” field.

---

### **Q4: What fields are included in the exported Excel file?**  
- ✅ Includes: User ID, Name, Nationality, Residence, Phone, Email, Level, Registration Time, Last Login Time  
- ❌ Excludes: Trading accounts, fund balances, KYC documents, withdrawal records

---

## **7. Summary**

The **User List** module is a critical component of MIM CRM for achieving **precise customer operations and efficient management**. It offers powerful filtering and export capabilities while supporting multi-role collaboration. Through scientific data management and efficient querying, organizations can build a robust customer management system, delivering superior service experiences.

✅ **Recommended Workflow**:  
1. Go to **Users → User List** → 2. Use filters to locate users → 3. Click **View** or **Download to Excel** → 4. Analyze or export data

> 📌 All actions are permission-controlled, ensuring data security and compliance.

---

**Version: v1.0**  
**Last Updated: February 2026**