# Ancient History
#### 10 points
###### Web Exploitation
###### Author: MADSTACKS

### Description
> I must have been sleep hacking or something, I don't remember visiting all of these sites... http://mercury.picoctf.net:46715/ (try a couple different browsers if it's not working right)

### Hints
> What kind of information can JavaScript modify?

> Don't rely on viewing the list all at once in your browser, sometimes the browser doesn't show all the flag characters. So instead, go through them one at a time. If that doesn't work, then you can try a totally different approach by digging around until you find the windows to the past.

### My Process
The website brings us to a site that seems to say "Hello World". Judging by the description, I'm assuming this was supposed to activate some sort of "time travel" feature for me to browse through and find the flag. Unfortunately, the cool feature didn't work for me, so I had to go into the source code of the website and examine the script. 

At the start, the script looked mighty scary and obfuscated (and I don't like obfuscation), but one glance through and you'll see:

![wacky script](https://github.com/EmeraldEntities/ctf-writeups/blob/main/picoctf%202021/ancient-history/writeup-files/herstory.png?raw=true)

It looks like the flag just goes in a descending manner, letter by letter. Nice! We can just assemble that.

**Flag:** `picoCTF{th4ts_k1nd4_n34t_53c701d9}`