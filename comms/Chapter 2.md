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