import socket
import threading

clients = []  

def client_handler(conn, addr):
    print(f"[+] 새로운 클라이언트 접속: {addr}")
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode()
            print(f"{addr}: {message}")
            
            for client in clients:
                if client != conn:
                    try:
                        client.send(data)
                    except:
                        client.close()
                        clients.remove(client)
        except:
            break

    print(f"[-] 클라이언트 종료: {addr}")
    clients.remove(conn)
    conn.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 2500))
    server.listen()

    print("[*] 서버 시작됨. 포트 2500에서 대기 중...")

    while True:
        conn, addr = server.accept()
        clients.append(conn)
        thread = threading.Thread(target=client_handler, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    main()