1. a
	a) Various factors influence the rate of an ethernet cable including but not limited to: the material used inside of the cable, the length of the cable, the design (structure of internals) of the cable, frequency, and much more 
	Sources: https://www.telco-data.com/blog/cat-cables/ https://tripplite.eaton.com/products/ethernet-cable-types
	b) 
		802.11 was the original developed in 1997 and supported speeds up to 1Mbps, it is defunct
		802.11a was developed in 1999 and supported speeds up to 54Mbps, was a slight upgrade
		802.11b was also developed in 1999 and used the 2.4Ghz band. It was much cheaper and had a max speed of 11Mbps. The issue was that it is unregulated to it has interference from other devices using the same band
		802.11g was developed in 2003 and uses the same band. It is also backwards compatible. It has max speeds of 54Mbps (Wifi 3)
		802.11n was developed in 2009 (Wifi 4) and has a max speed of 600Mbps while also having a longer range due to MIMO technology (multiple antennas and signals). It is more expensive though
		802.11ac was developed in 2014 (WiFi 5) and has a new 5Ghz band with speeds that are more than 1Gbps. It keeps the 2.4Ghz band for backwards compatibility 
		802.11ax (Wifi 6) is the fastest and is up to 10x faster than Wifi 5. It also operates on both freq
		https://www.fs.com/blog/80211-wireless-standards-explained-35.html
	c) Wired networks are generally faster with higher bandwidth but usually have less devices connected (wiring becomes a pain) but are usually more reliable. A wired network is like a server that needs the ultrafast and reliable speeds. Wireless networks usually have many devices connected at once and they are much easier to set up. An example being a school network where guests and students want to connect
1. 

2. 
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