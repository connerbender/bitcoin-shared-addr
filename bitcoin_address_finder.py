# Author: Conner Bender
# Version: Python 3.8.1

# IN:  Bitcoin address
# OUT: Number of addresses found, names of addresses and balance across all shared addresses

import requests
import json
import time

sharedAddr = []
balance = 0

def getTXAddr(addr):
    global balance
    tempAddr = []

    url = 'https://blockchain.info/rawaddr/'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    headers = {'User-Agent': user_agent}
    r = requests.get(url+addr, headers=headers)
    json_response = json.loads(r.text)

    balance += int(json_response['final_balance']) # fetch balance

    for t in json_response['txs']:
        for i in t['inputs']:
            if(i['prev_out']['addr'] == addr):
                for i in t['inputs']:
                  currentAddr = i['prev_out']['addr']
                  if(currentAddr not in sharedAddr):
                    tempAddr.append(currentAddr)
                    sharedAddr.append(currentAddr)
                    if(len(tempAddr) >= 50): # limit
                      for ta in range(len(tempAddr)):
                        time.sleep(5)
                        getTXAddr(tempAddr[ta])
                      tempAddr.clear() # empty out temp list
                break
    if(len(tempAddr) > 0):
        for ta in range(len(tempAddr)):
            time.sleep(5)
            getTXAddr(tempAddr[ta])

if __name__ == "__main__":
    stdin = input("Enter wallet address: ")

    sharedAddr.append(stdin)
    getTXAddr(stdin)

    print("\n********* SHARED ADDRESSES *********")
    for sa in range(len(sharedAddr)):
        print("#" + str(sa+1) + ": "+ str(sharedAddr[sa]))

    balance /= 100000000 # Satoshi to BTC
    print("\n[*] TOTAL BALANCE: " + str(format(balance, '.8f')) + " BTC")
