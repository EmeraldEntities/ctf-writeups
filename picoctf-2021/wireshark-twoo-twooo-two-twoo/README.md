# Wireshark twoo twooo two twoo...
#### 100 points
###### Forensics
###### Author: DYLAN

### Description
> Can you find the flag?

### Hints
> Did you really find _the_ flag?

> Look for traffic that seems suspicious.

### My Process
Hoooo boy, a wireshark one. I don't use wireshark a lot, so it'll be fun finding the flag. Also the second in the series, meaning large dump + excessive combing + irregular hiding location... not fun.

Opening up the pcapnp, we can see ~5000 packets... fun. We're given through various hints on Discord that this will be like Shark on wire 2, where the flag was hidden among the ports. Someone also deliberately mentions "Port numbers", so we'll keep an eye out for those.

Let's examine this project like how we did `Shark on Wire 2`. Looking through the streams (yes, all 900 udp streams and all 200 tcp streams), we can see udp.stream 0 has some interesting capital words sprinkled into the body. The rest is filled with garbage.

`tcp.stream 4` has interesting authorization chunk, but I'm not sure if that's necessarily suspicious. `tcp.stream 14` contains only periods and an e, which is a bit odd, and `tcp.stream 86/87` contains some sort of token or fake base64. The rest contains fake flags and super large http encoded stuff.

Now here comes the fun part of forensics: guessing! Here are some of the things I did:
- filtering by udp.stream eq 0 and looking at port numbers
	- filtering by port 443 (funnily enough, only udp stream 0 and dns calls use this)
	- filtering by `ip.src == 216.58.194.196`
	- filtering by `ip.addr == 192.168.38.104` (not helpful... about 100% of the packets originate or go to this ip)
	- filtering by `ip.addr == 216.58.194.196` 
	- subtracting packet length by data length to try and obtain an ascii (didn't work)
	- at this point i gave up and cried	
- filtering by tcp.stream 14
	- filtering by `ip.addr == 192.168.38.105` (this started to look promising... a lot of black and red, but nothing conclusive)
- filtering by tcp.stream 86
	- filtering by a crap ton of different IPs... nothing fruitful came up.

At this point it's been a day, so I go onto Discord for more tips. One thing that pops out to me is DNS, so I load up Wireshark to check (I used NetworkMiner, but I'll use Wireshark for the sake of this writeup). Filtering by DNS port (53) using `udp.port == 53`, we see:

![Interesting DNS...](https://github.com/EmeraldEntities/ctf-writeups/blob/main/picoctf-2021/wireshark-twoo-twooo-two-twoo/writeup-files/dns1.png?raw=true)

Okay... Interesting. One thing that caught my eye is the filler text before `reddshrimpandherring.com`. At a rudimentary glance I thought it was Base64, and tried to decode it, but it spat out nothing. How about we check out the rest of the filtered packets? Looking at the bottom, we see:

![Interesting bottom...](https://github.com/EmeraldEntities/ctf-writeups/blob/main/picoctf-2021/wireshark-twoo-twooo-two-twoo/writeup-files/dns2.png?raw=true)

Ooh! At the very last few DNS packet, we see `fQ==` appended before `reddshrimpandherring.com`. `==` is a padding used at the end of Base64—we may have seen a lot of red herrings involving Base64, but let's try and hop down this rabbit hole.

Let's figure out what's different from this packet and the rest. I'm thinking that only a few DNS packets with this filler text at front will decode into a flag. Looking at the other fields, we see that it goes to `18.217.1.57`. Strange, most of the other DNS calls went to `192.168.38.104`. Let's filter based on only this, using `udp.port == 53 && ip.dst == 18.217.1.57`.

![Interesting filtered files...](https://github.com/EmeraldEntities/ctf-writeups/blob/main/picoctf-2021/wireshark-twoo-twooo-two-twoo/writeup-files/dns3.png?raw=true)

NICE! That looks like a reasonable amount of packets. Let's extract each of the padding text in front of `reddshrimpandherring.com`, and run it through a Base64 decoder.

`cGljb0NU.reddshrimpandherring.com`
`RntkbnNf.reddshrimpandherring.com`
`M3hmMWxf.reddshrimpandherring.com`
`ZnR3X2Rl.reddshrimpandherring.com`
`YWRiZWVm.reddshrimpandherring.com`
`fQ==.reddshrimpandherring.com`

`cGljb0NURntkbnNfM3hmMWxfZnR3X2RlYWRiZWVmfQ==` turns into `picoCTF{dns_3xf1l_ftw_deadbeef}`

**Flag:** `picoCTF{dns_3xf1l_ftw_deadbeef}`
