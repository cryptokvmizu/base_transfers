# ERC-20 Token Transfer on Base Network

This Python script allows you to transfer ERC-20 tokens between wallets on the **Base network** using Web3.py.

## Prerequisites

1. **Python 3.7+** installed.
2. Install required dependencies:
   ```sh
   pip install web3
   ```
3. **A funded wallet** on Base Mainnet or Base Goerli (testnet) with ETH for gas fees.
4. The **ERC-20 token contract address** of the token you want to transfer.
5. The **recipient's wallet address**.
6. Your **private key** (Keep it safe and do NOT share it!).

## Setup

1. Clone this repository or download the script.
2. Open `transfer.py` and update the following variables:
   ```python
   SENDER_ADDRESS = "0xYourWalletAddress"
   PRIVATE_KEY = "0xYourPrivateKey"
   RECEIVER_ADDRESS = "0xRecipientWalletAddress"
   TOKEN_CONTRACT_ADDRESS = "0xTokenContractAddress"
   DECIMALS = 18  # Update based on the token
   AMOUNT_TO_SEND = 10 * (10**DECIMALS)  # Amount to transfer
   ```
3. Ensure the **Base RPC URL** is correct:
   ```python
   BASE_RPC_URL = "https://mainnet.base.org"  # Use "https://goerli.base.org" for testnet
   ```

## Usage

Run the script:
```sh
python transfer.py
```

If successful, you'll see an output with the transaction hash:
```sh
Transaction sent! Hash: 0xabcdef123456...
```
You can track the transaction on [Basescan](https://basescan.org/) using the hash.

## Important Notes

- **Private Key Security**: Never hardcode your private key in public repositories. Use environment variables or a secure vault.
- **Gas Fees**: Ensure you have enough ETH on Base to cover transaction fees.
- **Token Decimals**: Check the token's decimals before sending.

## Chain IDs
- **Base Mainnet**: `8453`
- **Base Goerli (Testnet)**: `84531`

## License
This project is open-source and available under the MIT License.

