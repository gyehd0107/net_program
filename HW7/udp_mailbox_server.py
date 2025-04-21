from socket import *

port = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

# mboxID 별로 메시지를 저장할 딕셔너리
mailbox = {}

print("UDP 서버 시작...")

while True:
    data, addr = sock.recvfrom(BUFF_SIZE)
    msg = data.decode()

    if msg.startswith("send "):
        parts = msg.split(' ', 2)
        if len(parts) < 3:
            sock.sendto("Invalid format".encode(), addr)
            continue
        mboxID, message = parts[1], parts[2]

        if mboxID not in mailbox:
            mailbox[mboxID] = []
        mailbox[mboxID].append(message)

        sock.sendto("OK".encode(), addr)

    elif msg.startswith("receive "):
        parts = msg.split(' ', 1)
        mboxID = parts[1]

        if mboxID in mailbox and len(mailbox[mboxID]) > 0:
            msg_to_send = mailbox[mboxID].pop(0)
            sock.sendto(msg_to_send.encode(), addr)
        else:
            sock.sendto("No messages".encode(), addr)

    elif msg == "quit":
        print("서버 종료")
        break

    else:
        sock.sendto("Unknown command".encode(), addr)

sock.close()