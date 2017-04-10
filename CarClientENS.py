
import sys
import socket
from lib.SimpleClient import SimpleClient
from CarClient import CarClient
from CarPacket import CarPacket
from CarPacket import WrongSizeException
from ens import ensclient


class CarClientENS(CarClient):
    def __init__(self, host2='localhost', port2=5000):
        super(CarClientENS, self).__init__(host2, port2)
        self.identifier = "mec.car-network-catcher"
        self.network = "micro-car-network.test-network"
        self.numberOfBytesToRead = CarPacket.size()
        self.session = None
        self.my_ens_client = None
        
        
    def decodeValue(self, value):
        print("decode value: {0}".format(value))
        try:
            if type(value) == bytes:
                return CarPacket.fromBytes(value)
        except WrongSizeException: 
                return CarPacket.fromSimpleString(value.decode('utf-8'))
        return None

    def useValue(self, value):
        print(value.toString())
        
    def findEndpoints(self):
        self.my_ens_client = ensclient.ENSClient(self.identifier)
        if self.my_ens_client.init():
            self.session = self.my_ens_client.connect(self.network)
            if self.session:
                self.setConnection(self.session.conn)
                self.endpoint = ensclient.ENSEndpoint(self.session.binding["endpoint"])
                print("host {0} port {1}".format(self.endpoint.host, self.endpoint.port))
            else:
                print("failed to connect to car-network")

        else:
            print("failed to initialize")
            sys.exit(1)

    def close(self):
        if self.my_ens_client is not None:
            self.my_ens_client.close()


if __name__ == "__main__":
    sc = CarClientENS()
    sc.findEndpoints()
    sc.subscribe()
