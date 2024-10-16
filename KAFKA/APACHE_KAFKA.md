# Prerequisite : 

* Download and extract java to /opt/java directory
* Add this line `export JAVA_HOME=/opt/java/jdk17` to `~\.profile` file

# 1 . Download Kafka

* from https://kafka.apache.org/downloads
* under Binary downloads: --> Scala 2.12  - kafka_2.12-3.8.0.tgz (asc, sha512)

# 2. Extract and place it under the /opt directory giving necessary permissions

# 3. Run the zookeeper command

`
cd /opt/kafka/bin
./zookeeper-server-start.sh ../config/zookeeper.properties
`
