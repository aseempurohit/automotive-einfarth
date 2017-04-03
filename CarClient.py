
import socket
from time import time, sleep
import sys
import logging
try:
    import serial
except ImportError:
    print("serial library not imported")

logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)-15s %(levelname)-8s %(filename)-16s %(lineno)4d %(message)s')
sys.path.append('./')
sys.path.append('lib')
sys.path.append('lib/lib')

from SimpleClient import SimpleClient
from CarPacket import CarPacket

device_location = '/dev/xbee'

if len(sys.argv) > 1:
    device_location = sys.argv[1]
    logging.debug(device_location)

class CarClient(SimpleClient):
    def __init__(self, host2='localhost', port2=5002):
        super(CarClient, self).__init__(host2, port2)
        self.carsReady = False
        self.ser = None

        try:
            self.ser = serial.Serial(device_location, 9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=None)
        except NameError:
            logging.error("serial not available")

        self.dist = 200

    def decodeValue(self, value):
        return CarPacket.fromBytes(value)

    def useValue(self, message):
        # logging.debug(message.toString())
        try:
            if(self.carsReady):
                targetLaptime = str(int((1000 - message.analog) * 1.7 + 1700))
                msg = '+' + targetLaptime + '/' + str(self.dist)
                if message.edge:
                    msg += '&'
            else:
                msg = '+3700/'

            logging.debug(msg)
            msg += '\n'

            if self.ser is not None:
                self.ser.write(msg.encode('utf-8'))

        except:
            logging.error("error handling received packet or writing serial")

if __name__ == "__main__":
    sc = CarClient(host2=socket.gethostname(),port2=5002)
    # sc = CarClient(host2='fast.secret.equipment',port2=5002)
    # sc = CarClient(host2='slow.secret.equipment', port2=5002)
    sc.subscribe()
