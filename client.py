import socket

def start_client():
    server_host = '127.0.0.1'
    server_port = 8888

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_host, server_port))

    message = "Hello, server! This is a test message."
    client.sendall(message.encode())

    # Receive the echoed message from the server
    echoed_message = client.recv(1024)
    print(f"Received echoed message from server: {echoed_message.decode()}")

    # Close the client socket
    client.close()

if __name__ == "__main__":
    start_client()
