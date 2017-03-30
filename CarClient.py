
import socket
from time import time, sleep
import sys
import serial
sys.path.append('/home/frogsf/Documents/car-base/lib')
sys.path.append('/home/frogsf/Documents/car-base')
sys.path.append('/home/frogsf/Documents/car-base/lib/lib')
from SimpleClient import SimpleClient
from CarPacket import CarPacket

serialPort = "/dev/ttyUSB0"

class CarClient(SimpleClient):
    def __init__(self,host2='localhost', port2=5002):
        super(CarClient, self).__init__(host2, port2)
        self.carsReady = False
        self.ser = serial.Serial(serialPort, 9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=None)
        self.dist = 200

    def decodeValue(self, value):
        return CarPacket.fromBytes(value)

    def useValue(self, message):
        try: 
            # msg = '{h} Edge On: {e}'.format(h=self.host, e=message.edge)
            print(self.host, message.toString())
            if(self.carsReady):
                msg = '+' + message.analog + '/' + self.dist
                if message.edge:
                    msg += '&'
            else:
                msg = '+0/'+self.dist

            self.ser.write(msg.encode('utf-8'))

            # print(msg)
            # temp = message.decode().split('/')
            # if(len(temp) == 5):
            #     try:
            #         self.speed = int((float(temp[0]) / 1920.0) * 80) + 120
            #         self.edge = int(temp[1])
            #         # print('{s},{e}'.format(s=self.speed,e=temp[1]))
            #         message = "+set/" + str(self.speed)
            #         if self.edge:
            #             message += "&"
            #         message += str(temp[3])
            #         message += "\r\n"
            #         self.serialToWrite = message.encode('utf-8') 
            #         # c = int((float(temp[0]) / 1920.0) * 100) - 50
            #         # print(c)
            #         # self.ser.write('+calibrate/30707' + str(c) + '\r\n')
            #         self.ser.write(b'+start/\r\n')
            #         print(message)
            #         sleep(.1)
            #     except:
            #         raise
            #         print("Packet lost")
        except:
            raise
            print("error")

if __name__ == "__main__":
    # sc = CarClient(host2=socket.gethostname(),port2=5002)
    # sc = CarClient(host2='fast.secret.equipment',port2=5002)
    sc = CarClient(host2='slow.secret.equipment',port2=5002)
    sc.subscribe()
