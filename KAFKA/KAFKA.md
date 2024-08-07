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
