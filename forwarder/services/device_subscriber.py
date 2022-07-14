import zmq
import random


def show_count(time_interval=1):
    pass

def subscriber():
    global msg_count
    subscriber_id = random.randrange(1,10005)
    print(f"I am subscriber # {subscriber_id}")
    context = zmq.Context()
    # recieve work
    subscriber_receiver = context.socket(zmq.SUB)
    try:
        subscriber_receiver.setsockopt(zmq.SUBSCRIBE, b"9")
        subscriber_receiver.connect("tcp://forwarder:7790")
        count = 0
        while True:
            count += 1
            data = subscriber_receiver.recv().decode()
            data_list = data.split("#")
            if "start" in data_list[0]:
                print(f"\nStarting receiving data from {data_list[-1]}") 
            if "end" in data_list[0]:
                print(f"\nReceived all successfully from {data_list[-1]}, count: {count}") 
            

    except Exception as e:
        print(f"Exception at Subscriber: {e}")


if __name__ == "__main__":
    subscriber()