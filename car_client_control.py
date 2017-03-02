
import socket
from lib.SimpleBroadcast import SimpleBroadcast

class CarBroadcast(SimpleBroadcast):
    def __init__(self,host2='localhost', port2=50024):
        super(CarBroadcast, self).__init__(host1=host2, port1=port2)
        

if __name__ == "__main__":
    sb = CarBroadcast(host2=socket.gethostname())
    sb.broadcast('10')