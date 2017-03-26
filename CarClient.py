
import socket
from time import time
from lib.SimpleClient import SimpleClient


class CarClient(SimpleClient):
    def __init__(self,host2='localhost', port2=5002):
        super(CarClient, self).__init__(host2, port2)

    def subscribe(self, connection=None):
        if connection is None and self.conn is None:
            self.conn = socket.socket()
            self.conn.connect((self.host, self.port))
        elif self.conn is None:
            self.conn = connection
        self.conn.send(b'C')
        while True:
            value1 = self.conn.recv(16)
            self.lastMessageTimes.append(time())
            if(len(self.lastMessageTimes) > 16):
                if(time() - self.lastMessageTimes[0] < self.warningTime):
                    raise ClientDisconnectedException()
                self.lastMessageTimes.pop(0)

            self.useValue(value1)
        self.s.close

if __name__ == "__main__":
    sc = CarClient(host2=socket.gethostname(),port2=5002)
    sc.subscribe()
