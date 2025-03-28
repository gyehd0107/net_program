import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from', addr)

    # 인사 메시지 전송
    client.send(b'Hello ' + addr[0].encode())

    # 이름 수신 후 출력
    name = client.recv(1024)
    print('Received name:', name.decode())

    # 학번을 문자열로 준비 (정수 대신 문자열로 전송)
    student_id = '20223665'  # 자신의 학번 입력
    client.send(student_id.encode())

    client.close()


