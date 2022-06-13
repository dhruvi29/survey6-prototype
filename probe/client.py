import scapy.all as scapy
import grpc
from concurrent import futures
import time
import sys
sys.path.append('../server')
import ip6_pb2_grpc as pb2_grpc
import ip6_pb2 as pb2
import threading
import time


# with grpc.insecure_channel('localhost:50051') as channel:
#     stub = pb2_grpc.HeartStub(channel)
#     response = stub.sendHeartBeat(pb2.Artery(a=1))
#     print(response.a)
execute = True

def CapturePackets():
    capture = scapy.sniff(filter="ip6", count=5)
    print(capture.summary())

def SendPackets():
    print("hey")

def HeartBeats():
    global execute
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pb2_grpc.HeartStub(channel)
        while(execute):
            response = stub.sendHeartBeat(pb2.Artery(a=1))
            time.sleep(2)
            print(response.a)

if __name__ == "__main__":
    capkts = threading.Thread(target=CapturePackets)
    sendpkts = threading.Thread(target=SendPackets)
    heart = threading.Thread(target=HeartBeats)
  
    capkts.start()
    sendpkts.start()
    heart.start()
  
    capkts.join()
    sendpkts.join()
    heart.join()
  

