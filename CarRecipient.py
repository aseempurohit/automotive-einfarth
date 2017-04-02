
import os
import socket
import sys
sys.path.append('lib')
sys.path.append('lib/lib')

from lib.BroadcastRecipient import BroadcastRecipient
from CarPacket import CarPacket
import logging

logging.basicConfig(level=logging.INFO,
                        format='%(asctime)-15s %(levelname)-8s %(filename)-16s %(lineno)4d %(message)s')

class CarRecipient(BroadcastRecipient):
    def __init__(self, socket2, address2):
        self.s = socket2
        self.address = address2
        self.connected = True

    def processBeforePublish(self, instruction):
        car_packet = CarPacket.fromBytes(instruction)
        car_packet.speed = int(calcSpeed(car_packet.analog))
        car_packet.dist = int(calcDist(car_packet.analog))
        logging.debug(car_packet)
        return car_packet.asBytes()

if __name__ == "__main__":
    cr = CarRecipient();
    cp = CarPacket(randint(0,1000),True,randint(0,100), randint(0,100), self.messageID)
    cr.processBeforePublish(cp)
