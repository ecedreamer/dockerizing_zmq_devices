import time
import zmq


def publisher():
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUB)
    try:
        zmq_socket.connect("tcp://forwarder:7779")
        zmq_socket.send("9 start#docker_publisher".encode())
        for num in range(message_count):
            zmq_socket.send(f"9 Count is {num}".encode())
        zmq_socket.send("9 end#docker_publisher".encode())
    except Exception as e:
        print(f"Exception at Publisher: {e}")


if __name__ == "__main__":
    print("Starting Publisher")
    message_count = 1000000
    t1 = time.time()
    publisher()
    t2 = time.time()
    print("\n-----------------------PUBLISHER------------------------------")
    print(f"Total message sent: {message_count}")
    print(f"Time taken: { t2 - t1}")
    print(f"MPS: {message_count/(t2 - t1)}")

