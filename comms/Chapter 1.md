# Intro
~31b IoT devices and ~10b non IoT (smartphones)
Video traffic takes up a lot of the total traffic
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
Packet switches forward packets (data chunks)
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
![[Pasted image 20250129124230.png]]
Then there are content provider networks that bring the services closer to you

## Internet structure
Tier 1 commercial ISPs are stuff like ATT, Verizon that provide coverage
Content provider networks are private networks that connect the data center to the internet
## Network Edge

Edge is the end users, the once connected to the internet

## Network Core
Multiplexing: Sharing a resource among multippe users 
	Frequency Division Multiplexing (FDM): Partition resource in frequency, each device gets a different part of the frequency band
	Time division multiplexing (TDM): Partition resource in time, the device gets access to the full band but only for a certain time
<mark style="background: #FF5582A6;">	Statistical multiplexing</mark>: Not allocate rigid resources, resources used as needed (kind of sharing)


**Fundemental question:** How is data transferred through the network?
	Circuit switching: dedicated resource allocation
	Packet switching: 
Circuit switching is when you allocate resources (either freq or time) for a communication between networks. No one else can use the resource, it is "dedicated", ineffecient for burst or anything with inactivity, like a call but good because guarenteed

Packet switching: Hosts break application layer messages into packets where the packets are interleaved between users
	Users share network and send packets, each packet uses full bandwidth 
	Packets don't have to take the same route
	Resources only used as needed

The issue with this is that the amount of packets being sent can be more than the computer can handle, packet queue becoming too long can cause congestion and delays and if the queue is full then packets are dropped
	Pros: Good for bursty, resource sharing
	Cons: Can lead to congestion


Entire packet has to arrive at router before it can be transmitted
	Called Store and forward
This begs the question, how many bits is the right number? why 1500

## Performance
Packet switching allows more users bc it doesnt consume bandwidth when not useful

Packets have a delay on end-to-end paths with 4 sources at each hop
	nodal processing ($d_{proc}$): Checks for bit errors at router, determine output link, usually <1ms
	queueing delay ($d_{queue}$): Time waiting at output link for transmission (how long a packet waits in the queue until it's sent), depends on congestion
	transmission delay ($d_{trans}$): equal to $\frac{\text{packet length}}{\text{transmission rate}}$ 
	propogation delay ($d_{prop}$): time it takes to travel through the cord, equal to $\frac{\text{Length of physical link}}{\text{Propogation speed}}$ 

Packet loss occurs if the arrival rate of packets (in bps) is more than the transmission rate (in bps) of the router
	Packets get queued to be sent and and are lost if the queue (in memory) can't hold any more

Packet queuing delay: 
	R = link bandwidth (bps)
	L = packet length (bits)
	a = average packet arrival rate (bps)
	If $\frac{Ra}{L} \approx 0$ then small delay
	If $\frac{Ra}{L} \approx 1$ then large delay
	If $\frac{Ra}{L} > 1$ then more packets arriving than can be serviced, infinite delay with packet loss


Traceroute shows the delay from the source to every router that a packet travels 
	Sends 3 packets to each router and measueres time between sent and reply

Throughput: transfer size/ time to transfer
	Essentially, information (bits, bytes) over some time unit
	Usually averaged 
	pretty much the bandwidth percieved 
	Instant throughput: rate at a given time
	Average throughput: rate over a time period

Bottleneck link is the part of the path (link) that limits the end-end throughput 
	Slowest link dominates


## IP Stack
Application: Network applications like http (send an http request)
Transport: data transfer protocols (UDP/TCP)
Network: Routing datagrams from source to destination (IP)
Link: data transfer between people on same network
Physical: bits on the wire

The application layer has the message itself
The transport layer adds a header called the segment
Network layer adds another header with the full thing called a datagram
Link layer adds the last layer called the frame

![[Pasted image 20250205124421.png]]


## 