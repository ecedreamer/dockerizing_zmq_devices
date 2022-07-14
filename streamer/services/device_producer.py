import time
import zmq
import signal

from docker import DockerClient
from lib.config import get_config


def producer():
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    try:
        zmq_socket.connect("tcp://streamer:8889")
        zmq_socket.send_json({"cmd": "#start#", "producer": "docker_producer"})
        for num in range(config.get('message_count')):
            data = {'cmd': "", "msg": f"Count is {num}"}
            zmq_socket.send_json(data)
        zmq_socket.send_json({"cmd": "#end#", "producer": "docker_producer"})
    except Exception as e:
        print(f"Exception at Producer: {e}")


def display_stat(t1, t2):
    print("\n-----------------------PRODUCER------------------------------")
    print(f"Total message sent: {config.get('message_count')}")
    print(f"Time taken: { t2 - t1}")
    print(f"MPS: {config.get('message_count')/(t2 - t1)}")
    print("\n-----------------------PRODUCER END------------------------------")
    sleep_time = config.get("producer_sleep_time")
    time.sleep(2)
    print(f"\n PRODUCER: Sleeping for {sleep_time} seconds\n")
    time.sleep(sleep_time)



def sighup_handler(signum, frame):
    print('PRODUCER: Sighup Signal received, so reloading the configuration.')
    global config
    config = get_config()

    # sending signal to consumer
    client = DockerClient(base_url='unix:///tmp/docker.sock')
    container = client.containers.get('streamer-consumer-1')
    container.exec_run(['kill', '-1', '1'])


def main():
    signal.signal(signal.SIGHUP, sighup_handler)
    while True:
        t1 = time.time()
        producer()
        t2 = time.time()
        display_stat(t1, t2)


if __name__ == "__main__":
    print("PRODUCER: Starting Producer")
    config = get_config()
    main()
