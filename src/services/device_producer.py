import time
import zmq
from lib.logger import logger
from lib.config import get_config


def producer():
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    try:
        zmq_socket.connect("tcp://streamer:8889")
        zmq_socket.send_json({"cmd": "#start#", "producer": "docker_producer"})
        for num in range(message_count):
            data = { 'cmd' : "", "msg": f"Count is {num}" }
            zmq_socket.send_json(data)
        zmq_socket.send_json({"cmd": "#end#", "producer": "docker_producer"})
    except Exception as e:
        logger.info(f"Exception at Producer: {e}")


if __name__ == "__main__":
    logger.info("Starting Producer")
    config = get_config()
    message_count = config.get("message_count")
    t1 = time.time()
    producer()
    t2 = time.time()
    logger.info("\n-----------------------PRODUCER------------------------------")
    logger.info(f"Total message sent: {message_count}")
    logger.info(f"Time taken: { t2 - t1}")
    logger.info(f"MPS: {message_count/(t2 - t1)}")

