import socket
import sys
import datetime


ip = sys.argv[1]
port = int(sys.argv[2])
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Established socket")
except socket.error as err:
    print("Error: ", err)
    exit()


try: 

    c1 = datetime.datetime.now()
    s.connect((ip, port))
    c2 = datetime.datetime.now()
    print("Time delta (Establish connection with server): ", (c2 - c1).total_seconds() * 1000, " ms")

    start = datetime.datetime.now()
    info = datetime.datetime.fromisoformat(s.recv(1024).decode())
    print("Got packet, Server time: ", info)
    curr = datetime.datetime.now()

    print("Current time: ", curr)
    print("Time delta (client to server): ", (info - start).total_seconds() * 1000, " ms")
    print("Time delta (server to client): ", (curr - info).total_seconds() * 1000, " ms")
    print("Time delta (RTT for info): ", (curr - start).total_seconds() * 1000, " ms")
    print("Time delta (info RTT + connection RTT): ", (c2 - c1 + curr - start).total_seconds() * 1000, " ms")
    
except Exception as err:
    print("Failed: ", err)



