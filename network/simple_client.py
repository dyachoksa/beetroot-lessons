import socket

with socket.socket() as s:
    print("Connecting to 127.0.0.1:3333...")
    s.connect(('127.0.0.1', 3333))

    data = input("Type something q to exit: ")
    while data != 'q':
        print("Sending data...")
        s.sendall(data.encode())

        data = s.recv(1024)
        print("Response:", data)

        data = input("Type something q to exit: ")
