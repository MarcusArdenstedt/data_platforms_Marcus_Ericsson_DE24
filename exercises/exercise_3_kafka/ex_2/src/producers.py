from pathlib import Path
from pprint import pprint
import json
from quixstreams import Application

# The path where data is located
data_path = Path(__file__).parents[1]/"data"

# open with context manager and json.load() to convert it to python dictionary 
with open(data_path/"orders.json", "r") as file:
    data = json.load(file)
    
# pprint(data)

app = Application(broker_address= "localhost:9092", consumer_group="order")

# print(app)

order_topics = app.topic(name= "orders", value_serializer= "json")

# print(order_topics)

def main():
    with app.get_producer() as producer:
        # print(producer)
        
        for order in data:
            # print(order)
            
            kafka_msg = order_topics.serialize(key= order, value= order)
            print(f"Input: {kafka_msg.key}\n")
            
            
            # total = 0
            # for product in order["products"]:
            #     print(f"Product: {product['name']:<20} Quantity {product['quantity']:<20} Price: {product['price']}")
            #     total += product["quantity"] * product["price"]
            
            # print(f"Total price: {total:.2f}")
            
            producer.produce(topic= order_topics.name, key= str(kafka_msg.key), value=kafka_msg.value)
        


# run this code only when executing this script and not when importing this modul
if __name__=='__main__':
    main()

