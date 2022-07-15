import zmq


def main():
    try:
        context = zmq.Context(1)
        # Socket facing publishers
        publisher = context.socket(zmq.SUB)
        publisher.bind("tcp://*:7779")
        publisher.setsockopt_string(zmq.SUBSCRIBE, "")
        # Socket facing subscribers
        subscriber = context.socket(zmq.PUB)
        subscriber.bind("tcp://*:7790")

        zmq.device(zmq.FORWARDER, publisher, subscriber)
    except Exception as e:
        print(e)
        print("bringing down zmq device")
    finally:
        publisher.close()
        subscriber.close()
        context.term()


if __name__ == "__main__":
    print("Running forwarder device")
    main()