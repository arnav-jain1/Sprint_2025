1. T
	a) He role of the router is to accumulate traffic on a network and direct it to where it is supposed to go. It gets information from devices on the network and sends it to where it is supposed to go. Then when receiving messages, it finds the right device on the network to send it to. Overall it connects devices across networks (core device)
	b) The two models I picked are *Nexus 7000 Supervisor 1* with 8gb memory and *Nexas 7700 Supervisor 3E* with 64. It also has 8 core processor (vs 2 core on the 7000) with 240gb ssd. In general, more gb RAM means more temporary storage so in the case of routers, it means a larger queue for network traffic allowing less packets to be dropped. It also allows the router to keep a bigger routing table which will allow for more devices to be connected
2. 
	a) $1-(1-p)^{h+d}$ 
	b) $((1-p)^{h+d} * \frac{d}{h+d} * C)$  
	c) $\approx 3113$ 
	![[Pasted image 20250213140640.png]]
3. 
	a)
		10k bits = .01 mb / 1mbps = .01s = 10 ms + 1 ms delay = 11ms 
		.01 mb / 2mbps = .005s = 5ms + 2ms delay = 7ms
		7ms + 11ms = 18ms
	b) 
		1k bits = .001 mb / 1mbps = .001s = 1 ms + 1 ms delay = 2ms 
		.001 mb / 2mbps = .0005s = 0.5ms + 2ms delay = 2.5ms
		2+2.5+9 * 1 since we only care about when the last packet reaches = 13.5
4. 
	a) UDP, TCP, ARP
	b) Host: 192.168.50.27	Others: 162.159.134.234 and 185.188.109.133
5. 
	a) 0.0436 time units (not specified)
	b) HTTP1.1 for both
	c) Host: 192.168.50.27 Server: 128.119.245.12
	d) 200
	e) Yes, a HTTP 404 Not found is received
	f) tslv1.3 and TCP 
	![[Pasted image 20250214203837.png]]