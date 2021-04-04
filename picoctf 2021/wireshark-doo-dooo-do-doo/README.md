# Wireshark doo dooo do doo...
#### 50 points
###### Forensics
###### Author: DYLAN

### Description
> Can you find the flag? [shark1.pcapng](https://mercury.picoctf.net/static/81c7862241faf4a48bd64a858392c92b/shark1.pcapng).

### Hints
*None*

### My Process
Yay, a wireshark! My... "favourite".

After opening the provided `pcapng` with Wireshark, we're greeted with a load of packages... yay.

Since this is the first wireshark challenge and only worth 50 points, I figure this might be a "follow the streams" kind of challenge. Let's just check all the streams as usual. I'll start with TCP streams.

Oh, what's this? On `tcp.stream eq 5`, there appears to be an encrypted something... and it looks like a flag?

![Interesting traffic...](https://github.com/EmeraldEntities/ctf-writeups/blob/main/picoctf%202021/wireshark-doo-dooo-do-doo/writeup-files/pictureshark-doo-doooo-dooo-doo.png?raw=true)

Let's run it through a ROT13 cipher since it looks like a simple shift cipher.

`Gur synt vf cvpbPGS{c33xno00_1_f33_h_qrnqorrs}` turns into `The flag is picoCTF{p33kab00_1_s33_u_deadbeef}`

Nice! A good warmup.

**Flag:** `picoCTF{p33kab00_1_s33_u_deadbeef}`
