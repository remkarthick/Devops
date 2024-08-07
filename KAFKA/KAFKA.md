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

# Start Kafka
