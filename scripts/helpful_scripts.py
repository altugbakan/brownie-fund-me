from brownie import network, accounts, config, MockV3Aggregator

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache"]
DECIMALS = 8
STARTING_PRICE = 400000000000


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    if len(MockV3Aggregator) <= 0:
        print("\nDeploying mocks...")
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
