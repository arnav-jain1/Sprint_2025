1. 
	a) 130-105= 25 bytes
	b) 105
2. a
	a) From time 0 to 6 and 23 to at least 26 but cut off. We know because the increase is exponential. It then switches to linear so it is no longer slow start
	b) From time 6 to 16 and 17 to 22. In these intervals the packets sent increase linearly
	c) Triple ACK because the window gets halved. It is TCP Reno so halving is done when Triple ACK
	d) timeout because the window is set to 1. In both Reno and Tahoe you set to 1 on timeout
	e) Looks like 32 because that is when it switches from exponential to linear
	f) Looks like 21ish because once again it is linear from here on out. Also the ssthresh is halved whenever a loss event occurs and in TCP Reno you half if you get a triple ACK so since the half was 21, that means the SSThresh is too
	g) Looks like 13 or so since the window was 26 when the event occured so half would be 13.
	h) 7. The first 6 are `1 + 2 + 4 + 8 + 16 + 32=63`. The 7th has size of 33 so that would bump this to 96 so the 70th packet is in the 7th round
	i) 4 for both since loss at 8 packets sent, the ssthresh gets halved so 4.
3. 
	a) This gets sent to 3 since it starts with 110 which doesn't match with any so goes to 3
	b) This one goes to 2. The only one that fits is the prefix for 2. The prefix for 0 requires 0 for 8th bit so it won't work. Same with 1. 2 Works and 3 requires 1 for 9th bit which fails so 2
	c) This one would be 3. There are two matches 2 and 3 but 3 is a longer match so it goes to 3
4. 
	a) Forwarding and routing. Forwarding is taking the input and putting it on the right output port. This moves the packet in the same router. It is like getting in a lane to get out of the parking lot. Routing is figuring out how to get to the destination and where the packet will travel. This is like Google maps figuring out a route
	b) In the header, there is a section called upper layer protocol which differentiates between TCP and UDP
	c) If an application generates 40 bytes of data, there is 20 bytes for TCP and 20 for network layer header overhead so total of 80. 50% will be headers and 50% data
	d) 4 fragments are generated. If you are trying to send 2400byte datagram then there is 2380 bytes of data. 700 is the max per so 4 segments are needed. 
		Packet 1: 680 bytes of data; Frag flag = 1; 0 offset flag
		Packet 2: 680 bytes of data; Frag flag = 1; 680/8=85 offset flag
		Packet 3: 680 bytes of data; Frag flag = 1; 680\*2/8=170 offset flag
		Packet 4: 340 bytes of data; Frag flag = 0; 680\*3/8=255 offset flag
		The first 3 packets have total size 700 while the last has 360
		All packets have ID of 422

# Wireshark
![[Pasted image 20250415202443.png]]
a. 192.168.77.128:45388
b. 90.130.70.73:80
c. The raw seq number is 465196406 with the relative being 0. The SYN flag in the TCP header is set to 1 in order to identify it as a SYN packet
d. The relative ack is 1 with raw being 465196407. The relative syn is 0 and raw is 3758151152
e. The relative seq is 1 with raw being 3758151153
![[Pasted image 20250415202450.png]]
f. The slow start is from the start till around .125. After that it seems like the max transmit peaks and there are no slopes that are larger. The vertical bars stay around that same height. 
![[Pasted image 20250415202504.png]]