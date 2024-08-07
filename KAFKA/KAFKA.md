# Install Java

```
sudo apt install default-jre

```

# Start Zookeeper

Change directory to location where kafka is extracted
```
cd /opt/confluent/kafka/confluent-7.7.0/bin
```
Start Zookeeper using below command
```
./zookeeper-server-start ../etc/kafka/zookeeper.properties
```
Zookeeper Port `2181`
```
[2024-08-07 15:33:04,811] INFO binding to port 0.0.0.0/0.0.0.0:2181 (org.apache.zookeeper.server.NIOServerCnxnFactory)
```
# Start Kafka Broker/Kafka Server

Change directory to location where kafka is extracted
```
cd /opt/confluent/kafka/confluent-7.7.0/bin
```
Start Kafka Server/Broker using below command
```
./kafka-server-start ../etc/kafka/server.properties
```

# Create Kafka Topic

From /opt/confluent/kafka/confluent-7.7.0/bin$  run the below command
```
./kafka-topics --create --topic testtopic --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092
```

# Send Message Using Producer

2 ways to sent message from Producer

1. From Command Line

```
./kafka-console-producer --topic testtopic --broker-list localhost:9092
>hello 3
>^
```

2. From File
```
./kafka-console-producer --topic testtopic --broker-list localhost:9092 < ..\data\file.json

```
# Receive Message Using Consumer

```
/kafka-console-consumer --topic testtopic --bootstrap-server localhost:9092 --from-beginning
```
