import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from', addr)

    client.send(b'Hello ' + addr[0].encode())

    name = client.recv(1024)
    print('Received name:', name.decode())

    student_id = '20223665'  
    client.send(student_id.encode())

    client.close()


