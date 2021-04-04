# Trivial Flag Transfer Protocol
#### 90 points
###### Forensics
###### Author: DANNY

### Description
> Figure out how they moved the [flag](https://mercury.picoctf.net/static/fb24ddcfaf1e297be525ba7474964fa5/tftp.pcapng).

### Hints
> What are some other ways to hide data?

### My Process
Another Wireshark problem? Oh pico devs, you're spoiling us...

After opening the provided `pcapng` with Wireshark, we're greeted with some packets. More importantly, we're greeted with a ton of TFTP packets... makes sense, since this problem is called (T)rivial (F)lag (T)ransfer (P)rotocol.

TFTP (Trivial File Transfer Protocol) is a protocol designed to transfer files, and sends them unencrypted onto the network. Let's go to Wireshark -> Home -> Export Objects -> TFTP and see if we can recover any of these objects.

![Objects!](https://github.com/EmeraldEntities/ctf-writeups/blob/main/picoctf%202021/trivial-flag-transfer-protocol/writeup-files/tftp.png?raw=true)

After exporting these objects, let's inspect them. `instructions.txt` and `plan` look like a good start... I bet you `plan` is just a `txt` but not labelled as one.

`GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA`

`VHFRQGURCEBTENZNAQUVQVGJVGU-QHRQVYVTRAPR.PURPXBHGGURCUBGBF`

Wonderful. Let's run this through a ROT13 cipher, since I suspect it's encrypted with that.

`TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN`

`IUSEDTHEPROGRAMANDHIDITWITH-DUEDILIGENCE.CHECKOUTTHEPHOTOS`

There we go! This looks like a conversation between two parties about disguising the flag. One thing I notice is that `DUEDILIGENCE` follows a dash. That's an interesting way to put it... let's look at `program.deb` now.

Once you extract it, you'll see this program is actually Steghide! Steghide is another fairly popular stego tool used for disguising, and yes, extracting, files from images. We can assume that Steghide was used to hide a file in an image. Two problems though—which image, and what's the password?

This is where I began to massively overthink. I focused in on `picture2.bmp` because it looked larger, but this was a massive mistake. I tried variations of `DUEDILIGENCE` on Steghide trying to extract it and nothing worked. I tried ignoring Steghide and running `binwalk` or other stego tools. Finally, I resorted to writing/looking up brute-force applications to test all three pictures at the same time... and presto.

![Blessing!](https://github.com/EmeraldEntities/ctf-writeups/blob/main/picoctf%202021/trivial-flag-transfer-protocol/writeup-files/tftp2.png?raw=true)

Turns out all along that the password was really `DUEDILIGENCE`, but it was in `picture3.bmp`! Well, now that we solved it, we can finally open up `picture3_flag.txt` and get our well-deserved flag.

**Flag:** `picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}`
