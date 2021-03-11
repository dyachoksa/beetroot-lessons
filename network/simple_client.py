import socket

host = socket.gethostbyname("6.tcp.ngrok.io")
port = 11800

with socket.socket() as s:
    print("Connecting to 127.0.0.1:3333...")
    s.connect((host, port))

    data = input("Type something q to exit: ")
    while data != 'q':
        print("Sending data...")
        s.sendall(data.encode())

        data = s.recv(1024)
        print("Response:", data)

        data = input("Type something q to exit: ")
