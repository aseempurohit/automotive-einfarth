
import socket
from lib.SimpleBroadcast import SimpleBroadcast
from CarBroadcast import CarBroadcast
from ens import ensclient


class CarBroadcastENS(CarBroadcast):
    def __init__(self, host2='localhost', port2=5000):
        super(CarBroadcastENS, self).__init__(host1=host2, port1=port2)
        self.identifier = "mec.maintenance-car-pitcher"
        self.network = "micro-car-network.test-network"
        self.session = None
        
    def closestEndpoint(ensEndpoints):
        pass
        # TODO: find and return closest of ENSEndpoints
        
    
    def findEndpoints(self, cloudhost):
        c = ensclient.ENSClient(cloudhost,self.identifier)
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
    sb = CarBroadcastENS()
    sb.findEndpoints("172.17.0.1")
    sb.broadcast('10')
    
