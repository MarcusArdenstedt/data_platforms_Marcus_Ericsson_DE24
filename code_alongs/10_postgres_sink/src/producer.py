from quixstreams import Application
from constants import COINMARKET_API
from requests import Session
import json
from pprint import pprint
import time


def get_latest_coin_data(target_symbol = "BTC"):
    API_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest" 


    parameters = {
    'symbol': target_symbol,
    'convert': 'USD'
    }
    
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': COINMARKET_API,
    }

    session = Session()
    session.headers.update(headers)


    response = session.get(API_URL, params=parameters)
    return json.loads(response.text)["data"][target_symbol]


    
def main():
    app = Application(broker_address="localhost:9092", consumer_group="coin_group")
    coins_topic = app.topic(name="coins", value_serializer= "json")
    
    with app.get_producer() as producer:
        while True:
            coin_latest = get_latest_coin_data("BTC")
            
            kafka_msg = coins_topic.serialize(key=coin_latest["symbol"], value=coin_latest)
            
            print(f"producer event with key = {kafka_msg.key}, price = {coin_latest['quote']['USD']['price']}")
            
            producer.produce(
                topic=coins_topic.name, key= kafka_msg.key, value= kafka_msg.value
            )
        
            time.sleep(10)


    
if __name__=='__main__':
    main()
    
 
