from __future__ import print_function

import grpc
import executor_pb2_grpc
import executor_pb2


def make_message(message):
    return executor_pb2.Message(
        message=message
    )


def generate_messages():
    messages = [
        make_message("First message"),
        make_message("Second message"),
        make_message("Third message"),
        make_message("Fourth message"),
        make_message("Fifth message"),
    ]
    for msg in messages:
        print("Hello Server Sending you the %s" % msg.message)
        yield msg


def send_message(stub):
    responses = stub.GetServerResponse(generate_messages())
    for response in responses:
        print("Hello from the server received your %s" % response.message)


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = executor_pb2_grpc.ExecutorStub(channel)
        send_message(stub)


if __name__ == '__main__':
    run()