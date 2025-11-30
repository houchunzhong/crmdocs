# Trading Server Overview

The **Trading Server Management** module is designed to display and
manage the broker's trading infrastructure.\
The system uses a **three-level structure**: **Trading Server → Account
Type → Group**, providing a clear hierarchy that allows administrators
to manage different trading environments and account classifications in
a unified manner.

------------------------------------------------------------------------

## ① Trading Servers

Trading servers are used to centrally manage servers from different
trading platforms within the CRM, such as:

-   MT4\
-   MT5\
-   Match-Trader\
-   AQX Trader

and other third-party trading system platforms.

After a server is added, the system will automatically synchronize the
trading account information stored on the server. The module supports:

-   Viewing server status\
-   Synchronizing user groups (Groups)\
-   Managing account types (Account Types)

------------------------------------------------------------------------

## ② Account Types

Account Types are used to differentiate various trading rules and
trading models. Examples include:

-   Standard\
-   ECN\
-   Raw Spread\
-   Classic\
-   Cent / Mini

The functions of Account Types include:

-   Defining the account number range (Account Number Range)\
-   Setting the maximum number of accounts a user can create\
-   Establishing mappings to multiple Groups on the trading platform\
-   Displaying account rule descriptions on the client side (for display
    purposes only; does not affect actual trading logic)

------------------------------------------------------------------------

## ③ Groups

Each Account Type can correspond to multiple Groups on the trading
server. Different Groups under the same Account Type may have different
leverage settings. For example:

-   ECN-BB  1:100\
-   forex-hedge 1:500\
-   standard-usd 1:200\
-   cent-eur  1:500

By establishing an **Account Type ↔ Group** mapping in the CRM, the
account-opening process becomes automated and accurate.
