# **Notifications**  

## **1. Module Overview**

The **Notifications List** module serves as the **centralized messaging hub** of MIM CRM. It supports multilingual content (currently English-first), targeted delivery, real-time status control, and read-tracking, ensuring messages are delivered accurately and transparently. Key capabilities include:

- ✅ Creating and editing system notifications (title + body)  
- ✅ Supporting bilingual or multilingual content input  
- ✅ Configuring delivery scope (global / specific user groups)  
- ✅ Toggling visibility on/off without deletion  
- ✅ Monitoring read statistics (e.g., 4 out of 36 users have read)  
- ✅ Enabling bulk actions and historical audit trails  

> 🔐 Access is restricted to **System Administrators** or **Operations Managers** only. All notifications require explicit saving and are logged in the system audit trail.

---

## **2. Interface Layout**

### **Left Navigation Menu**
| Item | Function |
|------|----------|
| **Emails & Notifications** | Enter the email template and notification management center |
| - Email Templates | Manage transactional and marketing email designs |
| - Notifications List | View and manage all system notifications |

---

### **Top Tab Bar**
| Tab | Description |
|-----|-------------|
| **Overview** | Return to the main dashboard  
| **Settlement Plans** | Navigate to settlement configuration  
| **Commission Plans** | Navigate to commission settings  
| **Email Templates** | Navigate to email management  
| **Notifications List** | Current page |

---

### **Notifications List View**
| Field | Description |
|-------|-------------|
| **ID** | Unique auto-increment identifier  
| **Notification Title** | Front-end display title (e.g., “Happy New Year!”)  
| **Status** | Draft or Published  
| **Display Toggle** | On = visible to users; Off = hidden  
| **Delivery Scope** | Global or targeted user group  
| **Read / Total Recipients** | Read count vs. total audience (e.g., 4 / 36)  
| **Default Language** | Primary language (e.g., English)  
| **Language Count** | Number of localized versions available (e.g., 1)  
| **Last Edited** | Timestamp of most recent edit  
| **Sent At** | Actual delivery timestamp  
| **Actions** | Contains a **View** button to access details  

> 💡 Example: Notification ID 2 titled “Happy New Year!” has been read by 4 out of 36 recipients.

---

## **3. Core Feature Details**

### **1. Creating a New Notification**

#### **Procedure**
1. Navigate to **Emails & Notifications → Notifications List**  
2. Click the **New Notification** button at the top  
3. In the pop-up window, fill in the following required fields:
   - **Delivery Scope**: Choose “Global” or “Specific User Group”  
     - *Global*: Sent to all active users  
     - *User Group*: Future versions will support segmentation  
   - **Recipient Count**: System auto-calculates eligible users (e.g., 36)  
   - **Default Language**: Select primary display language (e.g., English)  
   - **Notification Title**: Enter a concise, engaging headline (e.g., “Welcome to TradeWise!”)  
   - **Notification Body**: Compose full message (plain text, up to 2,000 characters)  
4. Optional: Add additional language versions (multilingual support coming soon)  
5. Click **Save** to finalize

> ✅ Tip: Use action-oriented, benefit-driven titles to boost open rates.

---

### **2. Viewing Notification Details**

#### **Procedure**
1. Locate the target notification (e.g., ID=2) in the list  
2. Click the **View** button on the right  
3. The detail page displays two panels:
   - **Left Panel**:
     - Delivery scope  
     - Recipient count  
     - Default language  
     - Timeline (created, last edited, sent)  
     - Read status (e.g., 4 / 36 read)  
   - **Right Panel**:
     - Editable title and body  
     - Language tabs (currently English only)  

> ✅ Example: Viewing “Happy New Year!” shows its body as “Happy New Year!” and confirms it was sent to 36 users, with 4 reads.

---

### **3. Enabling/Disabling Notification Visibility**

#### **Functionality**
- The **Display Toggle** is a switch:
  - **On (🟢)**: Notification appears in the user’s frontend (e.g., dashboard banner or inbox)  
  - **Off (⚪)**: Notification is hidden but preserved in the system  

> ⚠️ Note:  
> - Disabling does **not** delete the notification  
> - Re-enabling restores visibility immediately

---

### **4. Deleting a Notification**

#### **Procedure**
1. Open the notification detail page  
2. Click the **Delete** button in the bottom-right corner  
3. Confirm permanent deletion in the prompt  
4. Click **Confirm** to complete

> ⚠️ Warning:  
> - Deletion is irreversible  
> - All associated data (including read logs) will be purged

---

### **5. Search and Filtering**

#### **Available Filters**
- **Sent Between**: Filter by date range  
- **Read Status**: Choose “Read”, “Unread”, or “All”  
- **Notification Status**: Filter by “Published” or “Draft”

> ✅ Pro Tip: Combine filters to quickly locate specific campaigns (e.g., unread global notifications sent in February 2026).

---

## **4. Typical Use Cases**

### **Use Case 1: Holiday Greetings & Brand Care**

> 🎯 Goal: Strengthen emotional connection during festive seasons

- ✅ Implementation:
  1. Create notification:
     - Title: `Happy New Year!`  
     - Body: `We wish you a happy and prosperous new year! Thank you for choosing TradeWise.`  
  2. Set scope to “Global”  
  3. Save and enable the toggle  
  4. Appears automatically in user dashboards

> ✅ Outcome: Enhances brand warmth and user loyalty.

---

### **Use Case 2: Service Change Announcement**

> 🎯 Goal: Inform users about scheduled maintenance

- ✅ Implementation:
  1. Create notification:
     - Title: `System Maintenance Notice`  
     - Body: `Scheduled maintenance will occur on Feb 10, 2026, from 00:00 to 04:00 UTC. Please plan accordingly.`  
  2. Set scope to “Global”  
  3. Publish 24 hours in advance  
  4. Disable the toggle after maintenance concludes

> ✅ Outcome: Reduces support tickets and demonstrates operational professionalism.

---

### **Use Case 3: Promoting Time-Limited Offers**

> 🎯 Goal: Drive deposits via a limited-time bonus

- ✅ Implementation:
  1. Create notification:
     - Title: `Deposit $1000 & Get 5% Bonus!`  
     - Body: `Limited-time offer: Deposit $1000 or more and receive a 5% bonus credit. Offer valid until March 31, 2026.`  
  2. Set scope to “Global”  
  3. Enable toggle and monitor read-through rate  
  4. Disable after campaign ends

> ✅ Outcome: Boosts short-term funding inflows and trading activity.

---

## **5. Best Practices**

| Scenario | Recommendation |
|--------|----------------|
| **Title Design** | Keep under 20 characters; highlight value (e.g., “Bonus Alert!”) |
| **Tone & Clarity** | Friendly yet professional; avoid jargon |
| **Timing** | Avoid late-night sends; prefer business hours or holiday eves |
| **Localization** | When multilingual support launches, ensure accurate, culturally appropriate translations |
| **Performance Tracking** | If read rate <30%, revise copy or consider re-sending via email |

---

## **6. Frequently Asked Questions (FAQ)**

### **Q1: Can I send notifications to specific users only?**  
- ❌ Not in the current version.  
- ✅ Workaround: Manually adjust user permissions or wait for upcoming segmentation features.

---

### **Q2: Is scheduled sending supported?**  
- ❌ No automatic scheduling.  
- ✅ Solution: Draft the notification in advance and manually toggle it on at the desired time.

---

#
