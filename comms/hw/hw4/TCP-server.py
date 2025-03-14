import socket
import datetime
import sys

port = int(sys.argv[1])
try:
    s = socket.socket()
    s.bind(('0.0.0.0', port))
    s.listen()
    print("established socket")
except socket.error as err:
    print("Error: ", err)
    exit()



print("Listening on port: ", port)

while True:
    try:
        c, addr = s.accept()
        print("Connected with ", addr)

        c.send(f'{datetime.datetime.now()}'.encode())


        print("Sent date")

        c.close()

    except KeyboardInterrupt:
        print("Stopping program, closing socket")
        s.close()
        break


