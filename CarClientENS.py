
import sys
import socket
from lib.SimpleClient import SimpleClient
from ens import ensclient


class CarClientENS(SimpleClient):
    def __init__(self, host2='localhost', port2=5000):
        super(CarClientENS, self).__init__(host2, port2)
        self.identifier = "mec.car-network-catcher"
        self.network = "micro-car-network.test-network"
        self.session = None
        
    def closestEndpoint(ensEndpoints):
        pass
        # TODO: find and return closest of ENSEndpoints
        
    
    def findEndpoints(self, cloudhost):
        c = ensclient.ENSClient(cloudhost, self.identifier)
        if c.init():
            self.session = c.connect(self.network)
            if self.session:
                self.setConnection(self.session.conn)
                self.endpoint = ensclient.ENSEndpoint(self.session.binding)
                print "host {0} port {1}".format(self.endpoint.host, self.endpoint.port)
            else:
                print "failed to connect to ar-network"
                
        else:
            print "failed to initialize"
            sys.exit(1)


    
        

if __name__ == "__main__":
    sc = CarClientENS()
    sc.findEndpoints("172.17.0.1")
    sc.subscribe()
