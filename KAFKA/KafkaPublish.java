package com.kk.kafkapublish;

import java.net.InetAddress;
import java.net.UnknownHostException;
import java.time.Duration;
import java.time.Instant;
import java.util.Properties;
import java.util.concurrent.Future;
import org.apache.kafka.clients.producer.Callback;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.Producer;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.clients.producer.RecordMetadata;

public class KafkaPublish {

    Properties props;
    Producer<String, String> producer;

    //Constructor
    public KafkaPublish(String serverNamePort) {
        props = new Properties();
        props.put("bootstrap.servers", serverNamePort);
        try {
            props.put("client.id", InetAddress.getLocalHost().getHostName());

        } catch (UnknownHostException err) {
            System.out.println(err);
        }
        props.put("acks", "1");//"0"=no wait for broker, "1"=ack by leader, "all"=ack by all insync replicas
        props.put("retries", 0);//0=no retries
        props.put("max.block.ms",5000);//timeout
        props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        producer = new KafkaProducer<>(props);
    }

    public String sendToKafka(String topic, String key,String value) {
        try {
            final ProducerRecord<String, String> pRecord = new ProducerRecord<>(topic, key,value);
            Instant startTime = Instant.now();
            //for(int i=500;i<1000;i++){

            Future<RecordMetadata> future = producer.send(pRecord, new Callback() {
                @Override
                public void onCompletion(RecordMetadata recordMetadata, Exception exception) {
                    if(exception==null){
                       System.out.println("Received new metadata. \n" +
                                "Topic:" + recordMetadata.topic() + "\n" +
                                "Partition: " + recordMetadata.partition() + "\n" +
                                "Offset: " + recordMetadata.offset() + "\n" +
                                "Timestamp: " + recordMetadata.timestamp());
                    }
                    else{
                         System.out.println("Send failed for record "+pRecord+ "Error : "+exception);
                        
                    }
                }
            });
           RecordMetadata recMetadata = future.get();

            //}
            Instant endTime = Instant.now();
            Duration elapsedTime = Duration.between(startTime, endTime);
            System.out.print("Elapsed Time : " + elapsedTime.toMillis() + "ms");//452ms - async just send, 6124ms - sync using get() after send
            producer.flush();
            producer.close();
            return "success";
        } catch (Exception err) {
            return err.toString();
        }
    }

    public static void main(String[] args) {
        KafkaPublish kp = new KafkaPublish("192.168.1.22:9092");
        String s = kp.sendToKafka("topic1", "kkk","hello ther boomer 12345");
        System.out.println("Status of send : " + s);
    }
}
