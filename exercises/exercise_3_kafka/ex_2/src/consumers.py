from quixstreams import Application

app = Application(
    broker_address="localhost:9092",
    consumer_group="order",
    auto_offset_reset="earliest",
)

order_topics = app.topic(name="orders", value_deserializer= "json")

sdf = app.dataframe(topic= order_topics)

sdf = sdf.update(lambda order: print(f"\nInput: {order}"))

def process_order(data):
    
    total = 0
    for product in data["products"]:
       print(f"Product: {product['name']:<20} Quantity: {product['quantity']:<20} Price: {product['price']}")
       total = product["quantity"] * product["price"]
    print(f"Total price: {total}")

sdf = sdf.update(lambda message: print("Output:"))
sdf = sdf.apply(process_order)


if __name__=='__main__':
    app.run()