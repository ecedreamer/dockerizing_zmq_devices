import time
import zmq

def producer():
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    try:
        zmq_socket.connect("tcp://localhost:5555")
        # Start your result manager and workers before you start your producers
        zmq_socket.send_json({"cmd": "#start#", "producer": "external"})
        for num in range(message_count):
            data = { 'cmd' : "", "msg": f"Count is {num}" }
            zmq_socket.send_json(data)
        zmq_socket.send_json({"cmd": "#end#", "producer": "external"})

    except Exception as e:
        print(f"Exception at Producer: {e}")


if __name__ == "__main__":
    message_count = 1000000
    t1 = time.time()
    producer()
    t2 = time.time()
    print("\n-----------------------PRODUCER------------------------------")
    print(f"Total message sent: {message_count}")
    print(f"Time taken: { t2 - t1}")
    print(f"MPS: {message_count/(t2 - t1)}")


