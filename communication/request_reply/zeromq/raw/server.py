import zmq, sys

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.REP)
sock.bind("tcp://*:5678")

# Run a simple "Echo" server
while True:
    message = sock.recv()
    print(message)
    sock.send(message)
