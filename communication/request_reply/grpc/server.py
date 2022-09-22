from concurrent import futures

import grpc
import executor_pb2_grpc


class Calculator:
    def tambah(self,a=0,b=0):
        return a+b
    def kurang(self,a=0,b=0):
        return a-b
    def kali(self,a=0,b=0):
        return a*b
    def bagi(self,a=0,b=1):
        if (b==0):
            return 0
        return a/b



class ExecutorServer(executor_pb2_grpc.ExecutorServicer):

    def GetServerResponse(self, request_iterator, context):
        for message in request_iterator:
            yield message


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    executor_pb2_grpc.add_ExecutorServicer_to_server(ExecutorServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()