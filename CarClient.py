
import socket
from lib.SimpleClient import SimpleClient


class CarClient(SimpleClient):
    def __init__(self,host2='localhost', port2=5002):
        super(CarClient, self).__init__(host2, port2)

if __name__ == "__main__":
    sc = CarClient(host2='slow.secret.equipment',port2=5002)
    sc.subscribe()
