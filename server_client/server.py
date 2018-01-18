from __future__ import print_function
import socket
from contextlib import closing


def main():
    host = '127.0.0.1'
    port = 4000
    backlog = 1
    bufsize = 4096
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(backlog)
    conn, address = sock.accept()
    while True:
        msg = conn.recv(bufsize)
        print(msg)
        conn.send(msg)
        if msg == b"q":
            sock.close()
            break


if __name__ == '__main__':
    main()
