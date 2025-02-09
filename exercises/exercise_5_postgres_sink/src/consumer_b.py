from quixstreams import Application
from pprint import pprint
from constants import (
    POSTGRES_DBNAME,
    POSTGRES_HOST,
    POSTGRES_PASSWORD,
    POSTGRES_PORT,
    POSTGRES_USER,
)

from quixstreams.sinks.community.postgresql import PostgreSQLSink



def transformation(data):
    quote = data["quote"]["USD"]
    return {
        "update": quote["last_updated"],
        "id": data["id"],
        "name": data["name"],
        "price": quote["price"],
        "circulating_supply": data["circulating_supply"],
        "percent_change_24h": quote["percent_change_24h"],
    }

def create_postgres_sink():
    sink = PostgreSQLSink(
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        dbname=POSTGRES_DBNAME,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        table_name="currency",
        schema_auto_update=True,
    )
    
    return sink




def main():
    app = Application(broker_address="localhost:9092", consumer_group="different_crypto", auto_offset_reset="earliest")
    crypto_topic = app.topic(name="crypto", value_deserializer="json")
    
    sdf = app.dataframe(topic= crypto_topic)
    
    # Transformation 
    sdf = sdf.apply(transformation)
    
    sdf = sdf.update(lambda message: pprint(message))

    # sink to postgres
    postgres_sink = create_postgres_sink()
    sdf.sink(postgres_sink)
    
    app.run()

if __name__=='__main__':
    main()