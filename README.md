# bitcoin-shared-addr
A simple Python script that recursively searches for all shared addresses involved in transactions—and computes total balance—with the provided Bitcoin address.

## Requirements
* Python 3.8+
* `requests` library

## Installation

1. Clone the repository:
```
git clone https://github.com/connerbender/bitcoin-shared-addresses.git
```

2. Navigate to the directory:
```
cd bitcoin-shared-addresses
```

3. Install the required dependencies:
```
pip install requests
```

## Usage
Run the script and provide a Bitcoin wallet address when prompted:
```
python3 bitcoin_address_finder.py
```

Enter a Bitcoin address when prompted. The script will then recursively search and display the shared addresses and the total balance across them.

Example input:
```
Enter wallet address: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
```

Output:
```
********* SHARED ADDRESSES *********
#1: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
#2: 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2
...

[*] TOTAL BALANCE: 10.12345678 BTC
```

## Notes
The script uses the `blockchain.info` API to fetch transaction data for the provided Bitcoin address. It extracts the inputs from each transaction and tracks the shared addresses.
The script recursively follows up to 50 shared addresses per iteration to prevent rate-limiting by the API. The balance of the initial address and all linked addresses is calculated and displayed.

The script makes use of `time.sleep(5)` to prevent overloading the API by spacing out requests. It converts the balance from satoshis to Bitcoin (1 BTC = 100,000,000 satoshis).

## License
This project is licensed under the MIT License.
