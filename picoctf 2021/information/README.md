# information
##### 10 points
###### Forensics
###### Author: SUSIE

> Files can always be changed in a secret way. Can you find the flag?

Hints:
> Look at the details of the file

> Make sure to submit the flag as picoCTF{XXXXX}

### My Process
We're given this image.

![cat](https://github.com/EmeraldEntities/ctf-writeups/blob/main/picoctf%202021/information/cat.jpg?raw=true)

After downloading, we can run `exiftool` on it to obtain metadata. We note that the licence looks a bit strange:

`License: cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9`

Hmm... Let's run this through a Base64 decoder (my go-to decoder for long weird strings of text). That gives us `picoCTF{the_m3tadata_1s_modified}`. Nice!

**Flag:** `picoCTF{the_m3tadata_1s_modified}`