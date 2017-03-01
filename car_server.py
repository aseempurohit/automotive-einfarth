
import socket


class Client:
    def __init__(self, socket1=None):
        self.clientsocket = socket1

    def publish(self, instruction):
        self.socket1.send(instruction)


if __name__ == "__main__":
    print("starting server")
    s = socket.socket()
    host = socket.gethostname()
    port = 50041
    s.bind((host, port))
    clients = list()
    try:
        while True:
            s.listen(5)
            c, addr = s.accept()
            print("got connection from ", addr)
            identifier = c.recv(10)
            print("identifier: ", identifier)
            if(identifier.find('P') > -1):
                instruction = None
                if(len(identifier) > 1):
                    instruction = identifier.replace('P', '')
                else:
                    instruction = c.recv(10)
                print('publisher - ', instruction)
                for client in clients:
                    client.clientsocket.send(instruction)

            if(identifier.find('C') > -1):
                print("appended client", addr)
                clients.append(Client(c))

    except KeyboardInterrupt:
        for client in clients:
            client.clientsocket.close()
        print("exiting")
        s.close()
