
# Basic Settings

## 1. Domain Settings  
Configure system-related domains to ensure proper access and integration between the client, mobile, and server platforms.

- **Corporate Website Domain**  
  The domain of the company website, usually displayed in the top navigation or logo area. Supports both http and https and must end with .com.  
  Example: https://www.tradewisesoftware.com

- **CRM Client Domain**  
  URL used to access the web-based CRM system. Must use https and end with .com.  
  Example: https://crmclient.tradewisesoftware.com

- **CRM Mobile Domain**  
  URL for accessing the mobile version of the CRM. Must use https and end with .com.  
  Example: https://crmmobile.tradewisesoftware.com

- **Server Domain**  
  Used for integration with third-party services (e.g., E-KYC, SMS, email systems). Must use https and remain consistent with the domain used during server deployment.  
  Example: https://api.tradewisesoftware.com

---

## 2. User Agreement Settings  
The user agreement is displayed on the registration page. Users must review and accept it before completing registration or login.

- **Display Name**  
  The name shown on the registration page.  
  Example: User Agreement, Terms and Conditions

- **Agreement URL**  
  The link to the agreement content. Must begin with https. File uploads are supported (PDF, TXT), and the system will automatically generate a URL after upload.  
  Example: https://www.tradewisesoftware.com/terms.pdf

---

## 3. User Registration Settings  

### 3.1 Registration Modes  
Two registration modes are available:

- **Two-Step Registration**  
  Users complete registration by verifying their phone or email and can immediately log in. Additional information may be completed later within the system.  
  Best for: Quick registration and onboarding.

- **One-Step Registration**  
  Users must complete all registration information on the registration page before entering the system.  
  Best for: Platforms requiring complete data collection upfront.

---

### 3.2 Referral Code Settings  
Referral codes are typically provided by IBs (Introducing Brokers). If users access the registration page through an IB referral link, the system auto-fills the referral code.

- **Required**  
  Users must enter a referral code to register. All users will automatically be assigned to the IB who provided the referral code.

- **Optional (Recommended)**  
  Users may choose whether to enter a referral code. Supports both organic traffic and IB-referred customers. If no code is entered, the default referral code will be applied.

- **Disabled**  
  Referral codes are not used. All users will be assigned under the IB specified in the default referral code

---

### 3.3 Default Referral Code  
When users do not provide a referral code (in Optional or Disabled mode), the system automatically assigns them to the IB specified by the default referral code.

---

## 4. User Registration Form  
This section configures the information that needs to be filled in by the user during registration, as well as the required fields to complete the registration process.

- **Country/Region of Residence**  
  Configures whether users are required to enter their country or region.  
  **Example**:  
  If set to "Disabled" or "Optional," the user will not be required to fill in this field. If left blank, the system will automatically set the user's country of residence based on the country code of their phone number.

- **First Name / Last Name / Middle Name**  
  These fields are used to enter the user's full name. The administrator can enable or disable these fields.

---

## 5. Account Locking  
By configuring account lock and unlock policies, administrators can effectively prevent brute-force attacks and unauthorized login attempts.

- **Account Lock - Number of Failed Password Attempts**  
  Configures the number of consecutive incorrect password attempts before the system locks the account.

- **Account Lock - Automatic Unlock Time**  
  Configures the automatic unlock time for the account after it has been locked, in seconds.  
  **Example**:  
  - Number of Failed Password Attempts: 5 attempts  
  - Lock Time: 600 seconds (10 minutes)  
  In this configuration, if a user enters the wrong password 5 times consecutively, their account will be locked, and the system will automatically unlock the account after 10 minutes.

---

## 6. Withdrawal Account Settings  
In the **Withdrawal Account Settings**, administrators can configure whether users are required to upload images when registering their bank accounts and the number of images to be uploaded. This helps ensure the accuracy and security of the withdrawal account information.

- **Is image upload required?**  
  Configures whether users are required to upload images of their bank card when registering their withdrawal account. If enabled, users must upload at least one image to verify the account.

- **Minimum Number of Uploaded Images**  
  Configures the minimum number of images required to be uploaded when registering a withdrawal account.

- **Maximum Number of Uploaded Images**  
  Configures the maximum number of images that can be uploaded when registering a withdrawal account.

---

## 7. Withdrawal Settings  
In the **Withdrawal Settings**, administrators can configure the withdrawal limits and withdrawal fee rate for users.

- **Maximum Single Withdrawal**  
  Configures the maximum amount that can be withdrawn in a single transaction, in **USD**. For example, if set to 10,000 USD, users will not be able to withdraw more than 10,000 USD in a single transaction.

- **Minimum Single Withdrawal**  
  Configures the minimum amount that can be withdrawn in a single transaction, in **USD**. For example, if set to 0.1 USD, users must withdraw at least 0.1 USD in each transaction.

- **Withdrawal Fee Rate**  
  Configures the withdrawal fee rate, in **percentage**. For example, if set to 1%, a 1% fee will be deducted from each withdrawal.

---

## 8. Transfer Settings  
In the **Transfer Settings**, administrators can configure the limits for internal transfers.

- **Maximum Single Transfer**  
  Configures the maximum amount that can be transferred in a single internal transfer, in **USD**. For example, if set to 6,000 USD, users will not be able to transfer more than 6,000 USD in a single transfer.

- **Minimum Single Transfer**  
  Configures the minimum amount that can be transferred in a single internal transfer, in **USD**. For example, if set to 100 USD, users must transfer at least 100 USD in each transfer.

---
