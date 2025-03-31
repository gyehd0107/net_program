import socket

def calculate(expression):
    try:
        # 공백 제거 후 연산자 찾기
        expression = expression.replace(" ", "")
        if '+' in expression:
            operands = expression.split('+')
            result = float(operands[0]) + float(operands[1])
        elif '-' in expression:
            operands = expression.split('-')
            result = float(operands[0]) - float(operands[1])
        elif '*' in expression:
            operands = expression.split('*')
            result = float(operands[0]) * float(operands[1])
        elif '/' in expression:
            operands = expression.split('/')
            result = float(operands[0]) / float(operands[1])
        else:
            return "지원하지 않는 연산자입니다."
        # 소수점 첫째 자리까지 출력
        return f"{result:.1f}"
    except Exception as e:
        return f"오류: {str(e)}"

HOST = '127.0.0.1'
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print("서버가 준비되었습니다. 클라이언트 연결 대기 중...")

client_socket, addr = server_socket.accept()
print(f"{addr} 에서 연결되었습니다.")

while True:
    data = client_socket.recv(1024).decode()
    if data.lower() == 'q':
        print("클라이언트가 연결을 종료했습니다.")
        break
    print(f"수신된 계산식: {data}")
    result = calculate(data)
    client_socket.send(result.encode())

client_socket.close()
server_socket.close()