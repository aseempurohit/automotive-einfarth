
import socket

from lib.SimpleServer import SimpleServer

class CarServer(SimpleServer):
    def __init__(self,port1=50024):
        super(CarServer, self).__init__(port1=port1)
        
        

if __name__ == "__main__":
    print("starting server")
    s = CarServer()
    s.serve()
