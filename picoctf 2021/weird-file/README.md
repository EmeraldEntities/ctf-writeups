# Weird File
#### 20 points
###### Forensics
###### Author: THELSHELL

### Description
> What could go wrong if we let Word documents run programs? (aka "in-the-clear").

### Hints

### My Process

We're given a word document. Opening it up gives us this document.

![word](https://github.com/EmeraldEntities/ctf-writeups/blob/main/picoctf%202021/weird-file/writeup-files/macaroni1.png?raw=true)

Cool. Word has something called macros, which are kinda like scripts that people can set up to run tasks. I'm assuming this is what the description means by "run programs". Let's check the macros:

![macro time](https://github.com/EmeraldEntities/ctf-writeups/blob/main/picoctf%202021/weird-file/writeup-files/macaroni2.png?raw=true)

Awesome. Let's decode the Base64 which should give us our flag.

`cGljb0NURnttNGNyMHNfcl9kNG5nM3IwdXN9` becomes `picoCTF{m4cr0s_r_d4ng3r0us}`

**Flag:** `picoCTF{m4cr0s_r_d4ng3r0us}`