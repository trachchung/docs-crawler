<!-- Source: https://docs.payram.com/script -->

## 
Commands
### 
**Mainnet installation**
  * **Install PayRam on the mainnet (production environment):**
Copy
```
/bin/bash-c"$(curl-fsSL https://raw.githubusercontent.com/PayRam/payram-scripts/main/setup_payram.sh)"bash--mainnet
```



### 
**Testnet installation**
  * **Install PayRam on the mainnet (Development environment):**
Copy
```
/bin/bash-c"$(curl-fsSL https://raw.githubusercontent.com/PayRam/payram-scripts/main/setup_payram.sh)"bash--testnet
```



### 
Update
  * To update the PayRam container to the latest version, run the following command:
Copy
```
/bin/bash-c"$(curl-fsSL https://raw.githubusercontent.com/PayRam/payram-scripts/main/setup_payram.sh)"bash--update
```



### 
Reset
  * To completely reset the PayRam server configuration and perform a clean uninstallation, including the removal of all Docker images, run the following command:
Copy
```
/bin/bash-c"$(curl-fsSL https://raw.githubusercontent.com/PayRam/payram-scripts/main/setup_payram.sh)"bash--reset
```



### 
Restart
  * To restart the PayRam server and refresh all active services without removing any data or configurations, run the following command.This will safely restart PayRam, helping to resolve issues such as unprocessed blocks or inactive services


Copy
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/PayRam/payram-scripts/main/setup_payram.sh)" bash --restart
```

[PreviousBitcoin Funds Sweep Guidechevron-left](https://docs.payram.com/onboarding-guide/funds-sweeping/bitcoin-funds-sweep-guide)[NextIntroductionchevron-right](https://docs.payram.com/api-integration/introduction)
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](http://payram.com/privacy-policy).
close
AcceptReject
