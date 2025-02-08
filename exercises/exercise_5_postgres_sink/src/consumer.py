from quixstreams import Application
from constants import (
    POSTGRES_HOST,
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_PORT,
    POSTGRES_DBNAME,
)

from quixstreams.sinks.community.postgresql import PostgreSQLSink

# function to extract data
def extract_coin_data(message):
    latest_quote = message["quote"]["USD"]
    return {
        "id": message["id"],
        "coin": message["name"],
        "price_usd": latest_quote["price"],
        "volume": latest_quote["volume_24h"],
        "update": message["last_updated"],
    }



def create_postgres_sink():
    sink = PostgreSQLSink(
        host=POSTGRES_HOST,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        port=POSTGRES_PORT,
        dbname=POSTGRES_DBNAME,
        table_name="binance",
        schema_auto_update=True,
    )

    return sink



def main():
    app = Application(broker_address="localhost:9092", consumer_group="coin_group", auto_offset_reset="earliest")
    coins_topic = app.topic(name="BNB_coins", value_deserializer="json")
    
    sdf = app.dataframe(topic=coins_topic)

    # transfromation
    sdf = sdf.apply(extract_coin_data)
    
    sdf = sdf.update(lambda coin_data: print(coin_data))
    
    
    # sink to postgres
    postgres_sink = create_postgres_sink()
    sdf.sink(postgres_sink)
    
    
    app.run()

if __name__=='__main__':
    main() 