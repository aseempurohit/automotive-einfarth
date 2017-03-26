
import os 
import socket

from lib.SimpleServer import SimpleServer
from lib.BroadcastRecipient import BroadcastRecipient

from carcalc import getCarSpeed, getMinDist

class CarRecipient(BroadcastRecipient):
    def __init__(self, socket2, address2):
        self.s = socket2
        self.address = address2

    def publish(self, instruction):
        try:
            temp = instruction.split('/')
            if(len(temp) == 2):
                try:
                    mouse = temp[0]
                    kph = getCarSpeed(mouse) 
                    dist = getMinDist(mouse) 
                    edge = temp[1]
                    instruction = mouse + "/" + edge + "/" + kph + "/" + dist
                    self.s.send(instruction.encode('utf-8'))
                except:
                    print "Error decoding and sending instruction"

        except socket.error:
            print("car client became disconnected")
        except:
            print instruction


class CarServer(SimpleServer):
    def __init__(self, port2=5002):
        super(CarServer, self).__init__(port1=port2)
        if os.getenv("USE_REDIS"):
            if os.getenv("USE_REDIS").find("TRUE") > -1:
                self.initRedis('localhost', 'car_value')

    def addClient(self, connection, address1):
        if self.listener is None:
            self.clients.append(CarRecipient(connection, address1))
        if self.listener is not None:
            self.listener.addClient(CarRecipient(connection, address1))


if __name__ == "__main__":
    print("starting server")
    print(socket.gethostname())
    server = CarServer()
    print server.port
    server.serve()
