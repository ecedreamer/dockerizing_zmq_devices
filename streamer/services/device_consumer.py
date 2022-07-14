import zmq
import random
import signal


def subscriber():
    global msg_count
    subscriber_id = random.randrange(1, 10005)
    print(f"CONSUMER: Starting consumer service(ID: {subscriber_id})")
    context = zmq.Context()
    subscriber_receiver = context.socket(zmq.PULL)
    try:
        subscriber_receiver.connect("tcp://streamer:8890")
        count = 0
        while True:
            count += 1
            data = subscriber_receiver.recv_json()
            if data['cmd'] == "#start#":
                print(
                    f"\nCONSUMER: Starting receiving data from {data['producer']}")
            if data['cmd'] == "#end#":
                print(
                    f"\nCONSUMER: Received all successfully from {data['producer']} | count: {count-2}\n")
                count = 0

    except Exception as e:
        print(f"Exception at subscriber: {e}")


def sighup_handler(signum, frame):
    print('CONSUMER: Sighup Signal received at consumer...............................')


if __name__ == "__main__":
    signal.signal(signal.SIGHUP, sighup_handler)
    subscriber()
