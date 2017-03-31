
import socket
from time import time, sleep
import sys
import logging
try:
    import serial
except ImportError:
    print("serial library not imported")

logging.basicConfig(level=logging.INFO,
                        format='%(asctime)-15s %(levelname)-8s %(filename)-16s %(lineno)4d %(message)s')
sys.path.append('./')
sys.path.append('lib')
sys.path.append('lib/lib')

from SimpleClient import SimpleClient
from CarPacket import CarPacket

serialPort = "/dev/ttyUSB0"

class CarClient(SimpleClient):
    def __init__(self, host2='localhost', port2=5002):
        super(CarClient, self).__init__(host2, port2)
        self.carsReady = False
        self.ser = None
        try:
            self.ser = serial.Serial(serialPort, 9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=None)
        except NameError:
            logging.error("serial not available")
        self.dist = 200

    def decodeValue(self, value):
        return CarPacket.fromBytes(value)

    def useValue(self, message):
        logging.debug(message.toString())
        try:
            if(self.carsReady):
                msg = '+' + str(int(message.analog * 255 / 1000)) + '/' + str(self.dist)
                if message.edge:
                    msg += '&'
                logging.info('cars ready!', msg)
            else:
                msg = '+0/'+str(self.dist)

            if self.ser is not None:
                self.ser.write(msg.encode('utf-8'))

        except:
            raise
            logging.error("error")

if __name__ == "__main__":
    #sc = CarClient(host2=socket.gethostname(),port2=5002)
    # sc = CarClient(host2='fast.secret.equipment',port2=5002)
    sc = CarClient(host2='slow.secret.equipment', port2=5002)
    sc.subscribe()
