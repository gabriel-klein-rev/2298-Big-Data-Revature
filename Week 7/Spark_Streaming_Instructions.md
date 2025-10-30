# Spark Streaming Instructions

## Set up a data server

Open a terminal and run the following command:

```
nc -lk 9999
```

This is where you will send data.

## Unstructured Streaming with DStreams

Open pyspark shell, then run the following:

```
ssc = StreamingContext(sc, 3)

# Create a DStream that will connect to hostname:port, like localhost:9999
lines = ssc.socketTextStream("localhost", 9999)

# Split each line into words
words = lines.flatMap(lambda line: line.split(" "))

# Count each word in each batch
pairs = words.map(lambda word: (word, 1))
wordCounts = pairs.reduceByKey(lambda x, y: x + y)

# Print the first ten elements of each RDD generated in this DStream to the console
wordCounts.pprint()

ssc.start()             # Start the computation
```

When you type in the first terminal, your output should appear in the pyspark shell.

## Structured Streaming with Dataframes

Open pyspark shell, then run the following:

```
from pyspark.sql.functions import explode
from pyspark.sql.functions import split

# Create DataFrame representing the stream of input lines from connection to localhost:9999
lines = spark.readStream.format("socket").option("host", "localhost").option("port", 9999).load()

# Split the lines into words
words = lines.select(explode(split(lines.value, " ")).alias("word"))

# Generate running word count
wordCounts = words.groupBy("word").count()

query = wordCounts.writeStream.outputMode("complete").format("console").start()
```

When you type in the first terminal, your output should appear in the pyspark shell.