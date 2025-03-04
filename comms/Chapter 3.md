# Sockets

Sockets: Door between Application process and end-end transport protocol 

Support UDP and TCP 

UDP:
	No connection between the user and the server
	No handshake
	IP and port specified for each packet
	WHen the packet is recieved, then the sender IP and port are known
	May come out of order
	![[Pasted image 20250303150824.png]]

TCP:
	Client needs to contact the server first so server must have a socket ready
	Client creates TCP socket with IP address and port of the server
	TCP established when client creates a socket
	Server creates a new socket when contacted so that server can talk to multiple clients
	![[Pasted image 20250303151808.png]]

So UDP has 1 socket for N clients and TCP has N+1 sockets for N clients
# Transport layer protocol

## Transport layer vs network layer
Network layer: Communication between hosts
	Drop messages (datagram)
	Re-order messages
Transport layer: Communication between processes
	Relies on network layer services
	Sender breaks messages into segments and reciever puts them back together


## Transport protocols
2 main TCP and UDP

TCP
	Reliable in-order delivery 
	Congestion and flow control
	connection setup
UDP
	Unreliable unordered delivery 
	Lightweight 

No delay or bandwidth guarantees for either


Sender Transport layer actions:
	Transport layer gets the message from the application layer
	It then determines the header values, creates the segment, and passes it to the IP (network)
Reciever Transport layer actions:
	Gets the segment from the IP (network) 
	Checks header, extracts message, and demultiplexes 

## Multiplexing
Sender:
	The processing of handling data from multiple sockets, done by adding header data which is then used split the packet
Receiver: 
	Uses header to deliver segments to the correct socket
![[Pasted image 20250303154108.png]]


For connectionless (UDP), the host (receiver) checks the destination port number and directs the UDP segment to a socket with that port number
	All packets with same dest IP/port go to the same socket

Connection oriented (TCP):
	TCP socket is defined by 4 elements: Source IP/port and dest IP/port
	Receiver (demux) uses all 4 elements to direct the packet
	Server has to have many TCP sockets so each one is ID'd by the 4 tuple
	![[Pasted image 20250303155456.png]]
	All 3 have the same dest IP/port but go to different spots 

# UDP
Connectionless: Meaning no handshake, each segment is independent
Unreliable, unordered
Endpoints are ports

Pros
	Since no connection, less delay
	Also simpler with smaller header
	No congestion control so you can blast away as fast as possible


Good for:
	Streaming (loss tolerant vs rate sensitive when doing TCP vs UDP)
	DNS
	HTTP3
Can also just add reliability and congestion control at application layer

Format 
	![[Pasted image 20250303160415.png]]
Destination port number is either a well know port (like 53 for DNS or 161/2 for SNMP) or known before sending packets


Checksum:
	Goal is to check errors (flipped bits)
	Sender computes it by treating content of message as 16 bit ints and then just adding
	The receiver checks this by doing the same thing and making sure it matches
		If != then errors for sure
		If == then errors possible but not detected
	![[Pasted image 20250303161552.png]]
	The carry of the last bit is added to the original sum. Then, the 1s complement is taken so that if you add A+B+C, you get all 1s
	THis is not infallible though 
	![[Pasted image 20250303161702.png]]


Overall UDP is quick and dirty
	Also "best effort" aka send and hope for the best
	No handshake so faster and has checksum which is good

## Principals of reliable data transfer
Goals: 
1. Data integrity (No packet loss/duplication, and in-order)
2. Flow control (Receiver does not overflow)
Mechanisms:
	Acknowledgement (ACK) 
	Time out
	Re-transmission 

Application layer assumes reliable channel but transport layer does not
![[Pasted image 20250304095907.png]]
	The data transfer complexity depends highly on how reliable the channel is and why the channel is unreliable (corruption, packet loss)
	Sender and receiver also do not know state of each other  like whether a packet was received or not (unless communicated)

<mark style="background: #FF5582A6;">Missed some stuff</mark>

Implemented using finite state machines where it becomes more complex depending on the problem
	![[Pasted image 20250304100514.png]]
	Unidirectional but control flow changes both directions

### Case 1: Reliable channel
![[Pasted image 20250304100647.png]]
Really simple. As soon as you send the reciever just says received and you are good but unrealisitic

### Case 2: bit errors
Channel flips bits
Use checksums and acknowledgement
Acknowledgement (ACK): 
	Tells sender packet was received 
Negative Acknowledgement (NAK): Tells sender packet has errors and the sender resends
The sender waits for the ACK before sending another (stop and wait)
	