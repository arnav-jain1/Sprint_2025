import socket
import datetime
import sys

port = int(sys.argv[1])
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', port))
except socket.error as err:
    print("Error: ", err)
    exit()



print("Socket established, ready on port ", port)

while True:
    try:
        d, addr = s.recvfrom(1024)
        print("Got from ", addr)

        s.sendto(f'{datetime.datetime.now()}'.encode(), addr)


        print("Sent date")


    except KeyboardInterrupt:
        print("Stopping program")
        s.close()
        break


