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