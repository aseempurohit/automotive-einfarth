
import socket
from lib.SimpleClient import SimpleClient


class CarClient(SimpleClient):
    def __init__(self,host2='localhost', port2=50024):
        super(CarClient, self).__init__(host2, port2)

if __name__ == "__main__":
    sc = CarClient(host2=socket.gethostname())
    sc.subscribe()
