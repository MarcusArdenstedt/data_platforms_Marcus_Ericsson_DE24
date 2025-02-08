from quixstreams import Application
from constants import COINMARKET_API
from requests import Session
import json
from pprint import pprint
import time


def get_latest_coin_data(target_symbol="BNB"):

    API_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

    target_symbol = "BNB"

    parameters = {"symbol": target_symbol, "convert": "USD"}

    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": COINMARKET_API,
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(API_URL, params=parameters)
    return json.loads(response.text)["data"][target_symbol]


def main():
    app = Application(broker_address="localhost:9092", consumer_group="coin_group")
    coins_topic = app.topic(name="BNB_coins", value_serializer="json")

    with app.get_producer() as producer:
        while True:
            coin_latest = get_latest_coin_data("BNB")

            kafka_message = coins_topic.serialize(
                key=coin_latest["symbol"], value=coin_latest
            )

            print(
                f"Producer event with key: {kafka_message.key}, Price: {coin_latest['quote']['USD']['price']:.2f}"
            )

            producer.produce(
                topic= coins_topic.name, key=kafka_message.key, value=kafka_message.value
            )

            time.sleep(10)


if __name__ == "__main__":
    main()
