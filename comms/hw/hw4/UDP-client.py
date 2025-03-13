import socket
import sys
import datetime


ip = sys.argv[1]
port = int(sys.argv[2])
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(3)
    print("Established socket")
except socket.error as err:
    print("Error: ", err)
    exit()


try: 
    for i in range(3):
        try:
            send = datetime.datetime.now()
            s.sendto("hi".encode(), (ip, port))
            print("Sent message")
            info = s.recvfrom(1024)[0].decode()
            curr = datetime.datetime.now()
            if info:
                print("Recieved message")
                print("Server time: ", info)
                print("Current time: ", curr)
                print("Time delta (client to server): ", (datetime.datetime.fromisoformat(info) - send).total_seconds() * 1000, " ms")
                print("Time delta (server to client): ", (curr - datetime.datetime.fromisoformat(info)).total_seconds() * 1000, " ms")
                print("Time delta (Total RTT): ", (curr - send).total_seconds() * 1000, " ms")
                break
        except socket.timeout:
            print("Timeout while waiting for packet")
except Exception as err:
    print("Failed: ", err)



