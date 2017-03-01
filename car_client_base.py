
import socket

if __name__ == "__main__":
    s = socket.socket()
    host = socket.gethostname()
    port = 50041
    s.connect((host, port))
    s.send('C')
    while True:
        print(s.recv(10))
    s.close
