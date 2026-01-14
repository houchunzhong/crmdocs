# My Investment Markets (MIM) CRM Login and Registration Process Overview

This guide will detail the complete process of logging in and registering for the **My Investment Markets (MIM)** client, with operational steps illustrated through interface screenshots to help users quickly create an account and log in.

---

## 1. Homepage: Registration/Login Entry

After entering the MIM official website, users will see the main login page, containing the following core functionalities:

### Page Layout Overview

- **Top Left Logo**: `MM My Investment Markets`, clicking returns to the homepage.
- **Theme Toggle Button**: `Day/Night`, supports switching between daytime and nighttime modes.
- **Left Background Image**: Displays a preview of the CRM backend interface, enhancing professionalism and credibility.
- **Right Side Login Form Area**: Offers two login methods: phone number or email.

---

### 1. Select Login Method

Users can switch between logging in with “Phone Number” and “Email”:

| Option | Description |
|--------|-------------|
| ✅ Phone Number | Recommended, supports international number input, automatically detects country code |
| 📧 Email | Suitable for users who prefer to log in with email |

> Default displays the "Phone Number" option.

---

### 2. Enter Phone Number (Example: Singapore)

#### Steps:

1. Click the country code dropdown (default is `+65`).
2. Select the target country from the popup list, for example:
   
   - `+65` Singapore (selected)
   - `+60` Malaysia
   - `+61` Australia
   - `+63` Philippines
   - etc.
3. Fill in the phone number in the right input box (e.g., `81388988`).

> ✅ Example: `+65 81388988`

---

### 3. Enter Password and Verify

1. In the password input field below, enter your account password.
2. The password must meet the system security requirements. If not filled in, a prompt will appear:
   
   > ❌ **Input cannot be empty**
3. Check two necessary agreement options:
   
   - ☑ I have read and agree to the **Terms and Conditions**
   - ☑ I confirm that I am not a U.S. citizen.
4. Option to log in using the verification code or click “Forgot Password??” for recovery.

---

### 4. Submit Login

Click the black button at the bottom:

> 🔹 **Register/Login**

- If you already have an account → log in directly to the client backend.
- If you do not have an account → enter the registration process (usually guided by the system to complete the information).

---

## 2. After Successful Login: Client Entry Homepage

Upon successful login, you will be redirected to the **MIM Client Center Homepage**, as shown below:

### Top Navigation Bar

- **Language Settings**: Currently set to "Chinese-Traditional", can switch to other languages.
- **User Avatar and Name**: Displays the logged-in user's information (e.g., Stella lili), clicking allows you to view personal details.
- **Notification Prompt**: Green prompt bar showing "Success: Language settings have been changed".

---

### Left Side Menu Bar

| Icon | Menu Item | Function Description |
|------|-----------|---------------------|
| 📊 | Trading | Quickly access trading platform |
| 🟡 | Home | Return to main control panel |
| 💳 | Funds | View fund flow, deposits, withdrawals |
| 👤 | Trading Accounts | Manage multiple trading accounts |
| 🤝 | Partners | View referral rewards and invitation links |
| 🧑‍💼 | Personal Center | Modify personal information, contact details, etc. |
| 🔄 | Trading Platform | Download trading software like MT5, MT4 |

---

### Main Content Area

#### 1. Financial Overview Card

| Module | Amount | Function |
|--------|--------|----------|
| **Total Assets** | \$7,545.78 | Shows total net worth |
| **MIM AQX Balance** | \$268.29 | Specific account balance |
| **MIM BO Balance** | \$132.80 | Another sub-account balance |
| **MIM MT5 Balance** | \$500.00 | Available funds on the MT5 platform |
| **Available Balance** | \$6,644.69 | Actual tradable amount |

> ⭐ Each card has an "Trade Now" button in the upper right corner for quick access to the corresponding platform.

---

#### 2. Notification Bar

- Displays the latest system notifications and messages.
- Example:
  - `Number of Recipients` (12-08-2025)
  - `System Upgrade Notification`
  - `Welcome to MIM`
- Supports pagination for browsing (total 4 items).

---

#### 3. Welcome to MIM MT5

- Provides multi-platform download links:
  - 📱 **MT5 iOS APP**
  - 🤖 **MT5 Android...**
  - 💻 **MT5 PC**
- Emphasizes it as a "Multi-Platform Multi-Trading Server," supporting cross-device trading.

---

#### 4. Invitations and Rewards

- Displays the user's exclusive invitation code and link:
  - 🎯 **Invitation Code**: `9AZFB6`
  - 🔗 **Invitation Link**: `https://mimclient.tradewisesoftware.com/#/login/9AZFB6`
- Users can copy and share this with others for promotion and reward programs.

---

#### 5. QR Code

- A QR code is provided at the bottom right corner, allowing direct access to the client entrance or download the client.

---

## 3. Summary: Login Process Flowchart

```mermaid
graph TD
    A[Visit Official Website] --> B{Choose Login Method}
    B --> C[Phone Number]
    B --> D[Email]
    C --> E[Enter Country Code + Phone Number]
    E --> F[Enter Password]
    F --> G[Check Agreement Terms]
    G --> H[Click "Register/Login"]
    H --> I[Enter Client Backend]