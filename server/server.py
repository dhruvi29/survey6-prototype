import grpc
from concurrent import futures
import time
import ip6_pb2_grpc as pb2_grpc
import ip6_pb2 as pb2

class PacketService(pb2_grpc.PacketServicer):

    def __init__(self, *args, **kwargs):
        self.count = 0

    def sendPacket(self, request, context):

        print("client contacted", self.count)
        self.count += 1

        result = {'result': request.a * request.b}

        return pb2.PacketRecieved(**result)

class HeartService(pb2_grpc.HeartServicer):
    def __init__(self,*args,**kwargs):
        pass

    def sendHeartBeat(self,request,context):
        print("Pulse recieved")
        result = {'a': 1}
        return pb2.Vein(**result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_PacketServicer_to_server(PacketService(), server)
    pb2_grpc.add_HeartServicer_to_server(HeartService(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()