# Chapter 1
## Network
The building blocks of networks are nodes and links
	Nodes:
		End systems (like computers)
		Switches, routers
	Links: connects nodes together
		Fiber, wires
		Can also be wireless (Wifi)
		Point to point: Like an ethernet cable that connects a router to a computer
		Multiple access (shared media): Shared link

Network: 2+ nodes connected by links
End node: The host
Internal nodes: switches and routers

The most important requirement is to provide connectivity, but performance (speed), scalability, stability, security, etc are important too

## Internetworking
Connecting networks
Router: special node that connects networks

Requires addressing schemes (ways to find someone) and routing schemes (how it will get there)

Address: Byte string that identifies a node (network)
	IPv4: 32 bits
Routing: The path that packets travel from start to dest
Forwarding: Advancing packets along the rout (more local limited to single node)
<mark style="background: #FF5582A6;">Forwarding vs routing</mark>

Ping does not give us information how the packet traveled just that it reached its destination or not


Address types:
	Unicast: 1-1, sending information from 1 to another
	Multicast: 1-Many, sending info from 1 to >1
	Broadcasting: 1-All, sending info from 1 to all nodes

## Network protocol
Network protocol is a way to respond to certain messages 


## Internet
The outside of the network is edge that's like computers that run the apps
	Hosts are the end systems
Network core are the interior that forward packets and data (router and switches)

Communication links: fiber, copper, radio, satiliite
	Bandwidth is how fast data can be transmitted 
	Two different types: Download and upload, download is more important

Internet is a network of networks
	Interconnected ISPs
Protocols are everywhere to manage the sending and recieving of messages (HTTP, streaming, ethernet, 4G, TCP, etc)
	When we use an ethernet cord, we are using a protocol 
Internet standards: 
	RFC: Requests for comments
	IETF: Internet engineering task force

The internet is infrastructure that provides services to apps
Provides a programming interface to distributed apps
	Hooks allow sending and reciving apps to connect to the intenet to transmit info

Internet structure:
	Edge:
		Hosts and servers
	Access networks/physical media:
		wired, wireless communication links
	Network core:
		Interconnected routers 
		Network of network


How are end systems connected to edge routers?
	residential access nets (WiFi at home)
	Institutional (school)
	mobile access (4G/5G)

Access networks:
	Consist of Wifi access point, router, and modem (sometimes combined)
	Router has a NAT (hides devices connected to network by saying packets only come from one point)

Wireless access networks
	Wireless local area networks (WLANs)
		802.11b/g/n (WiFi)
		Usually a range of around 100ft
	Wide area cellular access networks
		Provided by cellular network operators
		4G/5G

Internet structure is a network of networks
Each internet does not connect directly to another network because that would mean N^2 connections 
Instead there are global ISPs where you connect to the global and the global connects you to the one you are trying to connect to
The global ISPs there are many and to connect them there needs to be IXPs (internet exchange point)
	IXPs are literal physical buildings where ISPs connect to each other

Then, there are also smaller regional ISP
## Network Edge

I played geoguessr oops


## Network Core
Multiplexing: Sharing a resource among multippe users 
	Frequency Division Multiplexing (FDM): Partition resource in frequency, each device gets a different part of the frequency band
	Time division multiplexing (TDM): Partition resource in time, the device gets access to the full band but only for a certain time
<mark style="background: #FF5582A6;">	Statistical multiplexing</mark>: Not allocate rigid resources, resources used as needed (kind of sharing)


**Fundemental question:** How is data transferred through the network?
	Circuit switching: dedicated resource allocation
	Packet switching: 
Circuit switching is when you allocate resources (either freq or time) for a communication between networks. No one else can use the resource, it is "dedicated", ineffecient for burst or anything with inactivity, like a call

Packet switching: Hosts break application layer messages into packets where the packets are interleaved between users
	Users share network and send packets, each packet uses full bandwidth 
	Packets don't have to take the same route
	Resources only used as needed

The issue with this is that the amount of packets being sent can be more than the computer can handle, packet queue becoming too long can cause congestion and delays and if the queue is full then packets are dropped
	Pros: Good for bursty, resource sharing
	Cons: Can lead to congestion


Entire packet has to arrive at router before it can be transmitted
This begs the question, how many bits is the right number? why 1500