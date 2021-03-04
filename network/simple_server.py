import socket

with socket.socket() as s:
    print("Starting server on 127.0.0.1:3333...")
    s.bind(('127.0.0.1', 3333))
    s.listen()

    conn, addr = s.accept()

    with conn:
        print("Client connected:", addr)

        while True:
            data = conn.recv(1024)

            if not data:
                break

            print("Incomming data:", data)

            conn.sendall(data.upper()[-1::-1])
