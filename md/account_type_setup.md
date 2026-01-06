# Account Type Setup

Account types are used to categorize trading accounts, such as Standard accounts, ECN accounts, Cent accounts, etc.
They represent different trading models and parameters, allowing brokers to offer differentiated trading experiences to users.

The content of an account type is divided into two categories:

---

## 1. Configuration Items

### Account Number Range

Defines the range of account numbers available for this account type within the Trading Server.
The system will automatically select the next available account number within this range when creating a new account.

**Example:** 500000 – 500200
This indicates that up to **200 accounts** can be generated under this account type.

---

### Max Accounts Per User

Specifies the maximum number of accounts of this type that each user is allowed to create.

**Example:**  
If set to **3**, a user may open **up to 3** accounts of this type.

---

### Group Mapping

An account type can be linked to multiple user groups within the trading server, such as:

- ECN-BB
- forex-hedge
- standard-usd

During account creation, the system will automatically use the mapped group to ensure the correct trading rules are applied.

---

## 2. Front-End Display Rules (Display Only)

The following fields are **only displayed to users** as account information.
They do **NOT** affect the actual configuration on the trading server:

**Example:**  
- **Spread:** From 1.2 pips
- **Commission:** No commission
- **Minimum Deposit:** 5000 USD
- **Minimum Trade:** 0.05 lot
- **Leverage:** 1:200
- **Products:** FX, CFDs, Metal, Oil
- **Margin Call Level:** 200%
- **Stop Out Level:** 50%
- **EA Trading:** Allow

These fields serve as descriptive information only, helping users understand the characteristics and rules of the account type.
