3. 
	a) A circuit switching network dedicates a physical path between the source and the destination. The entire bandwidth is reserved. Packet switching is when the data is split up into "packets" where the packets are all traveling independent of one another but all end at the same point. Packet switching is better for more bursty traffic where there are periods of nothing happening because resources aren't being wasted. It is worse when it gets overwhelmed because the packets get queued which delays their arrival and then packets can get lost. Circuit switching on the otherhand will consume resources when not busy but the pro is that you are guaranteed latency because it will take a certain amount of time for the data to travel that route 
	Source: https://apposite-tech.com/packet-switching-vs-circuit-switching/
	b) The network edge refers to the endpoints of a network. The network edge consists of devices that want to connect with and use the internet. Examples include my computer, a smart fridge, my phone, etc. The network core is how data is passed and includes the infrastructure and middlepoints needed to connect 2 edge devices. This includes intermediary servers to pass packets (like CDNs), routers, firewalls, network towers, etc.
4. (Assumes KiloBITS not kiloBYTES) 25Kb = .025 Mb
	a) .025 / 50 Mbps = .0005 seconds = .5ms
	b) .025 / 100 Mbps = .00025 seconds = .25ms 
	c) .25+.5 = .75ms
5. 
	a) When circuit switching, each user gets a "slice" of the bandwidth. Since each user needs 2Mbps and 20Mbps is the bandwidth of the link, then 20/2 = 10 users at once, maximum
	b) If there are 20 users and each user is active 25% of the time, then P(X=20) = $(.25)^{20} \approx 9.9 * 10^{-11}\%$  
	c) This is a binomial distribution so formula: $$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$ Here we want P(X > 10) so sum of P(X=11), P(X=12), ... P(X=20). This is equivalent to $$P(X > 10) = \sum_{k=10}^{20} \binom{20}{k} .25^{k} .75^{20-k} = .00394$$ so, $\approx .394\%$ 
5. 
	![[Pasted image 20250129135642.png]]
	a) yes it reached with 18 total hops
	b) `sudo traceroute -I ee.stanford.edu -q 10`