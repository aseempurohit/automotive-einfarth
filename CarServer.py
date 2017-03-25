
import socket

from lib.SimpleServer import SimpleServer
from lib.BroadcastRecipient import BroadcastRecipient


class CarRecipient(BroadcastRecipient):
    def __init__(self, socket2=None, address2=None):
        super(BroadcastRecipient, self).__init__(socket1=socket2, address1=address2)

    def publish(self, instruction):
        try:
            # cast instruction to a number
            # do math here
            # turn it back into a string
            # make it bytes before you send it
            # with variable.encode()
            self.s.send(instruction)
        except socket.error:
            print("car client became disconnected")


class CarServer(SimpleServer):
    def __init__(self,port1=50024):
        super(CarServer, self).__init__(port1=port1)

    def addClient(self, connection, address1):
        if self.listener is None:
            self.clients.append(CarRecipient(connection, address1))
        if self.listener is not None:
            self.listener.addClient(CarRecipient(connection, address1))


if __name__ == "__main__":
    print("starting server")
    s = CarServer()
    s.serve()
