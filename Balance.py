from web3 import Web3
import prv_to_pbl
#from ethe_seed_rev import get_public
# QuickNode endpoint URL
QUICKNODE_ENDPOINT = 'https://eth-mainnet.g.alchemy.com/v2/8EOdAVzSiFFbykrWDoaWlBYbAW96BT_t'

# Connect to the QuickNode Ethereum node
w3 = Web3(Web3.HTTPProvider(QUICKNODE_ENDPOINT))

#for wallet in wallets:
while True:
    wallet= prv_to_pbl.prvtpub()
    balance = w3.eth.get_balance(wallet)
    if balance > 0:
        print(f'Wallet {wallet} has a balance of {balance} wei')
        break  # Stop once we find a wallet with a balance
    else:
        print(f'Wallet {wallet} has a balance of 0 wei')
