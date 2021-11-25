from brownie import network, config, FundMe, MockV3Aggregator

from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    deploy_mocks,
    get_account,
)


def deploy_fund_me():
    account = get_account()

    # if we are on a development network
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    # if we are on a persistent network
    else:
        price_feed_address = config["networks"][network.show_active()].get(
            "eth_usd_price_feed"
        )

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
