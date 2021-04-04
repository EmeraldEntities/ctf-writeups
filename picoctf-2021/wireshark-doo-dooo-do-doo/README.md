# Wireshark doo dooo do doo..

| Points | Category  | Author |
|--------|-----------|--------|
| **50** | Forensics | Dylan  |

### Description
> Can you find the flag? [shark1.pcapng](https://mercury.picoctf.net/static/81c7862241faf4a48bd64a858392c92b/shark1.pcapng).

### Hints
*None*

### My Process
Yay, a wireshark! My... "favourite".

After opening the provided `pcapng` with Wireshark, we're greeted with a load of packages... yay.

Since this is the first Wireshark challenge and only worth 50 points, I figure this might be a "follow the streams" kind of challenge. Wireshark streams collect related network packets, sorts them, and lets you view their data as a whole. Usually for early, low point Wireshark challenges, the flag is generally hidden somewhere in a stream. Let's just check all the streams as usual. I'll start examining TCP streams by right clicking a TCP packet > follow stream > TCP (alternatively, you can type `tcp.stream eq 0` into the Wireshark filter bar).

Oh, what's this? In `tcp.stream eq 5`, there appears to be an encrypted sentence... and it looks like a flag?

![Interesting traffic...](https://github.com/EmeraldEntities/ctf-writeups/blob/main/picoctf-2021/wireshark-doo-dooo-do-doo/writeup-files/pictureshark-doo-doooo-dooo-doo.png?raw=true)

Let's run it through a ROT13 cipher since it looks like a simple shift cipher.

`Gur synt vf cvpbPGS{c33xno00_1_f33_h_qrnqorrs}` turns into `The flag is picoCTF{p33kab00_1_s33_u_deadbeef}`

Nice! A good Wireshark warmup and refresher for what to come next... [Wireshark 2](../wireshark-twoo-twooo-two-twoo/)... \**shudders*\*

**Flag:** `picoCTF{p33kab00_1_s33_u_deadbeef}`
