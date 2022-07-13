import zmq
from lib.logger import logger


def main():
    try:
        context = zmq.Context(1)
        # Socket facing producers
        producer = context.socket(zmq.PULL)
        producer.bind("tcp://*:8889")
        # Socket facing consumers
        consumer = context.socket(zmq.PUSH)
        consumer.bind("tcp://*:8890")

        zmq.device(zmq.STREAMER, producer, consumer)
    except Exception as e:
        logger.error(e)
        logger.info("bringing down zmq device")
    finally:
        producer.close()
        consumer.close()
        context.term()


if __name__ == "__main__":
    logger.info("Running streamer device")
    main()
