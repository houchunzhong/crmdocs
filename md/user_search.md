# **User Search**  

## **1. Module Overview**

The **User Search** module serves as the **fast retrieval center** of MIM CRM, used to directly locate user account information based on contact details (phone number or email). It streamlines the process of finding users in large datasets, providing **instant matching results** and **direct navigation to profile pages**.

### ✅ Core Value:
- Rapid response to customer inquiries (e.g., “I forgot my ID, please help me find it.”)
- Supports multi-field input validation (phone/email)
- Provides auto-completion and smart suggestions to reduce input errors
- One-click access to full user profile

> 🔐 Access is restricted to **System Administrators**, **Finance Managers**, and **IB Supervisors** only. Regular clients cannot use this feature.

---

## **2. Interface Layout**

### **Left Navigation Menu**
| Item | Function |
|------|----------|
| **Users** | Enter user management main menu |
| - User Search | Current page |
| - User List | View all users |
| - User Relationship Tree | View hierarchical structure |

---

### **User Search Form**
| Field | Description |
|-------|-------------|
| **Phone** | Input phone number with country code selector (e.g., +65) |
| **Email** | Input email address |
| **Matching Results Area** | Displays matched user info (avatar, name, ID, contact details) |
| **Search Button** | Click to execute search and navigate to user profile |

> 💡 Example: Enter `+65 89901122`, system immediately shows match `David Tan` (ID: 16680), click **View** to open profile.

---

## **3. Core Features**

### **1. Multi-Method Search Support**

#### **Supported Search Methods**
| Method | Description |
|--------|-------------|
| **Phone Number Search** | Supports full number with country code (e.g., +65 89901122) |
| **Email Search** | Supports standard email format (e.g., david.tan@email.com) |
| **Combined Search** | Input both phone and email; system prioritizes phone matching |

> ✅ Pro Tips:
> - If user remembers only part of the number, try fuzzy matching (future version will support).
> - Email verification status is shown with green label (e.g., "Verified"), helping assess validity.

---

### **2. Real-Time Matching & Smart Suggestions**

#### **Function Description**
- When entering phone or email, system performs real-time database lookup
- On success, displays user card with:
  - Avatar
  - Name
  - User ID
  - Phone and email
- If multiple matches exist, lists all possible options

> 🎯 Example:
> - Enter `david.tan@email.com` → System returns single match `David Tan`
> - Enter `tan` → Returns multiple users with surname Tan (e.g., David Tan, Alice Tan)

---

### **3. Error Handling & Input Validation**

#### **Common Prompts**
| Condition | Message |
|---------|---------|
| Empty phone | “Input cannot be empty” (red border) |
| Invalid email | “Please enter a valid email address” |
| No match found | “No matching user found” (gray message) |

> ✅ Security Measures:
> - All inputs are validated on frontend to prevent injection attacks
> - Search results do not expose sensitive data (e.g., trading accounts, fund balances)

---

### **4. One-Click Profile Navigation**

#### **Workflow**
1. In **User Search**, enter phone or email  
2. System displays matched result  
3. Click **View**  
4. Directly navigate to the user’s **Profile Page** without additional filtering  

> ✅ Benefits:
> - Saves time: From search to profile in two steps
> - Reduces errors: Avoids accidentally selecting wrong user from list

---

## **4. Typical Use Cases**

### **Use Case 1: Customer Service Handling Inquiries**

> 🎯 Goal: Help customers recover account information

- ✅ Implementation:
  1. Customer calls: “I’m David Tan, but I forgot my user ID. Can you help?”
  2. CS agent goes to **Users → User Search**
  3. Enters phone number `+65 89901122`
  4. System shows match `David Tan` (ID: 16680)
  5. Clicks **View** → Opens profile → Checks registration IP and last login
  6. Confirms identity → Tells customer their ID is `16680` and guides login

> ✅ Outcome: Improve customer satisfaction and shorten service cycle.

---

### **Use Case 2: Finance Team Verifying Withdrawal Requests**

> 🎯 Goal: Confirm if the user submitting withdrawal exists

- ✅ Implementation:
  1. Receives withdrawal request with email `david.tan@email.com`
  2. Goes to **Users → User Search**
  3. Enters email `david.tan@email.com`
  4. System returns user `David Tan` (ID: 16680)
  5. Clicks **View** → Profile → Checks wallet balance
  6. Confirms sufficient funds → Proceeds with review

> ✅ Outcome: Ensure accurate withdrawal processing and reduce risk.

---

### **Use Case 3: Compliance Team Checking KYC Status**

> 🎯 Goal: Verify if a user has completed identity verification

- ✅ Implementation:
  1. Receives regulatory notice to check KYC status of `david.tan@email.com`
  2. Goes to **Users → User Search**
  3. Enters email `david.tan@email.com`
  4. System returns user `David Tan`
  5. Clicks **View** → Profile → Checks “Two-Factor Authentication” status
  6. Finds status as “Not Set”, notifies user to complete verification

> ✅ Outcome: Promptly respond to regulatory requirements and maintain compliance.

---

## **5. Best Practices**

| Scenario | Recommendation |
|---------|----------------|
| **Data Security** | Do not save search records on public computers to prevent leaks |
| **Permission Control** | Only allow authorized roles to use this feature |
| **Input Standardization** | Encourage users to always provide full contact details (with country code) |
| **Error Handling** | If search fails repeatedly, contact technical support |

---

## **6. Frequently Asked Questions (FAQ)**

### **Q1: Why no result when entering phone number?**  
- ❌ Possible causes: Wrong format, unregistered, or deactivated account  
- ✅ Solution: Check if country code is included (e.g., +65), or try email search

---

### **Q2: Can I input both phone and email?**  
- ✅ Yes. System prioritizes phone matching; if invalid, tries email.

---

### **Q3: What does “Verified” mean in the result?**  
- ✅ Indicates the contact method has been confirmed via SMS or email, enabling secure login and notifications.

---

### **Q4: Can I edit user information?**  
- ✅ Yes. In the profile page, click **Edit** to modify contact info, nickname, etc. (requires permission).

---

## **7. Summary**

The **User Search** module is a critical component of MIM CRM for achieving **efficient customer service and precise user targeting**. With its clean interface and powerful matching algorithm, it greatly enhances user lookup efficiency and reduces manual effort. Whether for customer support, financial review, or compliance checks, this module enables rapid initial identification.

✅ **Recommended Workflow**:  
1. Go to **Users → User Search** → 2. Enter phone or email → 3. Click **View** → 4. Navigate to profile for further actions

> 📌 All operations are permission-controlled, ensuring data security and compliance.

---

**Version: v1.0**  
**Last Updated: February 2026**