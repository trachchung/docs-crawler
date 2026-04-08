<!-- Source: https://docs.payram.com/mcp/analytics-mcp -->

### 
Introduction
The PayRam Telegram Analytics Bot provides direct access to PayRam analytics from Telegram. Once configured, authorized users can query payments, users, payouts, and activity without accessing the PayRam dashboard.
The bot connects securely to the PayRam Analytics server and responds only in allowlisted chats, enabling teams to monitor metrics, generate summaries, and obtain insights directly within Telegram.
### 
Prerequisites
Before setting up the PayRam Telegram Analytics Bot, ensure the following requirements are met:
  * A server (VPS or dedicated machine) where the bot will be deployed and run
  * A running PayRam server with analytics enabled
  * PayRam dashboard **admin credentials** (email and password)
  * A Telegram bot token created using **@BotFather**
    * Refer to this guide for setup instructions: <https://blog.devgenius.io/how-to-set-up-your-telegram-bot-using-botfather-fd1896d68c02>[arrow-up-right](https://blog.devgenius.io/how-to-set-up-your-telegram-bot-using-botfather-fd1896d68c02)
  * An OpenAI API key for generating analytics responses
  * Docker installed on the server


### 
Installation
#### 
Run the setup script
Copy
```
./setup_payram_agent.sh
```

#### 
Provide required configuration details
  * During the setup process, you will be prompted to enter the following information:
    * **Publicly accessible PayRam Server URL**
      * This URL must be reachable by the analytics bot.
    * **PayRam dashboard admin credentials**
      * The admin email and password used to authenticate the analytics bot with your PayRam server.


  * **OpenAI API Key**
    * Required to enable AI-powered analytics responses.
  * **Telegram Bot Token**
    * The token generated via **@BotFather** for your Telegram bot.
  * **Allowed Telegram Users**
    * A comma-separated list of Telegram usernames that are permitted to interact with the bot.
  * **Auto-Updates (Optional)**
    * Choose whether the analytics bot should automatically update itself when new versions of the Analytics MCP server are released.
  * **Start Container After Setup (Optional)**
    * Choose whether to start the analytics agent Docker container immediately after the setup completes.


If you choose to start the container during setup, the Analytics MCP server will be installed and running once the process completes. You can then open Telegram and begin using the bot.
#### 
Using the Telegram Analytics Bot
Once the setup is complete, open Telegram and send a message to the bot from an allowlisted chat. The bot will respond with PayRam analytics in the same chat.
**Example Queries:**
  * **“Show me today’s payments summary.”**
  * **“Create a payment link for 3 USD on the main project with email example@gmail.com and customerId cust-123.”**
  * **“Top paying users this week.”**
  * **“Deposit distribution by chain for the last 7 days.”**
  * **“Payouts by currency for December.”**
  * **“User growth compared to the previous period.”**


> **Access Control Note**
> If you message the bot from a chat that is not allowlisted, it will respond with an **“Access denied”** message along with the `chat_id`. Add this `chat_id` using the allowlist update command, then retry your request.
### 
Managing Bot Access
You can grant access to additional users or groups without rerunning the full setup by using the commands below.
#### 
Add Telegram Usernames (Recommended)
Use this option to allow individual Telegram users to interact with the analytics bot:
Copy
```
./setup_payram_agent.sh --add-telegram-usernames "alice,@bob,t.me/carol"
```

> **Notes:**
>   * Usernames can be provided with or without the  prefix or `t.me/` format.
>   * Multiple usernames must be comma-separated.
> 

#### 
Add Telegram Chat IDs (For Groups)
Use this to allow Telegram groups or chats:
Copy
```
./setup_payram_agent.sh --add-telegram-chat-ids "12345,67890"
```

[PreviousPayRam MCPchevron-left](https://docs.payram.com/mcp/payram-mcp)[NextPayment Linkschevron-right](https://docs.payram.com/features/payment-links)
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](http://payram.com/privacy-policy).
close
AcceptReject
