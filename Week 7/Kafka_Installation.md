# Kafka Installation Instructions

## 1. Install Kafka in Ubuntu
```
wget https://archive.apache.org/dist/kafka/2.6.0/kafka_2.13-2.6.0.tgz
```

## 2. untar the Kafka archive, and cd to the kafka directory:
```
tar -xzf kafka_2.13-2.6.0.tgz
cd kafka_2.13-2.6.0
```

Run the ls -al command to list the contents of the kafka directory:


## 3. Run the following command to start ZooKeeper:
```
cd  kafka_2.13-2.6.0
bin/zookeeper-server-start.sh config/zookeeper.properties
```

There will be a lot of messages, and ZooKeeper will be ready in a short time, typically around a second or two.

## 4. Start server

Open another terminal session. Change the directory to the kafka directory, and start the Kafka broker:

```
cd kafka_2.13-2.6.0
bin/kafka-server-start.sh config/server.properties
```

## 5. Create Producer

Open another terminal session and run the kafka-topics command to create a Kafka topic named topic-1:
```
cd kafka_2.13-2.6.0
bin/kafka-topics.sh --create --topic topic-1 --bootstrap-server localhost:9092
```

Start Producer:

```
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic topic-1
```

## 6. Start Consumer

Open another terminal Start Consumer

```
cd kafka_2.13-2.6.0
bin/kafka-console-consumer.sh --topic topic-1 --from-beginning --bootstrap-server localhost:9092
```

## 7. Test
In the producer terminal, type a few messages, and watch as they appear in the consumer terminal.

## 8. Stop Kafka
1.	Stop the consumer and producer clients with Ctrl+C
2.	Stop the Kafka broker with Ctrl+C
3.	Stop the ZooKeeper server with Ctrl+C
4.	Run the following command to clean up:
		```
		rm -rf /tmp/kafka-logs /tmp/zookeeper
		```










