# Basic Settings

## 1. Domain Settings
Configure system-related domains to ensure proper access and integration between the client, mobile, and server platforms.

### • Corporate Website Domain
The domain of the company website, typically displayed in the top navigation or logo area. Supports both http and https and must end with `.com`.  
**Example:** https://www.tradewisesoftware.com

### • CRM Client Domain
URL used to access the web-based CRM system. Must use `https` and end with `.com`.  
**Example:** https://crmclient.tradewisesoftware.com

### • CRM Mobile Domain
URL for accessing the mobile version of the CRM. Must use `https` and end with `.com`.  
**Example:** https://crmmobile.tradewisesoftware.com

### • CRM Server Domain
Used for integration with third-party services (e.g., E-KYC, SMS, email systems). Must use `https` and remain consistent with the domain used during server deployment.  
**Example:** https://api.tradewisesoftware.com

---

## 2. User Agreement Settings
The user agreement is displayed on the registration page. Users must review and accept it before completing registration or login.

### • User Agreement Display Name
The name shown on the registration page.  
**Example:** User Agreement, Terms and Conditions

### • User Agreement URL/Address
The link to the agreement content. Must begin with `https`.  
File uploads are supported (PDF, TXT), and the system will automatically generate a URL after upload.  
**Example:** https://www.tradewisesoftware.com/terms.pdf

---

## 3. User Registration Settings

### (1) Registration Modes

#### • Two-Step Registration
Users complete registration by verifying their phone or email and can immediately log in.  
Additional information may be completed later within the system.  
**Best for:** Quick registration and onboarding.

#### • One-Step Registration
Users must complete all registration information on the registration page before entering the system.  
**Best for:** Platforms requiring full data collection upfront.

---

### (2) Referral Code Settings
Referral codes are normally provided by IBs (Introducing Brokers).  
If users access the registration page through an IB referral link, the system auto-fills the referral code.

#### Options:
- **Required**  
  Users must enter a referral code to register.  
  All users will be assigned to the IB who provided the referral code.

- **Optional (Recommended)**  
  Users may choose whether to enter a referral code.  
  Supports both organic traffic and IB-referred customers.  
  If no code is entered, the default referral code will be applied.

- **Disabled**  
  Referral codes are not used.  
  All users will be assigned under the IB specified in the default referral code.

---

### (3) Default Referral Code
When users do not provide a referral code (in Optional or Disabled mode), the system automatically assigns them to the IB specified by the default referral code.
