import socket
import threading
from typing import Dict


def main():
    print("Logs from your program will appear here!")

    # Creating a server socket bound to localhost on port 4221
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)

    # server_socket.listen()
    # while True:
    #     client, _ = server_socket.accept()
    #     with client:
    #         request = client.recv(1024).decode("utf-8")
    #         lines = request.split("\r\n")
    #         _, path, _ = lines[0].split()
    #         if path == "/":
    #             response = "HTTP/1.1 200 OK\r\n\r\n"
    #         elif path.startswith("/echo/"):
    #             response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(path[6:])}\r\n\r\n{path[6:]}"
    #         elif path.startswith("/user-agent"):
    #             user_agent = "User-Agent header not found"
    #             for line in lines:
    #                 if line.startswith("User-Agent:"):
    #                     user_agent = line.split(": ", 1)[1]
    #                     break
    #             response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(user_agent)}\r\n\r\n{user_agent}"
    #         else:
    #             response = "HTTP/1.1 404 Not Found\r\n\r\n"
    #         client.sendall(response.encode())

    server_socket.listen()

    # Accepting a client connection (blocking call)
    client_socket, client_address = server_socket.accept()

    # Using 'with' to ensure the client socket is properly closed when done
    with client_socket:

        # Handling the client connection
        while True:
            # Log the accepted connection
            print(f"Accepted connection from {client_address}")
            data = client_socket.recv(
                1024
            )  # Receiving data from the client (up to 1024 bytes)

            # If no data is received, break the loop (client closed the connection)
            if not data:
                break

            # Decode the received data and split it by HTTP line delimiter
            request_data = data.decode().split("\r\n")

            response = b"HTTP/1.1 200 OK\r\n\r\n"  # Default response

            # Checking the request path, if it's not "/", set response to 404 Not Found
            if len(request_data) > 1:
                path = request_data[0].split(" ")

                if path[1] != "/":
                    response = b"HTTP/1.1 404 Not Found\r\n\r\n"

                if "echo" in path[1]:
                    string = path[1].strip("/echo/")
                    response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(string.encode())}\r\n\r\n{string}".encode()

                if "user-agent" in path[1]:
                    user_agent = request_data[2].split(": ")[1]
                    response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(user_agent.encode())}\r\n\r\n{user_agent}".encode()
                print(f"First par {path}")

            # Sending the HTTP response to the client
            print(f"Received: {data}")
            client_socket.sendall(response)


if __name__ == "__main__":
    main()
