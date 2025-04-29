1. 
	a) IPv4 has more fields and the header itself is shorter. It has fields like checksum, options, fragmenting, etc that IPv6 doesn't. IPv6 has something called Flow Label and Traffic class which IPv4 doesn't. They both have version and source/dest but the source/dest is much longer for IPv6. Both also have a payload but that is obvious
	b) Yes the router is using NAT because only one IP address is given. The router is the only one with an IP address given by the ISP so it has to be using a NAT. Because of this, the 5 devices are given a local IP address by the router that will be used within the network. These IP addresses will be chosen by the network but are usually starting with 10.0.0.0. To get these IP address, DHCP will be used between the router and the devices themselves. 
2. 
	a) From x

| Step | N'            | D(t) , p(t) | D(v) , p(v) | D(u) , p(u) | D(y) , p(y) | D(z) , p(z) | D(w) , p(w) |
| ---: | ------------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
|    0 | x             | inf         | 3 , x       | inf         | 6 , x       | 8 , x       | 6 , x       |
|    1 | x v           | 7 , v       | 3 , x       | 6 , v       | 6 , x       | 8 , x       | 6 , x       |
|    2 | x v w         | 7 , v       | 3 , x       | 6 , v       | 6 , x       | 8 , x       | 6 , x       |
|    3 | x v w y       | 7 , v       | 3 , x       | 6 , v       | 6 , x       | 8 , x       | 6 , x       |
|    4 | x v w y u     | 7 , v       | 3 , x       | 6 , v       | 6 , x       | 8 , x       | 6 , x       |
|    5 | x v w y u t   | 7 , v       | 3 , x       | 6 , v       | 6 , x       | 8 , x       | 6 , x       |
|    6 | x v w y u t z | 7 , v       | 3 , x       | 6 , v       | 6 , x       | 8 , x       | 6 , x       |
	b) From t	

| Step | N'            | D(v) , p(v) | D(x) , p(x) | D(z) , p(z) | D(y) , p(y) | D(u) , p(u) | D(w) , p(w) |
| ---: | ------------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
|    0 | t             | 4 , t       | inf         | inf         | 7 , t       | 2 , t       | inf         |
|    1 | t u           | 4 , t       | inf         | inf         | 7 , t       | 2 , t       | 5 , u       |
|    2 | t u v         | 4 , t       | 7 , v       | inf         | 7 , t       | 2 , t       | 5 , u       |
|    3 | t u v w       | 4 , t       | 7 , v       | inf         | 7 , t       | 2 , t       | 5 , u       |
|    4 | t u v w x     | 4 , t       | 7 , v       | 15 , x      | 7 , t       | 2 , t       | 5 , u       |
|    5 | t u v w x y   | 4 , t       | 7 , v       | 15 , x      | 7 , t       | 2 , t       | 5 , u       |
|    6 | t u v w x y z | 4 , t       | 7 , v       | 15 , x      | 7 , t       | 2 , t       | 5 , u       |
3. 
	![[Pasted image 20250423125943.png]]
	![[Pasted image 20250423122953.png]]
	a) 
		![[Pasted image 20250423123814.png]]
		The -s flag shows statistics of the protocol including information like packet type and amount received, dropped packets, etc. In the screenshot, we can see different protocols like Ip, TCP, UDP, and more and each line has different statistics about the protocol. Like for example there are 2833 active TCP connections. 
		![[Pasted image 20250423124359.png]]
		The -c flag shows the network connections but updates it every second so the information it is giving is in real time and not out of date. Other than that the info is the same as just regular netstat which shows active internet and local connections
		![[Pasted image 20250423124816.png]]
		The -r flag shows the routing table for the kernel which essentially just tells the computer where to route traffic. Looking at the last entry, the address 172.18.0.0 is the network for the route (in this case I think it is a doker container), the gateway is none, the mask is for the size of the network (/16), the flag is U which means active. The next 2 are for max segment/window size (not used). irtt is round trip estimate (not used). And the last one is the network interface which according to google is a docker bridge.
	b)
		![[Pasted image 20250428133314.png]]
		This is for KU. The first lease was replaced by the second entry when I forced my computer to renew the lease (I wasn't sure if I did it right). It is cool to see a history of the leases. The mask is /17 and The lease length is 8 mins which is not very long. The DHCP broadcast address is 10.109.127.255 which is the highest address for /17

4. 
	![[Pasted image 20250423140421.png]]
		School, accurate
	![[Pasted image 20250423140823.png]]
		Different university (CMU), accurate
	![[Pasted image 20250423141149.png]]
		Friend's website hosted with cloudflare, also accurate because cloudflare is based in SF.
	![[Pasted image 20250423143400.png]]
		Zurich website, also accurate
	All of the websites were accurate when it came to finding the city of hosting. 
	b) One use case is for services to target info to people living in certain areas. There is no point in showing news articles about a city in China to someone living in North Dakota so being able to target the user with information that is closer (literally) to them is useful. The other is to track malicious users. If there is someone committing crimes on the internet then you can find where they are and respond with law enforcement in that city. 



# Lab
![[Pasted image 20250429140900.png]]

![[Pasted image 20250429140959.png]]	
1. UDP
2. The process of DHCP has 4 steps
	1. First, DHCP Discover is used to send a message to the network that it is looking for an IP address
	2. Second, the DHCP server sends a message with an IP (and other info sometimes). This IP is what the client can use (DHCP offer)
	3. Third, the user then asks to use that available IP address (DHCP request)
	4. And lastly, the DHCP confirms that client is using that IP with DHCP ACK
	![[Pasted image 20250429141809.png]]
3. 
	
| Packet        | Source IP    | Source Port | Dest IP         | Dest port |
| ------------- | ------------ | ----------- | --------------- | --------- |
| DHCP Discover | 0.0.0.0      | 68          | 255.255.255.255 | 67        |
| DHCP Offer    | 129.237.32.1 | 67          | 10.108.66.160   | 68        |
| DHCP Request  | 0.0.0.0      | 68          | 255.255.255.255 | 67        |
| DHCP ACK      | 129.237.32.1 | 67          | 10.108.66.160   | 68        |
4. There are a couple differentiating factors. The most important is in the options 53 field where value of 1 is for discover and value of 3 is Request. Secondly reqest has another field 54 for a server identifier which checks out because now we know what the server is
	Discover: 
	![[Pasted image 20250429145024.png]]
	Request:
	![[Pasted image 20250429145049.png]]
5. The transaction IDs are as follows:
	![[Pasted image 20250429145316.png]]
	They exist in order to keep track of which DHCP request chain each message belongs to. If a server gives 2 DHCP messages to the same laptop, it can help differentiate which it belongs to. The first set has transaction ID 0xf3e7d520 and the second set has 0xe1232626
6. The DHCP server is 129.237.32.1. This is found in two places, first the source of the offer and ack packets. Secondly it can be found in Option 54 of the DHCP request packet. The pictures are above
7. Again the IP is 129.237.32.1. Found in Option 54 
	 ![[Pasted image 20250429150042.png]]
8. The lease time is like a check-in to make sure you are still there. After a certain amount of time, if the lease is expired and the user is gone, we can forgo the connection so that we don't sustain connections that are gone. The IP is now freed up and can be used by someone else. If the user wishes to stay connected, they simply renew the lease and then nothing changes. 
	For us, the lease time is 7200s or 2 hours which makes sense as students enter and leave campus frequently (I am on campus)
	![[Pasted image 20250429150407.png]]