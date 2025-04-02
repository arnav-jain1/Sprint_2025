Application layer assumes reliable data transfer, transport layer has to actually implement the reliable transfer 
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
![[Pasted image 20250325082453.png]]
	Essentially the rdt_send() is called first and that gives it to rdt
	rdt calls udt_send() to send info over unreliable channel
	rdt_rev() for recieving the packet
	deliver_data() to get the packet to the upper layer

Implemented using finite state machines where it becomes more complex depending on the problem
	![[Pasted image 20250304100514.png]]
	Unidirectional but control flow changes both directions

incrementally develop the sender and receiver, called reliable data transfer protocol

### Case 1: Reliable channel
![[Pasted image 20250304100647.png]]
Really simple. You just keep sending like UDP

### Case 2: bit errors
Channel flips bits
Use checksums and acknowledgement
Acknowledgement (ACK): 
	Tells sender packet was received 
Negative Acknowledgement (NAK): Tells sender packet has errors and the sender resends
The sender waits for the ACK before sending another (stop and wait)

![[Pasted image 20250325083450.png]]![[Pasted image 20250325083514.png]]
But what if ACK/NACK is corrupted? 
	Sender doesn't know and can't just re-transmit

Duplicates:
	Retransmit current packet if ACK/NACK is corrupted
	Add a seq number so that the reciever can check if they already have it, discard if so
	![[Pasted image 20250325083828.png]]

Sender:
![[Pasted image 20250325084108.png]]

Reciever:
![[Pasted image 20250325084152.png]]

### RDT 2.2 NACK-free
Same as the prev but no more NACKs
Instead ACKs has seq number and if 2 of the same ACKs come back, that acts as a NACK
![[Pasted image 20250325084328.png]]


### RDT 3.0
Previous assumed packets were not lost, they were just wrong but what if packets are lost
Sender waits certain amount of time for ACK (timeout), retransmit if no ack
	retransmission duplicate doesnt matter bc of seq number
Called automatic repeat request (ARQ)
![[Pasted image 20250325084912.png]]
![[Pasted image 20250325084943.png]]


Sender
![[Pasted image 20250325085020.png]]

Performance:
	U (Utilization): fraction of time sender is sending
	Example: 1 Gbps, 15ms prop, 8000 bit packet
		D = L/R = 8000/10^9 = 8microsec
	![[Pasted image 20250325090907.png]]
	Util = D/(RTT+ D)
	Performance SUCKS
Pipelining: Sender has multiple in flight packets that are yet to be acknowledged
	Range of seq numbers increased
	Buffering and sender and/or receiver

![[Pasted image 20250325091149.png]]

2 ways to implement: 
	Go-back-N:
		Sender has N packets in the pipeline
		Receiver sends 1 cumulative ACK
		sender has timer for the oldest unacked packet, transmit all unacked packets 
	Selective repeat:
		Sender has N packets in pipeline
		Individual ack for each packet
		Timer for each packet, retransmit only the unacked packet

Go-back-N:
	Sender:
		"window" of N transmitted but unacked packets
		![[Pasted image 20250325093719.png]]
		ACK all packets up to (and including) seq number N, when ACK is received, move the window to start at n+1
		Timer for oldest packet
		timeout(n): retransmit n and all higher seq numbers
	Reciever:
		ACK-only: always send ACK for correctly recieved packet with the highest in order seq number
			Only need to remember rsv base but may generate duplicate ACKs
		When it gets a packet that is out of order:
			You can discard or you can save depending on implementation
			reACK pkt with the highest in-order seq #![[Pasted image 20250325094632.png]]
	![[Pasted image 20250325094723.png]]	


Selective repeat:
	Reciever acknoledges each correct packet individually
		Buffer the packets as you need them to get back to in-order
	Sender time-outs individually for each unacked packet (timer for each packet)
	Sender window:
		N consecutive seq \#s, limits seq # of sent unacked packet
	![[Pasted image 20250325095244.png]]
	Sender:
		If the next availble seq number is ready, send it
		timeout for each packet, resend the packet
		Mark each packet as recieved once you get it
		If the end (n) is the smallest unacked packet, move the window
	Receiver:
		When you get the packet send the ACK
		Buffer any out of order packet
		In order packet moves the window to the next packet that you are waiting for
		If it is in the previous window, then send the ack
		If it is not in the current or prev window, ignore it
	![[Pasted image 20250325100043.png]]



One issue with selective repeating is this scenario:
	Lets say 4 seq # (base 4 counting) and window size 3
	![[Pasted image 20250325100229.png]]
	There is a mismatch and neither sides are aware
	Size of seq # needs to be at least 2x window size


# TCP Overview
- Point-to-point: One sender/reciever 
- Reliable, in-order
- Full duplex (bidirectional)
- Cumulative acks
- Pipelining: congestion and flow control, set window size
	- Won't overwhelm receiver
- Connection-oriented: handshaking to initialize sender and reciever before sending


## Segment
Segment size:
	![[Pasted image 20250401102116.png]]
	The max segment size is 1460, add 20B for Transport layer
Segment structure:
	Includes source and dest port, seq number(counts bytes of data in the stream, not segments)
	seq # of the next expected byte, checksum
	Length of header
	Bits for: ACK, congesstion control options, (C, E), RST/SYN/FIN for connection management, 
	Flow control: Bytes that can be accepted
	TCP options and data
	![[Pasted image 20250401102631.png]]

	The seq number is the position of the first byte of the packet. 
Ack: Seq number of the next expected byte


Out of order packets is up to implementer to decide