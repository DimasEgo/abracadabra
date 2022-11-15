import socket

PORT = 5000
IP = '127.0.0.1'


def run_server(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip, port))
    sock.listen(1)
    print(f'Server is ready on {ip}:{port}')
    connection, address = sock.accept()
    try:
        while True:
            message_from_client = connection.recv(128)
            if not message_from_client:
                break
            print(f'Received a message from a client: {message_from_client.decode("utf-8")}')
            massage = input('->>: ')
            connection.send(massage.encode('utf-8'))
    except KeyboardInterrupt as e:
        print(f'KeyboardInterrupt: {e}')
    finally:
        connection.close()
        sock.close()


if __name__ == '__main__':
    run_server(IP, PORT)
