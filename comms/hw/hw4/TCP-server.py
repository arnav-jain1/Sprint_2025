import socket
import datetime
import sys

port = int(sys.argv[1])
try:
    s = socket.socket()
    s.bind(('', port))
    print("established socket")
except socket.error as err:
    print("Error: ", err)
    exit()



print("Listening on port: ", port)

counter = 0
while True:
    try:
        c, addr = s.accept()
        print("Connected with ", addr)

        c.send(f'{datetime.datetime.now()}'.encode())


        print("Sent date")

        c.close()
        print("Closed connection")
        counter += 1

    except KeyboardInterrupt:
        print("Stopping program, closing socket")
        s.close()


