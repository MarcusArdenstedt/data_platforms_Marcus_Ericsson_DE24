from quixstreams import Application
from constants import COINMARKET_API
from requests import (Request, Session)
from requests.exceptions import (ConnectionError, Timeout, TooManyRedirects)
import json
import time



def get_coin_data(start= 1, limit= 5):

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    parameters = {
    'start': start,
    'limit': limit,
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': COINMARKET_API,
    }

    session = Session()
    session.headers.update(headers)

    
    response = session.get(url, params=parameters)
    return json.loads(response.text)["data"]

    



def main():

    app = Application(broker_address="localhost:9092", consumer_group="different_crypto")
    crypto_topic = app.topic(name="crypto", value_serializer="json")
    
    with app.get_producer() as producer:
        
        while True:
            coin_data = get_coin_data()
            
            for data in coin_data:
                
                kafka_msg = crypto_topic.serialize(key="crypto_list", value=data)
                
                print(f"Key = {kafka_msg.key:<10} value = id: {data['id']}, name: {data['name']}, pris: {data['quote']['USD']['price']}")
                
                producer.produce(topic= crypto_topic.name, key=str(kafka_msg.key), value= kafka_msg.value)

            print()
            time.sleep(10)

if __name__=='__main__':
    main()