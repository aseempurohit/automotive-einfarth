
import sys
import os
import optparse
import logging

from lib.SimpleServer import SimpleServer
from lib.BroadcastRecipient import BroadcastRecipient
from CarPacket import CarPacket
from CarRecipient import CarRecipient


logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)-15s %(levelname)-8s %(filename)-16s %(lineno)4d %(message)s')

class CarServerENS(SimpleServer):
    def __init__(self, port2=5002):
        super(CarServerENS, self).__init__(port1=port2)
        self.port = port2

        redis_host = os.getenv('REDIS_SERVICE_HOST')

        if not redis_host:
            logging.error("REDIS_SERVICE_HOST not set")
            sys.exit(1)

        redis_port = 6397
        try:
            redis_port = int(os.getenv('REDIS_SERVICE_PORT'))
        except TypeError:
            logging.error("REDIS_SERVICE_PORT not available")

        if redis_host is None:
            print "REDIS_SERVICE_HOST not available"
            sys.exit(1)

        if os.getenv("USE_REDIS"):
            if os.getenv("USE_REDIS").find("TRUE") > -1:
                self.initRedis(redis_host, 'car_value', redis_port)
                logging.info("attempting to use redis with host %s and port %d watching value %s",redis_host,redis_port,'ar_value')
            else:
                logging.error("not using redis, USE_REDIS != TRUE")
        else:
            logging.error("not using redis - USE_REDIS not set")

    def fromBytesToString(self, value):
        if type(value) == bytes:
            a = CarPacket.fromBytes(value)
            s1 = a.simpleString()
            return s1
        if type(value) == str:
            return value

    def addClient(self, connection, address1):
        if self.listener is None:
            self.clients.append(CarRecipient(connection, address1))
        if self.listener is not None:
            self.listener.addClient(CarRecipient(connection, address1))


if __name__ == "__main__":
    print "starting server"
    parser = optparse.OptionParser(
            formatter=optparse.TitledHelpFormatter(),
            usage=globals()['__doc__'],
            version='$Id: py.tpl 332 2008-10-21 22:24:52Z root $')

    parser.add_option ('-v', '--verbose', action='store_true',default=False, help='verbose output')
    (options, args) = parser.parse_args()
    port = 5000
    if(len(args) > 0):
        port = int(args[0])
    server = CarServerENS(port)
    server.serve()
