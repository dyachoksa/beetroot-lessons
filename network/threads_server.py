import socket
import threading


def worker(conn, addr):
    with conn:
        print("Client connected:", addr)

        while True:
            data = conn.recv(1024)

            if not data:
                break

            print("Incomming data:", data)

            conn.sendall(data.upper()[-1::-1])


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("Starting server on 127.0.0.1:3333...")
        s.bind(('127.0.0.1', 3333))
        s.listen()

        while True:
            try:
                conn, addr = s.accept()

                client_thread = threading.Thread(
                    target=worker, args=(conn, addr))
                client_thread.start()
            except KeyboardInterrupt:
                break


if __name__ == "__main__":
    main()
