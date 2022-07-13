import sys
import zmq
import random
from lib.logger import logger
from lib.config import get_config
import time
import threading


def show_count(time_interval=1):
    pass

def consumer():
    global msg_count
    consumer_id = random.randrange(1,10005)
    logger.info(f"I am consumer # {consumer_id}")
    context = zmq.Context()
    # recieve work
    consumer_receiver = context.socket(zmq.PULL)
    try:
        consumer_receiver.connect("tcp://streamer:8890")
        while True:
            work = consumer_receiver.recv_json()
            data = work['num']
            result = { 'consumer' : consumer_id, 'num' : data}
            msg_count += 1
            if msg_count == config.get("message_count"):
                logger.info(f"All {msg_count} messages received")
                sys.exit(0)

    except Exception as e:
        logger.info(f"Exception at Consumer: {e}")


if __name__ == "__main__":
    config = get_config()
    msg_count = 0
    consumer()