
import socket
import sys
sys.path.append('lib')
sys.path.append('lib/lib')
from SimpleBroadcast import SimpleBroadcast
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
    # sb = CarBroadcast(host2='slow.secret.equipment')
    start_time = time()
    for a in range(0,20): 
        v1 = abs(randint(0,3000))
        v2 = abs(randint(0,100))
        v3 = abs(randint(0,100))
        print(v2)
        sb.broadcast(CarPacket(v1,True,v2, v3, a))

    print("total time {0}".format(time()-start_time))
