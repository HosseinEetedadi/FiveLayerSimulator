import socket

def start_server():
    server_host = '127.0.0.1'
    server_port = 8888

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((server_host, server_port))

    print(f"Server listening on {server_host}:{server_port}")

    while True:
        data, client_address = server.recvfrom(1024)
        print(f"Received message from {client_address}: {data.decode()}")

        # Echo the received message back to the client
        server.sendto(data, client_address)

if __name__ == "__main__":
    start_server()
