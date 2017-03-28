
import socket
from lib.SimpleBroadcast import SimpleBroadcast
from CarPacket import CarPacket

class CarBroadcast(SimpleBroadcast):
    def __init__(self,host2='localhost', port2=5002):
        super(CarBroadcast, self).__init__(host1=host2, port1=port2)
        
    def encodeValue(self, value):
        return value.asBytes()

from random import randint
from time import time
if __name__ == "__main__":
    sb = CarBroadcast(host2=socket.gethostname())
    #sb = CarBroadcast(host2='fast.secret.equipment')
    start_time = time()
    for a in range(0,20): 
        sb.broadcast(CarPacket(randint(0,3000),True,randint(0,100), randint(0,100), a))

    print("total time {0}".format(time()-start_time))
