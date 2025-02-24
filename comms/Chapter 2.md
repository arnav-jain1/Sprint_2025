# Application layer
Write programs that run on network edge (not network core like switches)
	Allows for faster development because you don't have to worry about any other layer
Programs will run on different end systems 

Seperates the client and server (client-server architecture)

Server:
	Always on
	Permanent IP address (so that when you try to access it it will always stay the same)
	Provides requested service to the client

Client 
	Starts the communication with the server
	Requests service 
	Implemented in the browser


Peer to peer
	No server thats always on
	Instead 2 end systems will communicate directly
	Peers request service from other peers and peers provide service to other peers
	Self-scalability: new peers increase capacity and also demand

Process: 
	Program running within a host 
	Within the same host, processes communicate via IPC
	Different hosts use application layer protocols 
	Client process starts communication and server process waits to be contacted

Sockets: 
	Process sends/recieves messages via sockets
	Its like a door, sending process sends it out the door and then its handled

Process needs to have identifier including IP address, port number, process id

Application layer protocol identifies:
	Types of messages exchanged (request, response)
	Message syntax (how its formatted)
	message semantics (meaning of the format)
	rules for 


Performance requirements:
	Some can tolerate loss while others cant
	Low delay
	Minimum throughput
	Encryption

# Transport protocol 
Transmission control protocol (TCP) and User Datagram Protocol (UDP)

## TCP
**Connection oriented: setup between client and server**
Reliable packet transport: No-loss, in-order delivery
Flow contro: Sender doesn't overwhelm the reciever
Congestion control: Sender wont overwhelm the network
No guarantees on delay and throughput

## UDP
Designed for shorter packets for when it doesn't matter as much if one packet is dropped
Unreliable data transfer: No security, reliability (no confirmation packet reached), timing
Quick and dirty
Setup is not required 


## HTTP
APplication layer protocol 
Client/server model
	Client: Browser that requests, receives, and displays web objects
	server: sends objects in response to the requests (with HTTP)
HTTP request followed by HTTP response 

Uses TCP
	Client initiates connection (creates socket) to server
	Server accepts TCP connection from client
	Once established, allowed to send messages between the 2

Non-persistent:
	HTTP initiates TCP connection to the server on port 80
	Server then accepts the connection 
	HTTP then sends the HTTP request method (with url) to the socket and says that it wants an object.
	Server recieves the message, creates the response message with the requested object and then sends the message into the socket
	Server then closes the connection
	Client then accepts the response 
	Repeated until done
	RTT: Time for packet to travel from client to server to client 
	HTTP response time: 1 RTT to start connection, 1 for HTTP request, File transmission time
	So 2RTT + file transmission 
	Also has OS overhead
	Sometimes multiple connections for parallelization


Persistent:
	Default
	TCP connection opened and server continoususly sends objects to the client via TCP, connection does not get closed
	1 RTT for all objects (so half of non persistent)



<mark style="background: #FF5582A6;">Other stuff that I dont have </mark>

POST method:
	Info from the client being sent to server
GET
	get data from server to user
Head: 
	Request headers (like the top part of a regular request)
Put:
	Upload the file to the server (replace the file at the url with body of post)


HTTP response:
	The first line is the status line
	After that is the header lines which have connection info 
		Like server, how long for the connection, content type, etc
	Then is the body of the message

HTTP status codes
	200: OK success
	301: Moved permanently, new location in this message
	400: Bad request (not understood)
	404: Not found, requested file not on the server
	505: HTTP version not supported

Cookies:
	Client has "cookie file" and amazon creates an ID for the user in the database
	The server tells the user to set the cookie to that same number
	Then when sending more info we can send the cookie number to keep track (state) of the user
	When access 1wk later, the same number still works
	3rd party services exist to connect cookies between amazon, google, etc


HTTP cookies
	Can be used for authorization, saving shopping carts, recommendations, ads

The challenge with cookies is hw to keep the state

Web caches (proxy servers)
	Installed by ISP but can happen at every layer (from browser to ISP, to company)
	Goal is to satisfy the client request without having to reach the origin server
	Browser first goes to web cache instead of origin
		if the object is there, then return the object. 
		If not, cache request from origin server and then return it to the client
	The cache is both the client and the server
	Reduces response time (cache is closer) and traffic

The cache is "closer" to the client and decreases traffic to distant servers
Links are also expensive while RAM is cheap (so links bottleneck) so it is cheaper to get a cache

Conditional GET:
	Its a GET request but the server will only respond with an object if the file has been modified since a given date. If it hasn't then it will send a 304 not modified


One issue with HTTP/1 is that all requests are in order so bigger objects kind of block other ones
	![[Pasted image 20250211101524.png]]

HTTP/2 breaks the objects into frames where the frames are interleaved
	![[Pasted image 20250211101547.png]]
	HTTP/2 also increased flexibility at server by making the server being able to send objects even if it is unrequested

HTTP/3
	Decrease the delay in multi object requests
	Changes on transport layer instead of application layer, runs on QUIC
	Also adds security, object error, and congestion control


