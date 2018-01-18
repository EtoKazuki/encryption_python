from __future__ import print_function
import socket
# from contextlib import closing
import readchar as rc


def main():
    host = '127.0.0.1'
    port = 4000
    # bufsize = 4096

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    while 1:
        kb = rc.readchar()
        kb = kb.encode("UTF-8")
        sock.send(kb)
        if kb == b'q':
            print(kb, end='', flush=True)
            sock.close()
            break


if __name__ == '__main__':
    main()
