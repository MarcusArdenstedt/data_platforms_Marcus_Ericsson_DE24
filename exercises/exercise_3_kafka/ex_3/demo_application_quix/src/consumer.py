from quixstreams import Application

# Create an Application - th main configuration entry point
app = Application(
    broker_address="localhost:9092",
    consumer_group="text-splitter-v1",
    auto_offset_reset="earliest",
)

# Define a topic whit chat message in json format
message_topic = app.topic(name="message", value_deserializer="json")


# Create a streamingDataFrame - the stream processing pipline 
# with a Pandas-like interface on streaming data
sdf = app.dataframe(message_topic)

# Print the input data
sdf = sdf.update(lambda message: print(f"Input: {message}"))

# Define a transfomation to split incoming sentences
# into words using a lambda function 
sdf = sdf.apply(lambda message: [{"text" : word} for word in message["text"].split()], expand=True)


# calculate the word length and store the result in th column
sdf["length"] = sdf["text"].apply(lambda word: len(word))

# Print the output result
sdf = sdf.update(lambda row: print(f"Output: {row}"))



# Run the streaming application 
if __name__ == '__main__':
    app.run()