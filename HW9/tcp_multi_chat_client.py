import socket
import threading

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024)
            if not msg:
                break
            print(msg.decode())
        except:
            break

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 2500))

    my_id = input("ID를 입력하세요: ")
    sock.send(f"[{my_id}] 님이 입장하셨습니다.".encode())

    # 수신 스레드 시작
    recv_thread = threading.Thread(target=receive_messages, args=(sock,))
    recv_thread.daemon = True
    recv_thread.start()

    # 입력 및 메시지 전송
    while True:
        msg = input()
        if msg.lower() == "quit":
            sock.send(f"[{my_id}] 님이 퇴장하셨습니다.".encode())
            break
        full_msg = f"[{my_id}] {msg}"
        sock.send(full_msg.encode())

    sock.close()

if __name__ == "__main__":
    main()