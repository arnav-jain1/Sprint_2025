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
		![[Pasted image 20250428133314.png]]
		This is for KU. The first lease was replaced by the second entry when I forced my computer to renew the lease (I wanted more interesting output). It is cool to see a history of the leases. The mask is /17 and The lease length is 8 mins which is not very long. The DHCP broadcast address is 10.109.127.255 which is the highest address for /17

4. 
	![[Pasted image 20250423140421.png]]
		School, accurate
	![[Pasted image 20250423140823.png]]
		Different university, accurate
	![[Pasted image 20250423141149.png]]
		Friend's website hosted with cloudflare, also accurate.
	![[Pasted image 20250423143400.png]]
		Zurich website, also accurate
	All of the websites were accurate when it came to finding the city of hosting. 
	b) One use case is for services to target info to people living in certain areas. There is no point in showing news articles about a city in China to someone living in North Dakota so being able to target the user with information that is closer (literally) to them is useful. The other is to track malicious users. If there is someone committing crimes on the internet then you can find where they are and respond with law enforcement in that city. 