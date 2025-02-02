from quixstreams import Application

# Create an Application - the main configuaration entry point
app = Application(broker_address="localhost:9092", consumer_group="text-splitter-v1")

# Define a topic with chat message in json format
message_topic = app.topic(name="message", value_serializer="json")

messages = [
    {"chat_id": "id1", "text": "Lorem ipsum dolor sit amet"},
    {"chat_id": "id2", "text": "Consectetur adipiscing elit sed"},
    {"chat_id": "id3", "text": "Do eiusmod tempor incididunt ut labore et"},
    {"chat_id": "id4", "text": "Mollis nunc sed id semper"},
]


def main():
    with app.get_producer() as producer:
        for message in messages:
            # Serialize chat message to send it to kafka
            # Use "chat_id" as kafka message key
            kafka_msg = message_topic.serialize(key=message["chat_id"], value=message)
            
            # Produce chat maessage to the topic
            print(f'Produce event with key= "{kafka_msg.key}" value = "{kafka_msg.value}"')
            producer.produce(
                topic=message_topic.name,
                key=kafka_msg.key,
                value=kafka_msg.value,
            )
    
       
if __name__ == '__main__':
    main()