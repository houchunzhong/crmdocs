# **Email & Notification Module User Guide**  
**My Investment Markets (MIM) CRM System**

This guide provides a comprehensive overview of the **Email & Notification Module** in the MIM CRM system, detailing its features, configuration methods, and operational workflows. Designed for marketing, customer support, and operations teams, it enables efficient, multilingual communication with users, agents, and internal staff.

---

## **1. Module Overview**

The **Email & Notification Module** is a core communication tool within MIM CRM, supporting two primary functions:

- ✅ **Email List**: Create, edit, and send bulk emails with multilingual support and targeted audience segmentation  
- ✅ **Notification List**: Configure in-app notifications (e.g., login banners, pop-ups) for announcements, policy updates, or promotional campaigns  

> 🔐 Only authorized personnel (e.g., administrators, marketing managers) can create or modify content. All actions are logged for audit and compliance purposes.

---

## **2. Interface Layout Explanation**

### **Left Sidebar Navigation**
| Item | Function |
|------|----------|
| **Email List** | View and manage all email templates and delivery records |
| **Notification List** | View and configure system-wide or user-specific notifications |

---

### **Top Filtering Toolbar**
Multi-dimensional filters help quickly locate specific messages:

| Field | Description |
|-------|-------------|
| **Send Time From ～ To** | Filter by date range |
| **Send Status** | Email status: `Draft` / `Sent Successfully` / `Failed` |
| **Display Status** | Notification status: `Published` / `Draft` |
| **Notification Status** | Toggle: `Enabled` / `Disabled` |

---

## **3. Core Function Details**

### **1. Email List**

#### **Function Description**  
Used to create and send bulk marketing or service emails, supporting multilingual content, precise recipient targeting, and delivery tracking.

#### **Field Descriptions**
| Field | Description |
|-------|-------------|
| **ID** | Unique email ID (e.g., `59`) |
| **Email Title** | Subject line (e.g., “Year-End Bonus Campaign Live!”) |
| **Send Status** | Current status:<br>🟢 `Sent Successfully`<br>🟡 `Draft`<br>🔴 `Failed` |
| **Recipient Scope** | Target audience:<br>`Specific Recipients` (custom list)<br>`Global` (all registered users) |
| **Delivered / Total Recipients** | Successful deliveries vs. total recipients (e.g., `1/2`) |
| **Default Language** | Default display language (e.g., English, Chinese, Indonesian) |
| **Number of Languages** | Supported language versions (e.g., 3) |
| **Last Edited Time** | Timestamp of most recent edit |
| **Send Time** | Actual send time (`-` if not sent) |
| **Action** | Button: **View** (open detail page) |

#### **Operation Workflow**
1. Click the **“New Email”** button at the top.
2. Fill in email details:
   - Subject and body (rich text supported)
   - Attach files (e.g., PDFs, images)
3. Configure multilingual versions (optional):
   - Add translations (e.g., English, Japanese, Vietnamese)
   - System automatically matches based on user’s language preference
4. Set recipient scope:
   - Choose `Global` or `Specific Recipients`
   - For specific recipients, manually enter user IDs or upload a CSV file
5. Preview the email, save as draft, or click **“Send”**.
6. After sending, the system logs delivery status and displays success rates in the list.

> 💡 Recommendation: Use **test sends** for critical emails to verify links, formatting, and translation accuracy.

---

### **2. Notification List**

#### **Function Description**  
Used to configure in-app notifications that appear as banners or pop-ups when users log in—ideal for compliance alerts, holiday greetings, or platform maintenance notices.

#### **Field Descriptions**
| Field | Description |
|-------|-------------|
| **ID** | Unique notification ID (e.g., `28`) |
| **Notification Title** | Concise headline (e.g., “Account Security Upgrade”) |
| **Content Status** | Draft or final state:<br>🟢 `Published`<br>🟡 `Draft` |
| **Notification Toggle** | Visibility control:<br>✅ Enabled → visible to users<br>❌ Disabled → hidden |
| **Recipient Scope** | Audience:<br>`Specific Users`<br>`Global` |
| **Read / Total Recipients** | Number of users who have seen it vs. total (e.g., `1/1`) |
| **Default Language** | Default display language |
| **Number of Languages** | Supported language versions |
| **Last Edited Time** | Most recent edit timestamp |
| **Publish Time** | When the notification was activated |
| **Action** | Button: **View** (open detail page) |

#### **Operation Workflow**
1. Click **“New Notification”**.
2. Enter a short title and message (recommended ≤100 characters).
3. Add multilingual versions if needed.
4. Select recipient scope (`Global` or `Specific Users`).
5. Toggle **“Enable Notification”** to activate.
6. Save—the notification will appear for eligible users on their next login.
7. You can return anytime to disable the toggle and hide the message.

> 📌 Note: Keep notifications concise, urgent, and relevant to avoid user fatigue.

---

## **4. Multilingual Support**

- Supports multiple languages (e.g., English, Chinese, Japanese, Indonesian, Vietnamese, Thai).
- Each email or notification can include multiple language versions.
- The system automatically displays the version matching the user’s registered or preferred language.

---

## **5. Audit & Tracking**

- Full history is retained for every email and notification.
- Includes:
  - Creator and editor timestamps
  - Send/publish time
  - Recipient list
  - Delivery/read status
- Exportable to Excel for performance analysis or regulatory audits.

---

## **6. Best Practices**

| Item | Recommendation |
|------|----------------|
| **Access Control** | Restrict “Create Email/Notification” permissions to marketing or ops teams |
| **Content Review** | Require legal/compliance approval for critical announcements |
| **Timing Strategy** | Schedule promotional emails during evenings or weekends for higher open rates |
| **A/B Testing** | Test different subject lines or copy with small user segments |
| **Regular Cleanup** | Archive or delete expired notifications (e.g., post-holiday campaigns) |

---

## **7. Frequently Asked Questions (FAQ)**

### **Q1: How do I send an exclusive email to VIP clients?**  
- Select “Specific Recipients,” then upload a CSV file containing VIP user IDs.

### **Q2: Why did my email fail to send?**  
Common causes:
- Invalid or malformed email addresses  
- SMTP server issues  
- Content flagged as spam (e.g., excessive links, sensitive keywords)  
- Check the error log in “Send Status” for details.

### **Q3: Can a notification be shown only once per user?**  
- ✅ Yes. By default, notifications appear only once—on the user’s first login after publication.

### **Q4: Can I recall a sent email?**  
- ❌ No. However, you can disable related notifications immediately or send a follow-up correction email.

---

## **8. Summary**

The **Email & Notification Module** in MIM CRM delivers a scalable, compliant, and multilingual communication channel for engaging users across the customer journey. Whether for routine service updates, marketing promotions, or urgent compliance alerts, this module ensures timely, personalized, and trackable outreach.

✅ **Recommended Workflow**:  
1. Create Content → 2. Translate → 3. Preview & Test → 4. Send/Publish → 5. Monitor Performance → 6. Archive

> 📌 All communications must comply with data privacy regulations (e.g., GDPR, CCPA) and user consent policies.

---

**Version: v1.0**  
**Last Updated: January 2026**