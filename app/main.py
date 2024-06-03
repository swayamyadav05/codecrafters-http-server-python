# import socket


# def parse_request(request_data):
#     lines = request_data.split("\r\n")
#     start_line = lines[0]
#     method, path, version = start_line.split(" ")
#     return method, path, version


# def get_response(path):
#     responses = {
#         "/": "HTTP/1.1 200 0K\r\n\r\n",
#     }

#     default_response = "HTTP/1.1 404 Not Found\r\n\r\n"

#     return responses.get(path, default_response)


# def handle_request(client_socket):
#     client_socket.recv(1024)

#     response = "HTTP/1.1 200 OK\r\n\r\n"
#     client_socket.send(response.encode())


# def main():
#     server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
#     print("Server is running on port 4221...")

#     try:
#         while True:
#             print("Waiting for a connection...")
#             client_socket, client_address = server_socket.accept()

#             print(f"Connection from {client_address} has been established...")

#             handle_request(client_socket)

#             client_socket.close()

#     except KeyboardInterrupt:
#         print("\nServer is shutting down...")

#     finally:
#         server_socket.close()
#         print("Server has been shut down.")


# if __name__ == "__main__":
#     main()


import socket


def main():
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
                response = b"HTTP/1.1 404 Not Found\r\n\r\n"
            client_socket.sendall(response)


if __name__ == "__main__":
    main()
