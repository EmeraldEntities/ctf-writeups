# Milkslap
##### 200 points
###### Forensics
###### Author: JAMES LYNCH

> 🥛

Hints:
> Look at the problem category

### My Process

The milk actually takes us to a webpage, http://mercury.picoctf.net:5013/. When we access it we see that it's set up just like [eelslap](http://eelslap.com/) (actually, this challenge was inspired by it). Let's take the hint's advice and treat this as a forensics problem, meaning no looking for robots, looking too closely at html, etc etc etc. 

The first thing I did was try to find the image for the milkslap, and to do that, I opened up inspect element and looked at the *Sources* tab. With that, I was able to find a big 17 MB image file to download... Fun!

It turns out this image file is every single frame in the milkslap page. Makes sense, I guess.

Great, the image is downloaded. Here comes the hard part of forensics—guessing until you get it right. I hear that many teams had to guess many many stego tools to see if it produced the flag. Luckily, I was given a hint by my team member and knew I had to use Stegsolve to view it. Stegsolve is a very useful jar file for any stego image since it applies a variety of colour filters and basically renders manual colour adjustments to find flags obsolete, and I would recommend [picking it up](https://github.com/zardus/ctf-tools/blob/master/stegsolve/install).

After cracking it open in Stegsolve, I looked through every filter until I found one that looked weird—`Blue plane 0`. It was pitch black with some white text at the top, but sadly the Stegsolve UI blocked it. To get around this, I simply extracted the preview, applied only the Blue 0 bit plane, and looked at the text—and bam!

![milk slapping gives flags!](https://github.com/EmeraldEntities/ctf-writeups/blob/main/picoctf%202021/milkslap/writeup-files/slappedmilk.png?raw=true)

There's the flag!

**Flag:** `picoCTF{imag3_m4n1pul4t10n_sl4p5}`