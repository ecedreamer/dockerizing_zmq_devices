# Dockerizing ZMQ Devices #
In this repository, we will dockerize 2 ZMQ Devices namely Forwarder and Streamer.

## Dockerizing STREAMER ##


## SIGNAL ##

$ docker compose kill -s SIGHUP producer

$ docker kill --signal="SIGHUP" streamer-producer
