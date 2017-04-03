
import socket
from time import time, sleep
import sys
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
        self.ser = None
        self.theta = 2

        self.screen_client = udp_client.UDPClient('127.0.0.1', 7002)

        try:
            self.ser = serial.Serial(device_location, 9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=None)
        except NameError:
            logging.error("serial not available")

        logging.info("initialized")

    def decodeValue(self, value):
        logging.info(value)
        try:
            if type(value) == bytes:
                return CarPacket.fromBytes(value)
        except WrongSizeException:
                return CarPacket.fromSimpleString(value.decode('utf-8'))
        return None

    def fromBytesToString(self, value):
        logging.debug(" bytes to string invoked {0}".format(value))
        a = CarPacket.fromBytes(value)
        s1 = a.simpleString()
        return s1

    def useValue(self, message):
        # logging.debug(message.toString())
        try:
            dist = int(calcActualSpeed(message.analog) * self.theta * 2 / 1000)


            if(self.carsReady):
                msg = '+' + str(int(message.analog * 255 / 1000)) + '/' + str(dist)
                if message.edge:
                    msg += '&'
                logging.debug('cars ready, sending')
                self.screen_client.send(buildMessage('/cardata', message.speed, message.distance, message.edge))
            else:
                msg = '+0/'
                logging.debug('all cars not ready')
                paused = osc_message_builder.OscMessageBuilder(address='/paused')
                self.screen_client.send(paused.build())

            logging.info(msg)
            msg += '\r\n'

            if self.ser is not None:
                self.ser.write(msg.encode('utf-8'))

        except:
            logging.error("error handling received packet or writing serial")

def buildMessage(address1, speed, dist, edge):
    builder = osc_message_builder.OscMessageBuilder(address=address1)
    builder.add_arg(speed, builder.ARG_TYPE_INT)
    builder.add_arg(dist, builder.ARG_TYPE_INT)
    if edge:
        builder.add_arg(tf, builder.ARG_TYPE_TRUE)
    else:
        builder.add_arg(tf, builder.ARG_TYPE_FALSE)

    return builder.build()

if __name__ == "__main__":
    sc = CarClient(host2='frogsf-dt3',port2=4999)
    # sc = CarClient(host2='fast.secret.equipment',port2=5002)
    #sc = CarClient(host2='slow.secret.equipment', port2=5002)
    sc.subscribe()
