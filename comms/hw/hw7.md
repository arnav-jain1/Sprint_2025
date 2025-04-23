1. 
	a) IPv4 has more fields and the header itself is shorter. It has fields like checksum, options, fragmenting, etc that IPv6 doesn't. IPv6 has something called Flow Label and Traffic class which IPv4 doesn't. They both have version and source/dest but the source/dest is much longer for IPv6
	b) Yes the router is using NAT because only one IP address is given. The router is the only one with an IP address and there is no DHCP so it has to be using a NAT. Because of this, the 5 devices are given a local IP address by the router that will be used within the network. These IP addresses will be chosen by the network but are usually starting with 10.0.0.0
2. 
	a) From x

| dest | route | cost |
| ---- | ----- | ---- |
| t    | v t   | 7    |
| u    | v u   | 6    |
| v    | v     | 3    |
| w    | w     | 6    |
| x    | -     | -    |
| y    | y     | 6    |
| z    | z     | 8    |
	b) From t	

| dest | route | cost |
| ---- | ----- | ---- |
| t    | -     | -    |
| u    | u     | 2    |
| v    | v     | 4    |
| w    | u w   | 5    |
| x    | v x   | 7    |
| y    | y     | 7    |
| z    | v x z | 15   |

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
TODO


4. 