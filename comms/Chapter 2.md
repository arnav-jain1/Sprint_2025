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

