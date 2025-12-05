# Trading Server Setup

This section explains how administrators can configure trading servers within the system and how to set up client software download links. This configuration will affect the user's **trading environment connection**, **server display name**, and **client software download portal**.

---

## 1. Trading Server Function Items

### ⚙️ Basic Information Configuration

* **Trading Platform**
  Select the type of trading platform, such as MT4 or MT5.![1764928378015](images/trading_server_setup/1764928378015.png)
* **Live or Demo**
  Set the server environment type: **LIVE**, **DEMO**, or **LIVE & DEMO (Not Recommended)**.

  > #### ❗ LIVE & DEMO Configuration Principle (Best Practice)
  >
  > We **do not recommend** setting a server to LIVE & DEMO.
  >
  > If your **single physical trading server** supports both LIVE and DEMO environments, the **correct approach is:**
  >
  > * Add **two** server configurations in the CRM, using different **Manager Accounts** for connection.
  > * Server 1: Type: **LIVE**, Address `123.10.10.1:443`
  > * Server 2: Type: **DEMO**, Address `123.10.10.1:443`
  >
  > This method ensures that the front-end display, account opening rules, and risk control logic are completely separated, preventing environment confusion.
  >
* **Server Display Name**
  The name of the server displayed to the user on the client side.
* **Server Timezone**
  Select the timezone used by the server to ensure correct time display for trade history, open positions, etc.

### 🌐 Address and Connection Configuration

* **Server Address**
  The main IP address or domain name of the trading server.
* **Backup Server Address**
  The backup address used by the system to switch to when the primary server is unavailable.
* **Port Number**
  The port number used to connect to the trading server.

### 🔑 Authentication and Integration Configuration

* **Manager Account / Account ID**
  This field is used to enter the backend management account (Manager) or Account ID of the trading platform, used for CRM authentication with the trading server.
* **Password / API Key / Secret**
  Different trading platforms use different authentication methods:
  MT4/MT5 → Manager login password
  Custom System → Token / Key

  **❗Authentication information must be correct**, otherwise the CRM cannot connect to the server to perform account opening, balance inquiries, trade synchronization, etc.
  Fill in based on actual needs, such as starting account number, server account range, or prefix.

### 🔗 Terminal Link Configuration

* **Web Trading URL**
  The link to the WebTrader or web-based trading terminal provided for desktop browsers.
* **Mobile Trading URL**
  The link to the trading terminal or trading page used by mobile users.

### ⚠️ General Notes

* All server information **must be consistent with the actual trading platform backend.**
* If using multiple environments (Live/Demo), they must align with the actual server type.

---

## 2. Client Download URL Settings

This module allows administrators to configure the trading software download links for different platforms.

### 2.1 Enable Client Download URL

Controls whether the client download module is visible to users:

* **Enabled:** Users can see all download links.
* **Disabled:** Users cannot see any download items.

### 2.2 Download URL List

This list manages the software download or access links for different platforms:

* **Icon Style**
  Used to display the identifier for different platforms (e.g., Windows, Apple, Android).
* **Download URL Display Name**
  The name of the download item displayed to users (e.g., Windows OS, Live WebTrader).
* **Download URL**
  The actual link address for software download or access.

**Action:**

* **Edit:** Modify the download item.
* **Delete:** Delete the item.
* **Add:** Click to add a new download item, requiring the **Icon Style**, **Download URL Display Name**, and **Download URL** to be filled in.

### ⚠️ Download Link Notes

* Please ensure all download links are **valid and externally accessible addresses.**
* The download name must be **clear and explicit** to help users identify the platform type.
* **Android APK links** must lead to a properly signed file.
* **WebTrader links** are typically used for web-based trading.
* Avoid using temporary file links to prevent user download failures.
