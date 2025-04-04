1. 
	a) TCP is a protocol that is reliable with flow and congestion control. If there are any dropped packets or errors or anything of the sort, a new packet will be delivered that is correct. The delivery of the packets is also controlled so the end user is not overwhelmed. UDP on the other hand is much faster but is not reliable. There is no guarantee that the packet reached and/or isn't corrupted. This is because unlike TCP, UDP has no connections it is just sending a packet. There is no feedback (ACK) like with TCP for when the packet reaches correctly.
	b) QUIC runs on top of UDP so it is low latency and uses the UDP transport method. Like TCP, it has congestion/flow control and other similar mechanisms to make it reliable. It is significantly faster than TCP though. It also has multiplexing allowing for multiple data to be sent over one connection as well as encryption built in (instead of TLS)
	c) QUIC is supported by all browsers and HTTP/3. It is also over half of Google's full traffic. According to https://w3techs.com/technologies/details/ce-quic it is used by a little over 8% of all websites
2. 
	01010011 + 01100110 = 10111001 + 01110100 = 0010_1101, complement = 1101_0010. The complement is used because you can add the original sum to the complement and then get all 1s. This is a lot easier for the computer to check than individual bits. The complement also makes it endian independent. If just the sum is used then the computer doesn't know if the start is the largest number or the end. Errors are detected if the sum of all the bits + the checksum given does not equal all 1s. 1-bit errors will always be detected while 2-bit errors will not be.
3. 
	a) Source is 1500 and destination is 1200
	b) Yes, the source IP will be different for both packets
	c) https://en.wikipedia.org/wiki/File_Transfer_Protocol 20 and 21
	d) They will all pass through a welcoming socket which establishes a separate socket for each of host A and B. The seperate sockets will be IDd using the source port and IP address. The sockets will be different but the number will be the same
4. 
	a) Sequence numbers are needed to make sure all the packets arrive and the correct order they are supposed to be in. The receiver doesn't know the order or how many packets in total so this allows for the reciever to realize a packet is missing and keep them in the correct order
	b) Timers are needed in case a packet is dropped. If a packet is dropped, the sender doesn't know so they set a timer so that after a certain point, they assume it is dropped and they send another one. If there wasn't one then the packet exchange would stall as the sender would be waiting to receive a packet before sending another one.
	c) Yes because if the delay is constant then the timer should be that constant time. The only time it is not needed is if there is a guarentee that packets wont be dropped.
5. 
	a) Telnet is on port 23 and it is like an SSH. You access a CLI remotely but it is insecure with no encryption so it is kind of obsolete.
	b) 
		i) A: Arbitrary, lets say 8100. S = 23 
		ii) B: Arbitrary, lets say 8101. S = 23 
		iii) A: Same as before 8100. S = 23 
		iv) B: Same as before 8101. S = 23 
		v) Yes, the sources aren't aware of each other so they could randomly use the same one. It doesn't matter since the source IP is also used as the key
		vi) If they are the same host then it needs to be different because then source IP would be the same and if the port is too then the key would be the same making it impossible to distinguish
	