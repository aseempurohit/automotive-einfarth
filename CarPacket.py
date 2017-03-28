import struct
from random import randint


class CarPacket(object):
    def __init__(self, value1, edge1, speed1, dist1, message_id1):
        self.analog = value1
        self.message_id = message_id1
        self.edge = edge1
        self.speed = speed1
        self.distance = dist1

    def asBytes(self):
        analog_bytes = struct.pack(">I", self.analog)
        speed_bytes = struct.pack(">I", self.speed)
        distance_bytes = struct.pack(">I", self.distance)
        message_bytes = struct.pack(">I", self.message_id)
        edge_byte = struct.pack(">B", self.edge)
        all_bytes = analog_bytes
        all_bytes += speed_bytes
        all_bytes += distance_bytes
        all_bytes += message_bytes
        all_bytes += edge_byte
        return all_bytes

    def toString(self):
      return "[CarPacket] value: {0}, message_id: {1}, edge: {2}, speed: {3}, distance: {4}".format(self.analog,
                                                                self.message_id,
                                                                self.edge,
                                                                self.speed,
                                                                self.distance)

    @staticmethod
    def fromBytes(value):
        value1 = struct.unpack(">I", value[0:4])[0]
        value2 = struct.unpack(">I", value[4:8])[0]
        value3 = struct.unpack(">I", value[8:12])[0]
        value4 = struct.unpack(">I", value[12:16])[0]
        value5 = bool(struct.unpack(">B", value[16:17])[0])
        return CarPacket(value1, value5, value2, value3, value4)


if __name__ == "__main__":
    v = 3001
    e = True
    s = randint(0, 100)
    d = randint(0, 100)
    m = randint(0, 100)
    p = CarPacket(v, e, s, d, m)
    print(p.toString())
    p1 = p.asBytes()
    p2 = CarPacket.fromBytes(p1)
    print(p2.toString())




