import zmq
import time

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.PUB)
sock.bind("tcp://*:5680")

id = 0

while True:
    time.sleep(1)
    id, now = id + 1, time.ctime()

    # Message [prefix][message]
    message = "1-Update! >> #{id} >> {time}".format(id=id, time=now)
    sock.send_string(message)

    # Message [prefix][message]
    message = "2-Update! >> #{id} >> {time}".format(id=id, time=now)
    sock.send_string(message)

    id += 1