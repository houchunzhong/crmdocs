# **Administrator Module**  

## **1. Module Overview**

The **Administrator** module functions as the **permission hub** of MIM CRM, comprising two key features:

- ✅ **Administrator List**: View, add, and edit system administrator accounts  
- ✅ **System Logs**: Track all administrative actions with support for filtering by time, IP, user, and more  

> 🔐 Access is restricted to **Master-level Administrators** only. All changes are recorded in an immutable audit log for full traceability.

---

## **2. Interface Layout**

### **Left Navigation Menu**
| Item | Function |
|------|----------|
| **Administrator List** | View all admin account details |
| **System Logs** | Query historical admin activities |

---

### **Top Tab Bar**
| Tab | Description |
|-----|-------------|
| **Overview** | Return to parent page |
| **Administrator List** | Display current list of administrators |
| **System Logs** | View system-level operation records |

---

## **3. Core Function Details**

### **1. Administrator List**

#### **Function Description**  
Displays basic information for all administrator accounts in the system, supporting creation, editing, and status control. Each administrator has a unique ID and assigned role that determines their functional access scope.

#### **Field Definitions**
| Field | Description |
|-------|-------------|
| **ID** | Unique auto-incremented administrator number |
| **Name** | Display name (e.g., “Default Admin”) |
| **Phone** | Contact number (used for login verification) |
| **Email** | Login username (must be unique) |
| **Role** | Assigned role (e.g., Master, Manager, Operator) |
| **Created At** | Account creation date (DD/MM/YYYY format) |
| **Last Login** | Timestamp of most recent successful login |
| **Last Login IP** | Source IP address of last login (for security analysis) |
| **Status** | `Enabled` / `Disabled` (toggle switch) |
| **Actions** | **Edit** (modify account details) |

#### **Workflow**
1. Click **“Add Administrator”**.
2. Fill in new admin details:
   - Name
   - Phone number (requires verification)
   - Email (must be unique)
   - Role (select from dropdown)
3. Set an initial password or send a reset link.
4. Click **“Save”** to complete creation.
5. The new administrator appears in the list and will be logged in **System Logs** upon first action.

> 💡 Example: To create a finance specialist, assign the “Operator” role with access limited to funding and payment modules.

---

### **2. System Logs**

#### **Function Description**  
Records all critical actions performed by administrators—including logins, data modifications, and configuration changes. Supports multi-dimensional filtering for rapid anomaly detection.

#### **Field Definitions**
| Field | Description |
|-------|-------------|
| **Name** | Administrator’s display name |
| **Email** | Login email address |
| **Phone** | Associated phone number |
| **Action Type** | Operation category (e.g., LOGIN, UPDATE, DELETE) |
| **Object Type** | Target entity (e.g., ADMINISTRATOR, CURRENCY, PAYMENT_CHANNEL) |
| **Target Object** | Specific item affected (e.g., “Administrator”, “USDT”) |
| **Details** | Brief description (e.g., “Login”, “Updated currency rate”) |
| **Timestamp** | Time of action (DD/MM/YYYY format) |
| **IP Address** | Source IP (enables geolocation tracking) |

#### **Search & Filter Options**
- **Date Range**: Filter by start/end date  
- **Name/Phone Search**: Find specific administrators  
- **IP Address Search**: Investigate suspicious logins  

#### **Workflow**
1. Navigate to **“System Logs”**.
2. Set filters using the top toolbar.
3. Click **“Search”** to retrieve matching records.
4. Review action details to verify legitimacy.

> 📌 Note: All logs are retained for at least **180 days**, complying with financial industry regulations.

---

## **4. Role-Based Access Control (RBAC)**

| Role | Permissions |
|------|-------------|
| **Master** | Full system access; can manage all modules, create admins, and modify global settings |
| **Manager** | Can manage users, funding, trading accounts, IBs, and core business functions |
| **Operator** | Limited permissions; typically used for finance or support staff with read-only or task-specific access |

> ⚠️ Recommendation: Follow the **principle of least privilege**—avoid over-assigning permissions.

---

## **5. Best Practices**

| Scenario | Recommendation |
|--------|----------------|
| **Initial Deployment** | Create one Master account as the primary controller; use sub-accounts for all other personnel |
| **Employee Offboarding** | Immediately disable the account to prevent unauthorized access |
| **Sensitive Operations** | Require dual approval for critical changes to prevent errors |
| **Regular Audits** | Review system logs monthly to detect anomalous behavior |

---

## **6. Frequently Asked Questions (FAQ)**

### **Q1: How do I add a new administrator?**  
- Go to **Administrator List** > **Add Administrator**, fill in the details, and assign a role.

### **Q2: Why can’t I see a certain action in the logs?**  
- Verify your filter criteria or check if you have sufficient permissions to view that module’s logs.

### **Q3: Can system logs be exported?**  
- ✅ Yes. Click **“Export CSV”** in the top-right corner to download an encrypted ZIP file (requires transaction password to unzip).

### **Q4: Can administrator accounts be deleted?**  
- ❌ No. Accounts can only be **disabled**. Deletion would break audit integrity and is not permitted.

---

## **7. Summary**

The **Administrator** module in MIM CRM delivers robust permission control and comprehensive operational auditing. Through clear role segmentation and immutable logging, it ensures both backend security and regulatory compliance.

✅ **Recommended Workflow**:  
1. Create Master account → 2. Add sub-administrators → 3. Assign roles → 4. Conduct regular log reviews → 5. Disable accounts when necessary

> 📌 All actions must align with internal security policies to maintain system stability and data integrity.

---

**Version: v1.0**  
**Last Updated: January 2026**