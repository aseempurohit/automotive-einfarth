
import socket
from time import time, sleep
import random
import sys
sys.path.append('lib')
sys.path.append('lib/lib')
import logging
from CarPacket import WrongSizeException
from carcalc import calcActualSpeed
from pythonosc import osc_message_builder
from pythonosc import udp_client
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
        self.calibrateCars = False
        self.ser = None
        self.theta = 2

        self.screen_client = udp_client.UDPClient('127.0.0.1', 7002)

        try:
            self.ser = serial.Serial(device_location, 9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=None)
        except NameError:
            logging.error("serial not available")

        logging.info("initialized")

    def decodeValue(self, value):
        # logging.info(value)
        try:
            if type(value) == bytes:
                return CarPacket.fromBytes(value)
        except WrongSizeException:
                return CarPacket.fromSimpleString(value.decode('utf-8'))
        except:
            return None
        return None

    def fromBytesToString(self, value):
        logging.debug(" bytes to string invoked {0}".format(value))
        a = CarPacket.fromBytes(value)
        s1 = a.simpleString()
        return s1

    def useValue(self, message):
        # logging.debug(message.toString())
        try:

            if(self.carsReady):
                targetLaptime = int((1000 - message.analog) * 1.5 + 1900)
                if targetLaptime > 3000:
                    msg = '+stop/'
                    self.screen_client.send(buildMessage('/cardata', 0, 0, message.edge))
                else:
                    if message.edge and self.theta is not 0.0:
                        self.theta = 1
                    elif self.theta is not 0.0:
                        self.theta = round(random.uniform(5,26), 2)
                    dist = int(message.analog / 1000 * self.theta * 2 + 4)
                    kph = int(message.analog * 310 / 1000)
                    msg = '+' + str(targetLaptime) + '/' + str(dist) + 'H'
                    if message.edge:
                        msg += '&'

                    self.screen_client.send(buildMessage('/cardata', kph, dist, message.edge))
                    logging.debug('screen osc {0} {1}'.format(kph, dist))

            else:
                msg = '+stop/'
                paused = osc_message_builder.OscMessageBuilder(address='/paused')
                self.screen_client.send(paused.build())

            logging.debug(msg)
            msg += '\n'

            if self.ser is not None:
                self.ser.write(msg.encode('utf-8'))

        except:
            raise
            logging.error("error handling received packet or writing serial")

def buildMessage(address1, speed, dist, edge):
    builder = osc_message_builder.OscMessageBuilder(address=address1)
    builder.add_arg(speed, builder.ARG_TYPE_INT)
    builder.add_arg(dist, builder.ARG_TYPE_INT)
    if edge:
        builder.add_arg(edge, builder.ARG_TYPE_TRUE)
    else:
        builder.add_arg(edge, builder.ARG_TYPE_FALSE)

    return builder.build()

if __name__ == "__main__":
    # sc = CarClient(host2='frogsf-dt3',port2=4999)
    sc = CarClient(host2='fast.secret.equipment',port2=5002)
    #sc = CarClient(host2='slow.secret.equipment', port2=5002)
    sc.subscribe()
