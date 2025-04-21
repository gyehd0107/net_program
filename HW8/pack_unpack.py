
from socket import *
import struct, binascii

# UDP Header 클래스
class Udphdr:
    def __init__(self, source_port, destination_port, length, checksum):
        self.source_port = source_port
        self.destination_port = destination_port
        self.length = length
        self.checksum = checksum

    # UDP 헤더 패킹 (4개의 2바이트 필드 → 총 8바이트)
    def pack_Udphdr(self):
        return struct.pack('!4H', self.source_port, self.destination_port, self.length, self.checksum)

    # UDP 헤더 언패킹
    def unpack_Udphdr(self, buffer):
        return struct.unpack('!4H', buffer[:8])

    # 개별 필드 접근 함수
    def getSrcPort(self, unpacked):
        return unpacked[0]

    def getDstPort(self, unpacked):
        return unpacked[1]

    def getLength(self, unpacked):
        return unpacked[2]

    def getChecksum(self, unpacked):
        return unpacked[3]

# 실행 부분
if __name__ == '__main__':
    # 테스트 인스턴스 생성
    udp = Udphdr(5555, 80, 1000, 0xFFFF)

    # 패킹된 바이트 출력
    packed_udphdr = udp.pack_Udphdr()
    print(binascii.b2a_hex(packed_udphdr))  # b'15b3005003e8ffff'

    # 언패킹
    unpacked_udphdr = udp.unpack_Udphdr(packed_udphdr)
    print(unpacked_udphdr)  # (5555, 80, 1000, 65535)

    # 필드별 출력
    print(f'Source Port:{udp.getSrcPort(unpacked_udphdr)} '
          f'Destination Port:{udp.getDstPort(unpacked_udphdr)} '
          f'Length:{udp.getLength(unpacked_udphdr)} '
          f'Checksum:{udp.getChecksum(unpacked_udphdr)}')