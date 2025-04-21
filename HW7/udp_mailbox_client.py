from socket import *

server_ip = 'localhost'
port = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

print("UDP 클라이언트 시작...")

while True:
    msg = input('Enter the message("send mboxId message" or "receive mboxId"): ')


    sock.sendto(msg.encode(), (server_ip, port))

    if msg == "quit":
        print("클라이언트 종료")
        break

    data, _ = sock.recvfrom(BUFF_SIZE)
    print("<-", data.decode())

sock.close()