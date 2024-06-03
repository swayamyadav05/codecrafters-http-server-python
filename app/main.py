import socket


def main():
    print("Logs from your program will appear here!")

    # Creating a server socket bound to localhost on port 4221
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)

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
            if request_data[0].split(" ")[1] != "/":
                response = b"HTTP/1.1 404 Not Found\r\n\r\n"

            # Sending the HTTP response to the client
            client_socket.sendall(response)


if __name__ == "__main__":
    main()
