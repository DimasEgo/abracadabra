import socket

PORT = 5000
TCP_IP = '127.0.0.1'


def run_client(ip, port):
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect((ip, port))
    message = input('->>: ')
    try:
        while True:
            if message.casefold().strip() == 'exit' or message.strip() == '':
                break
            client_sock.send(message.encode('utf-8'))
            message_from_server = client_sock.recv(128)
            print(f'Received message from a server: {message_from_server.decode("utf-8")}')
            message = input('->>: ').casefold().strip()
    except KeyboardInterrupt as e:
        print(f'KeyboardInterrupt: {e}')
    finally:
        client_sock.close()


if __name__ == '__main__':
    run_client(TCP_IP, PORT)
