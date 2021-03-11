import os
import socket
import multiprocessing


def worker(s):
    print("Worker started with pid", os.getpid())
    conn, addr = s.accept()

    with conn:
        print("Client connected:", addr)

        while True:
            data = conn.recv(1024)

            if not data:
                break

            print("Incomming data:", data)

            conn.sendall(data.upper()[-1::-1])


def main():
    with socket.socket() as s:
        print("Starting server on 127.0.0.1:3333...")
        s.bind(('127.0.0.1', 3333))
        s.listen()

        num_workers = 4
        workers = [s for _ in range(num_workers)]
        with multiprocessing.Pool(processes=num_workers) as executor:
            executor.map(worker, workers)


if __name__ == "__main__":
    main()
