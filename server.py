import socket

def server(q, host='localhost', port=8888, BUFFER_SIZE=1000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, port))
        sock.listen(10)
        while True:
            (conn, addr) = sock.accept()
            while True:
                data = conn.recv(BUFFER_SIZE)
                if data:
                    print('{}> {}'.format(addr, data.decode('utf-8')))
                    q.put(data.decode('utf-8'))
                    # return data.decode('utf-8')
                else:
                    break

if __name__ == '__main__':
    server('163.221.126.13', 37564)
    # print('hoge')