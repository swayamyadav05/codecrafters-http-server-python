import socket
import threading
from typing import Dict


def main():
    print("Logs from your program will appear here!")

    # Creating a server socket bound to localhost on port 4221
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)

    server_socket.listen()

    # Handling the client connection
    while True:
        # Accepting a client connection (blocking call)
        client_socket, client_address = server_socket.accept()

        # Using 'with' to ensure the client socket is properly closed when done
        with client_socket:
            # Log the accepted connection
            print(f"Accepted connection from {client_address}")
            data = client_socket.recv(1024).decode(
                "utf-8"
            )  # Receiving data from the client (up to 1024 bytes)

            # If no data is received, break the loop (client closed the connection)
            if not data:
                break

            # Decode the received data and split it by HTTP line delimiter
            request_data = data.split("\r\n")

            # Checking the request path, if it's not "/", set response to 404 Not Found
            if len(request_data) > 1:
                _, path, _ = request_data[0].split()

                if path != "/":
                    response = b"HTTP/1.1 404 Not Found\r\n\r\n"

                elif path.startswith("/echo/"):
                    response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(path[6:])}\r\n\r\n{path[6:]}"
                elif path.startswith("/user-agent"):
                    user_agent = "User-Agent header not found"
                    for line in lines:
                        if line.startswith("User-Agent:"):
                            user_agent = line.split(": ", 1)[1]
                            break
                    response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(user_agent)}\r\n\r\n{user_agent}"
                else:
                    response = b"HTTP/1.1 200 OK\r\n\r\n"  # Default response

                # Sending the HTTP response to the client
                print(f"Received: {data}")
                client_socket.sendall(response.encode())


if __name__ == "__main__":
    main()
