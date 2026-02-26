# 💰 Commission and Product Classification Configuration Guide

Commission configuration is the core module for managing agent commissions in the CRM system. By scientifically classifying trading products, administrators can implement refined commission management for different trading environments (servers + groups).

## 1. Product Classification (Product Type)

All trading products (Symbols) are synchronized in real-time from trading systems like MT5 to the CRM. Administrators need to classify these products based on commission standards.

- **Classification Principle**  
  The key to product classification is "consistency in commission." Only products with exactly the same commission scheme should be classified under the same type. If the commission standards differ, different categories must be created for distinction.

- **Example Explanation**  
  If the commission for EUR/USD is \$2, while GBP/USD or USD/JPY has a commission of \$3, they cannot be placed in the same type and must be classified separately, similar to Forex.Major and Forex.Cross.

⚙ **Core Configuration Items**  
- **Product Type Name**  
  Set clear category names, such as Forex.Standard or Metal.Standard.

- **Uncategorized Products**  
  Display a list of products synchronized from the trading server that have not yet been categorized. Click Sync Products to manually trigger synchronization.

- **Selected Items**  
  Move the products to be assigned from the left side to the right side to complete the categorization of this category.

## 2. Commission Plan

After completing product classification, administrators need to set specific commission schemes in the commission plan, combining three dimensions: "Trading Server," "Group," and "Product Type."

⚙ **Key Configuration Logic**  
The commission plan uses the following combination dimensions for differential pricing:
- **Trading Server**: Select the corresponding physical trading environment.
- **Group Name**: Specify the account group corresponding to the trading platform.
- **Product Type**: Choose the category defined in the previous step.

💵 **Commission Parameter Settings**
Administrators can set the following in the corresponding line items:
- **Spread Rebate**  
  Rebates the spread profit to the agent per Lot.  
  Example: For stocks traded in the MIM_S_B group, set the spread rebate to \$2.

- **Commission Rebate**  
  Rebates the service fee to the agent per Lot.  
  Example: For stocks traded in the MIM_S_B group, set the commission rebate to \$3.

⚠ **Management Rules**  
- **Upper Level Difference Setting**: The "Upper Agent Receives Spread/Commission Difference" switch can be turned on, allowing the system to automatically calculate the position differences between multiple levels of agents.
- **Same Level Commission Limitation**: Configure whether agents can earn commissions from their own trades (usually generated only when they act as customers of their upper-level agents).

## 📅 Settlement Plan

The settlement plan defines the time frame and method for agent commissions to transition from "Pending Settlement" status to "Available Balance." The system supports flexible automated settlements and manual review mechanisms.

### 1. Commission Settlement Logic
- **Real-time Calculation**  
  Commissions are calculated immediately by the system based on the preset "commission plan" after users complete their trades.

- **Pending Commission**  
  The calculated commissions will first appear in the Pending Commission section of the agent panel, and the funds have not yet entered the agent's wallet.

- **Formal Settlement**  
  When the designated time point defined in the settlement plan is reached, Pending Commission will be transferred to the agent's wallet as available balance according to the distribution rules.

### 2. Settlement Cycle Settings

Administrators can configure different settlement cycles for different agents or account groups according to business needs:
- **Real-time**  
  Settlement is completed and posted immediately after the transaction.

- **Daily**  
  Settlement occurs at a specified time every day.  
  Example: Manual - Daily at 16:00

- **Weekly**  
  Settlement occurs on a specified day of the week.  
  Example: Automatic - Every Thursday at 15:00

- **Monthly**  
  Settlement occurs on a fixed date each month.  
  Example: Automatic - Monthly on the 25th at 00:00

### 3. Distribution Method (Settlement Review)

The system provides two primary review and distribution modes to ensure fund security:
- **Automatic Distribution**  
  The system automatically executes settlement operations at the designated time without manual intervention.

- **Manual Review**  
  When the settlement time is reached, the system will generate a "Settlement Review Document."  
  The administrator must enter the backend for review, and commissions will only be formally distributed to the agent's wallet after passing the review.

### 4. Core Configuration Item Descriptions

When adding or editing a settlement plan, the following key information must be filled out:
- **Settlement Plan Name**  
  Used to differentiate various settlement rules.  
  Example: Automatic - Monthly on the 25th at 00:00

- **Settlement Date & Time**  
  Specify the exact settlement trigger time, noting the system time zone settings.

- **Remarks**  
  Used to record any special notes or internal audit numbers related to the settlement plan.

## 👤 User Level and Plan Management (User Level Management)

The user level module is the core configuration center of the system. By associating uniform account opening plans, commission plans, and settlement plans with different levels, administrators can efficiently manage a large number of users. Additionally, the system supports personalized configurations for specific agents to meet complex business needs.

### 1. User Level Configuration (User Level Setup)

Administrators can customize multiple user levels (such as New Client, Platinum, IB, Super IB, etc.) and preset a standard "plan package" for each level.
- **Account Opening Plan**  
  Define the rules that users of this level must follow when opening accounts (e.g., leverage, account types, etc.).

- **Commission Plan**  
  Associate preset product classification commission standards.

- **Settlement Plan**  
  Specify the distribution cycle and review mode (automatic or manual) for agent commissions at this level.