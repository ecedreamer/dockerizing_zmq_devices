# Dockerizing ZMQ Devices #
In this repository, we will dockerize 3 ZMQ Devices namely Queue, Forwarder and Streamer.

## Dockerizing STREAMER ##


## SIGNAL ##

$ docker compose kill -s SIGHUP producer

$ docker kill --signal="SIGHUP" streamer-producer