Email:
	3 major components: user agent, mail servers, simple mail transfer protocol
	User agent: The mail reader
		Compose, edit, read, and send messages
		messages stored on server
		Outlook, GMail
	Mail servers:
		Mailbox has incoming messages for the user
		Message queue: queue of messages that are waiting to be sent
		SMTP protocol: Protocol between mail "servers" to send messages
			Client is the ending "server", server is the recieving "server"
SMTP - RFC 5231
	Uses TCP (doesnt want to lose info), port 25
	Direct trasnfer: Sending "server" (client) sends to recieving server
	3 phases: Handshake/greeting, transfer message, closure
	Commands/response (like HTTP) in ascii with status codes and phrases
ASCII is human readable

Scenario: Alice sends email to bob
	Alice creates an email using user agent. 
	This is sent to her mail server where it is queued
	Client side of SMTP opens TCP with Bob's mail server 
	Client sends message over TCP
	Bob's mail server puts it in his mailbox 
	Bob gets his UA to read the message
	![[Pasted image 20250211103515.png]]
SMTP
	More like a push than a pull (HTTP)
	Both HTTP and SMTP use ASCII
	Multiple objects in same (multipart) message
	persisetent connections

Message format: 
	Header lines with subject, to, from, etc
	Body with message


## DNS Domain name system
When typing in a url we dont type the IP address we type a name like "google.com"  how do we know it is google's IP
Thats where DNS comes in
	Distributed database: Hierarchy of name servers
	Application layer protocols: Name servers have to communicate to resolve names (convert from name to IP) 
	Core 

![[Pasted image 20250219191604.png]]
	For example, if you are looking for www.Amazon.com, you first query the .com DNS servers who then give you amazon.com then you ask for IP of www.amazon.com 

Iterated query: 
	If you query and they don't know, then they tell you where to ask
	![[Pasted image 20250219191752.png]]
	Example: You are at nyu requesting for umass
		You First go to the local DNS which asks the root. The root tells you to ask TLD which twlls you to go to umass which gives you the IP and then you send it back

Recursive query: Instead of responding with where to look, the DNS searches and this becomes recursive
	![[Pasted image 20250219191931.png]]
	Puts a lot of load on the root tho
	Root talks to TLD which talks to umass which goes all the way back up

You don't want a centralized because of it being a pain to scale, single point of failure, volumn, etc.

DNS Root name:
	The official last resort servers
	Super important (ICANN
	![[Pasted image 20250219192316.png]]

## TLD and authoritative servers
Top level domain (TLD): responsible for .com, .org, etc. as well as country ones like .ca, .in, etc

authoritative DNS: Org's own DNS for hostname to IP mappings for named hosts
	Maintained by org or ISP

Local DNS:
	Not in heirarchy 
	Each ISP has one
	When making a query, goes to ISP local DNS first (like a proxy)

### Caching
Once a mapping is learned by a DNS it is saved into memory (cached) for faster lookup
	The entries dissappear after some time
	Root not often visited
Issue is that cached entries may be out of date


## DNS Protocol 
DNS query and reply have the same format 
	![[Pasted image 20250219195358.png]]
	Header 
		16 bit query ID with message and response having the same one
		Flags for more info (like message or reply, recursion, etc)
	Information about the query itself


DNS services:
	hostname to IP 
	Host (and mail server) aliasing 
	Load distribution

DNS Records (how it is stored)
	distributed database with resource records (RR)
	Format: `(name, value, type, ttl)`
		Type=A: name is hostname and value is IP
		Type=CNAME: name is an alias for the real name, value is real name (ibm.com -> backup2.ibm.com)
		Type=NS: name is domain and value is hostname of authoritative domain
		Type=MX: Value is the name of the mailserver 
To register a new name, it has to be registered at DNS registrar where you provide names and  IP addresses of authoritative name server
	From there, the registrar stores it in the respective TLD server 
Can also create a type A record (local DNS) by inserting a type A RR with name of the website and value of the IP

Example: Alice wants to access www.networkutopia.com
	Her host sends query to local DNS which contacts TLD (may also have to contact root)
	The TLD sends a reply to the local DNS with all of the records that match
	Lets say it was type NS, the local then sends it to the authoritative DNS asking for the type A record which the authoritative will then send the right IP of which Alice connects to 

DNS security: 
	DDoS attacks bombard the DNS with traffic (not successful because caching)
	Can also send bogus requests to DNS which makes it cache bogus stuff which makes it slower
	You can also bombard TLD servers which is more common and potentially more dangerous
	Can also intercept DNS queries to get info 

## P2P review
No always-on server
End systems directly communicate 
Peers request info (service) from other peers who then provide that service
	New peers bring more demands but also increase the service capacity 
Peers are intermittently connected (complex management)
Like torrenting 

## File distrib

### Client server
How long does it take to distribute a file of size *F* from one server to *N* people

Must upload N copies of the file
	Time for sending 1 copy is $F/u_{s}$ so for N files is $NF/u_{s}$ 
Client has to download 1 copy of size F
	Time is $F/d_{min}$ where d min is the minimum client download rate to $F/d_{max}$

So time to distribute is $\text{max}(\frac{NF}{u_{s}}, \frac{F}{d_{min}})$ 

### P2P
Server: Needs to upload one time: $F/u_{s}$
Client: Needs to download one time $F/d_{min}$ 