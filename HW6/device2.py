import socket
import random

HOST = 'localhost'
PORT = 9002

def generate_data():
    heartbeat = random.randint(40, 140)
    steps = random.randint(2000, 6000)
    cal = random.randint(1000, 4000)
    return f"{heartbeat},{steps},{cal}"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("[Device2] Waiting for connection...")
    conn, addr = s.accept()
    with conn:
        print(f"[Device2] Connected by {addr}")
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            if data == "Request":
                response = generate_data()
                conn.sendall(response.encode())
            elif data == "quit":
                print("[Device2] Quit received. Closing.")
                break