# information
#### 10 points
###### Forensics
###### Author: SUSIE

### Description
> Files can always be changed in a secret way. Can you find the flag? [cat.jpg](https://mercury.picoctf.net/static/e5825f58ef798fdd1af3f6013592a971/cat.jpg)

### Hints
> Look at the details of the file

> Make sure to submit the flag as picoCTF{XXXXX}

### My Process
We're given this image.

![cat](https://github.com/EmeraldEntities/ctf-writeups/blob/main/picoctf-2021/information/cat.jpg?raw=true)

Normally, when I'm given an image, I immediately run `file`, `exiftool`, and `binwalk` to see what I can find. `file` and `exiftool` help me get metadata/general information about the file, and `binwalk` checks if I can extract any embedded file. With this image, we can run `exiftool` on it to obtain its metadata. Now, I expected a 10 pointer to have the flag in plaintext, but that wasn't the case in this problem. We note that the licence looks a bit strange:

`License: cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9`

Hmm... Let's run this through a Base64 decoder (my go-to decoder for long weird strings of text). That gives us `picoCTF{the_m3tadata_1s_modified}`. Nice!

**Flag:** `picoCTF{the_m3tadata_1s_modified}`