
import socket

if __name__ == "__main__":
    s = socket.socket()
    host = socket.gethostname()
    port = 50041
    s.connect((host, port))
    s.send('P')
    s.send('1')
    s.close
