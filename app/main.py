import socket


def handle_request(client_socket):
    client_socket.recv(1024)

    response = "HTTP/1.1 200 OK\r\n\r\n"
    client_socket.send(response.encode())


def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    print("Server is running on port 4221...")

    try:
        while True:
            print("Waiting for a connection...")
            client_socket, client_address = server_socket.accept()

            print(f"Connection from {client_address} has been established...")

            handle_request(client_socket)

            client_socket.close()

    except KeyboardInterrupt:
        print("\nServer is shutting down...")

    finally:
        server_socket.close()
        print("Server has been shut down.")

    # with client_socket:

    #     while True:
    #         print(f"Accepted connection from {client_address}")
    #         data = client_socket.recv(1024)
    #         if not data:
    #             break
    #         request_data = data.decode().split("\r\n")
    #         response = b"HTTP/1.1 200 OK\r\n\r\n"
    #         if request_data[0].split(" ")[1] != "/":
    #             response = b"HTTP/1.1 200 OK\r\n\r\n"
    #         client_socket.sendall(response)


if __name__ == "__main__":
    main()
