# Prerequisite : 

* Download and extract java to /opt/java directory
* Add this line `export JAVA_HOME=/opt/java/jdk17` to `~\.profile` file

# Extras : Connect to VM from Local Machine

* Setup Port Forwarding for NAT
** Protocol:TCP, HostIP:< IP Address of Local Machine >, Host Port: < Any Number >, Guest IP: < IP Address of VM >, Guest IP:< Open SSL Port from VM >
* Create a batch file in windows and add the command `start ssh <user_name>@<Ip Address of Local Machine> -p <Host Port mentioned above>` and save the file. This can be used to open the VM's Linux terminal from your local machine

# 1 . Download Kafka

* from https://kafka.apache.org/downloads
* under Binary downloads: --> Scala 2.12  - kafka_2.12-3.8.0.tgz (asc, sha512)

# 2. Extract and place it under the /opt directory giving necessary permissions

# 3. Start the zookeeper server & kafka server

```
cd /opt/kafka/bin
./zookeeper-server-start.sh ../config/zookeeper.properties
```
open a different terminal and run kafka server

```
cd /opt/kafka/bin
./kafka-server-start.sh ../config/server.properties
```

# 4. Create kafka topic

```
cd /opt/kafka/bin
./kafka-topics.sh --bootstrap-server localhost:9092 --create --topic "topic1"
```
Note: you can obtain the port number from server.properties

# 5. Sent message to a topic
```
cd /opt/kafka/bin
./kafka-console-producer.sh --bootstrap-server localhost:9092 --topic "topic1"
```
use Ctrl+D to exit the command

# 6. Read message from a topic
```
cd /opt/kafka/bin
./kafka-console-consumer.sh  --bootstrap-server localhost:9092 --topic "topic1" --from-beginning
```

