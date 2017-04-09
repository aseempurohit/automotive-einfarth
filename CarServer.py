
import os
import socket
import sys
sys.path.append('lib')
sys.path.append('lib/lib')

from lib.SimpleServer import SimpleServer
from lib.BroadcastRecipient import BroadcastRecipient
from CarPacket import CarPacket
from CarPacket import WrongSizeException 
from CarRecipient import CarRecipient

from time import sleep

class CarServer(SimpleServer):
    def __init__(self, port2=5002):
        super(CarServer, self).__init__(port1=port2)
        self.port = port2
        self.packetSize = CarPacket.size()
        if os.getenv("USE_REDIS"):
            if os.getenv("USE_REDIS").find("TRUE") > -1:
                self.initRedis('localhost', 'car_value')
    
    def fromBytesToString(self, value):
        if type(value) == bytes:
            a = CarPacket.fromBytes(value)
            s1 = a.simpleString()
            return s1
        if type(value) == str:
            return value
    
    
    def addClient(self, connection, address1):
        if self.listener is None:
            self.clients.append(CarRecipient(connection, address1))
        if self.listener is not None:
            self.listener.addClient(CarRecipient(connection, address1))


if __name__ == "__main__":
    print("starting server")
    print(socket.gethostname())
    server = CarServer()
    #server.initRedis('127.0.0.1', 'car_value') 
    server.serve()
      
