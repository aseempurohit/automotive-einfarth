
import socket
from time import time
from lib.SimpleClient import SimpleClient
from CarPacket import CarPacket

class CarClient(SimpleClient):
    def __init__(self,host2='localhost', port2=5002):
        super(CarClient, self).__init__(host2, port2)

    def decodeValue(self, value):
        return CarPacket.fromBytes(value)

    def useValue(self, value):
        print(value.toString())

if __name__ == "__main__":
    sc = CarClient(host2=socket.gethostname(),port2=5002)
    #sc = CarClient(host2='fast.secret.equipment',port2=5002)
    sc.subscribe()
