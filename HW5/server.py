from socket import *

def get_mime_type(filename):
    if filename.endswith('.html'):
        return 'text/html'
    elif filename.endswith('.png'):
        return 'image/png'
    elif filename.endswith('.ico'):
        return 'image/x-icon'
    else:
        return 'application/octet-stream'

s = socket()
s.bind(('', 80))
s.listen(10)
print("웹 서버가 시작되었습니다. 브라우저에서 http://127.0.0.1/index.html 접속하세요.")

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')
    if len(req) < 1:
        c.close()
        continue

    try:
        filename = req[0].split()[1][1:]
        if filename == '':
            filename = 'index.html'
    except:
        filename = 'index.html'

    try:
        mimeType = get_mime_type(filename)
        if mimeType.startswith('text'):
            f = open(filename, 'r', encoding='utf-8')
            content = f.read()
            header = 'HTTP/1.1 200 OK\r\nContent-Type: ' + mimeType + '\r\n\r\n'
            c.send(header.encode('euc-kr'))
            c.send(content.encode('euc-kr'))
        else:
            f = open(filename, 'rb')
            content = f.read()
            header = 'HTTP/1.1 200 OK\r\nContent-Type: ' + mimeType + '\r\n\r\n'
            c.send(header.encode())
            c.send(content)
        f.close()
    except FileNotFoundError:
        not_found_response = (
            "HTTP/1.1 404 Not Found\r\n\r\n"
            "<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>"
            "<BODY>Not Found</BODY></HTML>"
        )
        c.send(not_found_response.encode('euc-kr'))

    c.close()