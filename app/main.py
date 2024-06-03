import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    client_socket, client_address = server_socket.accept()

    with client_socket:

        while True:
            print(f"Accepted connection from {client_address}")
            data = client_socket.recv(1024)
            if not data:
                break
            request_data = data.decode().split("\r\n")
            response = b"HTTP/1.1 200 OK\r\n\r\n"
            if request_data[0].split(" ")[1] != "/":
                response = b"HTTP/1.1 200 OK\r\n\r\n"
            client_socket.sendall(response)


if __name__ == "__main__":
    main()
