from quixstreams import Application
from pathlib import Path
import json
from pprint import pprint

app = Application(broker_address="localhos:9092", consumer_group= "text-splitter")

print()
# print(app)


jokes_topic = app.topic(name="jokes", value_serializer="json")

jokes_path = Path(__file__).parents[1] / "data" / "jokes.json"

with open(jokes_path, 'r', encoding="utf-8") as file:
    jokes = json.load(file)
    
    
def main():
    with app.get_producer() as producer:
        print(producer)
        
if __name__=='__main__':
    main()
