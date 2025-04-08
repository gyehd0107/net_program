import socket
import random

HOST = 'localhost'
PORT = 9001

def generate_data():
    temp = random.randint(0, 40)
    humid = random.randint(0, 100)
    Iilum = random.randint(70, 150)
    return f"{temp},{humid},{Iilum}"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("[Device1] Waiting for connection...")
    conn, addr = s.accept()
    with conn:
        print(f"[Device1] Connected by {addr}")
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            if data == "Request":
                response = generate_data()
                conn.sendall(response.encode())
            elif data == "quit":
                print("[Device1] Quit received. Closing.")
                break