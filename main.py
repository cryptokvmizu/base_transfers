from web3 import Web3
import json

# Base Mainnet or Base Goerli Testnet RPC
BASE_RPC_URL = "https://mainnet.base.org"  # Use "https://goerli.base.org" for testnet
web3 = Web3(Web3.HTTPProvider(BASE_RPC_URL))

# Check connection
if not web3.is_connected():
    raise Exception("Failed to connect to Base network")

# Your wallet details
SENDER_ADDRESS = "0xYourWalletAddress"
PRIVATE_KEY = "0xYourPrivateKey"  # KEEP THIS SAFE, DON'T SHARE!
RECEIVER_ADDRESS = "0xRecipientWalletAddress"

# ERC-20 Token contract address (Example: USDC on Base)
TOKEN_CONTRACT_ADDRESS = "0xTokenContractAddress"

# ERC-20 Token ABI (Minimal ERC-20 ABI for transfer function)
ERC20_ABI = [
    {
        "constant": False,
        "inputs": [
            {"name": "_to", "type": "address"},
            {"name": "_value", "type": "uint256"},
        ],
        "name": "transfer",
        "outputs": [{"name": "", "type": "bool"}],
        "type": "function",
    }
]

# Connect to the token contract
token_contract = web3.eth.contract(address=TOKEN_CONTRACT_ADDRESS, abi=ERC20_ABI)

# Amount to send (Example: 10 tokens, adjust for token decimals)
DECIMALS = 18  # Adjust this based on token
AMOUNT_TO_SEND = 10 * (10**DECIMALS)  # Convert to smallest unit

# Get nonce
nonce = web3.eth.get_transaction_count(SENDER_ADDRESS)

# Create transaction
tx = token_contract.functions.transfer(RECEIVER_ADDRESS, AMOUNT_TO_SEND).build_transaction({
    "chainId": 8453,  # Base Mainnet chain ID (use 84531 for Base Goerli testnet)
    "gas": 100000,
    "gasPrice": web3.eth.gas_price,
    "nonce": nonce,
})

# Sign transaction
signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)

# Send transaction
tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

print(f"Transaction sent! Hash: {web3.to_hex(tx_hash)}")
