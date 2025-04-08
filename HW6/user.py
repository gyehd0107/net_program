import socket
import time

def log_data(device, data):
    now = time.strftime('%a %b %d %H:%M:%S %Y')
    if device == 1:
        temp, humid, illum = data.split(',')
        line = f"{now}: Device1: Temp={temp}, Humid={humid}, illum={illum}"
    else:
        heartbeat, steps, cal = data.split(',')
        line = f"{now}: Device2: Heartbeat={heartbeat}, Steps={steps}, Cal={cal}"
    with open("data.txt", "a") as f:
        f.write(line + "\n")
    print(line)

def connect_and_request(port, device_number):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', port))
        for _ in range(5):  
            s.sendall("Request".encode())
            data = s.recv(1024).decode()
            log_data(device_number, data)
            time.sleep(1)
        s.sendall("quit".encode())

if __name__ == "__main__":
    while True:
        cmd = input("Enter 1 (Device1), 2 (Device2), or quit: ")
        if cmd == "1":
            connect_and_request(9001, 1)
        elif cmd == "2":
            connect_and_request(9002, 2)
        elif cmd == "quit":
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
                s1.connect(('localhost', 9001))
                s1.sendall("quit".encode())
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
                s2.connect(('localhost', 9002))
                s2.sendall("quit".encode())
            break
        else:
            print("Invalid input.")