import socket

HOST = '127.0.0.1'
PORT = 2500

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("계산기를 시작합니다. 'q'를 입력하면 종료됩니다.")

while True:
    expression = input("계산식 입력 (예: 20 + 17): ")
    client_socket.send(expression.encode())

    if expression.lower() == 'q':
        break

    result = client_socket.recv(1024).decode()
    print(f"결과: {result}")

client_socket.close()