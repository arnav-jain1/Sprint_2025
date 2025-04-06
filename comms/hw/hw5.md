# HW 5

## Part 1
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
	d) They will all pass through a welcoming socket which establishes a separate socket for each of host A and B. The separate sockets will be ID'd using the source port and IP address. The sockets will be different but the number will be the same
4. 
	a) Sequence numbers are needed to make sure all the packets arrive and the correct order they are supposed to be in. The receiver doesn't know the order or how many packets in total so this allows for the receiver to realize a packet is missing and keep them in the correct order
	b) Timers are needed in case a packet is dropped. If a packet is dropped, the sender doesn't know so they set a timer so that after a certain point, they assume it is dropped and they send another one. If there wasn't one then the packet exchange would stall as the sender would be waiting to receive a packet before sending another one.
	c) Yes because if the delay is constant then the timer should be that constant time. The only time it is not needed is if there is a guarantee that packets wont be dropped.
5. 
	a) Telnet is on port 23 and it is like an SSH. You access a CLI remotely but it is insecure with no encryption so it is kind of obsolete.
	b) 
		i) A: Arbitrary, lets say 8100. S = 23 
		ii) B: Arbitrary, lets say 8101. S = 23 
		iii) A: Same as before 8100. S = 23 
		iv) B: Same as before 8101. S = 23 
		v) Yes, the sources aren't aware of each other so they could randomly use the same one. It doesn't matter since the source IP is also used as the key
		vi) If they are the same host then it needs to be different because then source IP would be the same and if the port is too then the key would be the same making it impossible to distinguish
## Part 2
1. ![[Pasted image 20250404184730.png]]
	I could see me messing up the password (but not the password itself) as well as me doing it correctly. The password is blank whether it is right or not
2. ![[Pasted image 20250404185218.png]]
	DNS was used to find it and the local DNS found it successfully, probably because this is my second time trying it as I forgot to turn on wireshark the first time. The IP was 44.241.66.173
3. ![[Pasted image 20250404185830.png]]
	The first TCP is a syn and is in a different color. Wireshark specifies it as a \[SYN\] packet making it easier to spot. It is also outgoing. The one after was a SYN ACK so that is how I was sure it was correct and that was incoming which is how I know it was correct.
4. 

| Table 1         |                                                                                                                 |
| --------------- | --------------------------------------------------------------------------------------------------------------- |
| Source IP       | 192.168.50.27                                                                                                   |
| Dest IP         | 44.241.66.173                                                                                                   |
| Source port     | 42922                                                                                                           |
| Dest port       | 21                                                                                                              |
| seq num         | 0                                                                                                               |
| ack num         | The info section shows nothing but when I look at the sumamry it says 0<br>![[Pasted image 20250404191110.png]] |
| header length   | 40 bytes                                                                                                        |
| window size<br> | 65535<br>                                                                                                       |
![[Pasted image 20250404191525.png]]
Only SYN
![[Pasted image 20250404191612.png]]

| Table 2         |               |
| --------------- | ------------- |
| Source IP       | 44.241.66.173 |
| Dest IP         | 192.168.50.27 |
| Source port     | 21<br>        |
| Dest port       | 42922         |
| seq num         | 0             |
| ack num         | 1             |
| header length   | 40 bytes      |
| window size<br> | 26847         |
![[Pasted image 20250404191446.png]]
SYN and ACK
![[Pasted image 20250404191639.png]]

| Table 3         |               |
| --------------- | ------------- |
| Source IP       | 192.168.50.27 |
| Dest IP         | 44.241.66.173 |
| Source port     | 42922         |
| Dest port       | 21            |
| seq num         | 1             |
| ack num         | 1             |
| header length   | 32 bytes      |
| window size<br> | 65535         |
![[Pasted image 20250404191507.png]]
Only ACK
![[Pasted image 20250404191655.png]]

5. 
	![[Pasted image 20250404192345.png]]
	So first, the server sends a FIN, ACK packet to me starting the data close. The ACK is to notify the last packet received by the server and the fin is to start the end of communication. The client then responds with a FIN ACK acknowledging it got the last FIN and sending its own FIN telling the server it is done on its side too. This termination ensures all the info before it is received and that both sides acknowledge each others termination 