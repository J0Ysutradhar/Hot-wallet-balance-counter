# Hot Wallet Balance Checker
![HotWallet](https://i.ibb.co.com/YhysR9M/image.png "HotWallet Logo")

This script is designed to check the balance of multiple hot wallets using the [HotScan](https://hotscan.org) website. It leverages Selenium WebDriver to automate the process of navigating to each wallet's URL and extracting balance information.

## Features

- Fetches balance data for multiple wallet addresses.
- Logs the total balance of all wallets into a text file.
- Provides detailed error handling and reporting for failed balance retrievals.
- Outputs the total number of successfully processed wallets.

## Prerequisites

1. Python 3.x installed on your system.
2. Selenium library installed. You can install it using:
   ```bash
   pip install selenium
   ```
3. Google Chrome browser installed.
4. ChromeDriver compatible with your Chrome browser version. Download it from [ChromeDriver](https://chromedriver.chromium.org/downloads) and ensure it is added to your system's PATH or the script's directory.

## Installation

1. Clone this repository or download the script file `HotWallet.py`.
2. Ensure all prerequisites are installed and set up.

## Usage

### Step 1: Configure Wallet Addresses

Replace the wallet addresses in the `js_usernames` list with the ones you want to monitor:
```python
js_usernames = [
    "wallet1", "wallet2", "wallet3"  # Add your wallet addresses here
]
```

### Step 2: Run the Script

Execute the script using Python:
```bash
python HotWallet.py
```

### Output

1. The script will display the balance of each wallet in the console.
2. If a balance cannot be retrieved, the script will log an error message with a direct link to the wallet.
3. The total balance of all wallets will be saved in a file named `JShot.txt` with a timestamp.

Example Console Output:
```
wallet1 Balance: 1234.56
wallet2 Balance: 7890.12
|:>|||||||||||||==================>Error fetching balance for 'wallet3' Try manually with this link https://hotscan.org/wallet/wallet3
<<-------------------------------------------------------->>
Total 'HOT' token: 9124.68
Total Hot wallet counted 2/3
```

## Notes

1. The script pauses for a second (`time.sleep(1)`) between requests to avoid being flagged by the website.
2. Errors are gracefully handled, and manual links are provided for failed requests.
3. Ensure your wallet addresses are accurate to prevent incorrect balance fetching.

## Customization

- **Adding More Wallets:** Simply append wallet addresses to the `js_usernames` list.
- **Change Output File:** Modify the filename in the following section:
  ```python
  with open("JShot.txt", "a") as f:
      f.write(str(hot)+f" HOT token at {time}" "\n")
  ```

## Troubleshooting

1. **Browser Issues:** Ensure ChromeDriver matches your Chrome version.
2. **Selenium Errors:** Check that Selenium is installed and ChromeDriver is in your PATH.
3. **Website Changes:** If the HotScan website updates its structure, you may need to update the XPath used to fetch the balance:
   ```python
   balance_element = driver.find_element(By.XPATH, "//h2[@class='sc-gueXAH VAnti']")
   ```

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute this script.
