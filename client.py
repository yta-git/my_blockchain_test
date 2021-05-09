import socket

def client(host='localhost', port=8888, msg=''):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.settimeout(5)
            sock.connect((host, port))
            sock.sendall(msg.encode('utf-8'))

        except:
            print('ConnectionError:', host)

        finally:
            sock.shutdown(2)
            sock.close()


if __name__ == '__main__':
    client('163.221.124.239', 8888, '{"difficulty":6,"index":0,"nonce":9400292,"prev_block":"0000000000000000000000000000000000000000000000000000000000000000","time":1609836884,"tx":"test"}')
    # client('163.221.167.132', 8888, '{"command": "block_request"}')