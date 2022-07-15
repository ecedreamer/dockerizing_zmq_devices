# Dockerizing ZMQ Devices #
In this repository, we will dockerize 2 ZMQ Devices namely Forwarder and Streamer.
For more detail information about Forwarder Device and Streamer Device, visit the link below. 

https://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/devices/forwarder.html

https://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/devices/streamer.html

## Dockerizing STREAMER ##

To dockerize streamer device, I have created a Dockerfile and docker-compose which is inside the streamer folder. There are 3 services known as streamer, producer and consumer in this setup. All services depend upon the configuration file which is on the host machine and is mounted to all the container services.


STREAMER: Streamer device binds two ports in the PUSH PULL configuration. The Frontend or Source port is PULL socket and Backend or Sink port is PUSH socket.

PRODUCER: Sources or Producers PUSH the events to the Source port of streamer device. 

CONSUMER: Sinks or Consumers(Workers) PULL the events from the sink port and process them further according to the functional requirements.  


### To make extremely fast streamer device, I have chosen pypy:3.9 as an image. To run these containers, go to the streamer folder in the terminal and type following command. 
``` 
$ docker compose up
```
### OUTPUT ###
```
[+] Running 3/0
 ⠿ Container streamer-streamer-1  Created                                                               0.0s
 ⠿ Container streamer-producer-1  Created                                                               0.0s
 ⠿ Container streamer-consumer-1  Created                                                               0.0s
Attaching to streamer-consumer-1, streamer-producer-1, streamer-streamer-1
streamer-streamer-1  | STREAMER: Running streamer device
streamer-consumer-1  | CONSUMER: Starting consumer service(ID: 4439)
streamer-producer-1  | PRODUCER: Starting Producer
streamer-consumer-1  | 
streamer-consumer-1  | CONSUMER: Starting receiving data from docker_producer
streamer-producer-1  | 
streamer-producer-1  | -----------------------PRODUCER------------------------------
streamer-producer-1  | Total message sent: 1000000
streamer-producer-1  | Time taken: 4.597674608230591
streamer-producer-1  | MPS: 217501.25557163966
streamer-producer-1  | 
streamer-producer-1  | -----------------------PRODUCER END------------------------------
streamer-consumer-1  | 
streamer-consumer-1  | CONSUMER: Received all successfully from docker_producer | count: 1000000
streamer-consumer-1  | 
streamer-producer-1  | 
streamer-producer-1  |  PRODUCER: Sleeping for 10 seconds
```
You can see that currently events are streaming in 217501 MPS which is around 5 times faster than the normal Python image. 
 ### 

### SIGNAL ###
Signal handler is also implemented in this project. You can send the SIGHUP signal from the host machine to our docker container.

 This provision is made for the producer service to make it capable of responding to the configuration change in run time if changed by configuration management tools. That is configuration management tools changes the config file and sents SIGHUP signal to the producer service for the same so that producer can use new config file. 

```
$ docker compose kill -s SIGHUP producer

                    OR

$ docker kill --signal="SIGHUP" streamer-producer
```
To show the implementation of sending signal from one container to another, the consumer service is coded in such a way that it can also handle SIGHUP signal. When producer get SIGHUP signal from the HOST machine, it updates its configuration and sends SIGHUP signal to consumer service. 

You can verify it from the logs appeared after executing the above SIGHUP sending command. 
