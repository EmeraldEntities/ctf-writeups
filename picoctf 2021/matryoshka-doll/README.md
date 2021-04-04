# Matryoshka doll
#### 30 points
###### Forensics
###### Author: SUSIE/PANDU

### Description
> Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](https://mercury.picoctf.net/static/b6205dd933ec01c022c4e6acbdf11116/dolls.jpg)

### Hints
> Wait, you can hide files inside files? But how do you find them?

> Make sure to submit the flag as picoCTF{XXXXX}

### My Process
We're given this image:

![dolls](https://github.com/EmeraldEntities/ctf-writeups/blob/main/picoctf%202021/matryoshka-doll/dolls.jpg?raw=true)

We're told that there are files inside this png... sounds like a `binwalk` moment!

using `binwalk -e dolls.jpg`, we can extract the hidden files inside this file. This gives us another png that contains another png that contains another png that contains another png that finally gives us our `flag.txt` containing our flag!

**Flag:** `picoCTF{4f11048e83ffc7d342a15bd2309b47de}`
