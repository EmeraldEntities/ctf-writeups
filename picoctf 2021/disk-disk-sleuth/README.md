# Disk, disk, sleuth!
##### 110 points
###### Forensics
###### Author: SYREAL

> Use `srch_strings` from the sleuthkit and some terminal-fu to find a flag in this disk image

Hints:
> Have you ever used `file` to determine what a file was?

> Relevant terminal-fu in picoGym: https://play.picoctf.org/practice/challenge/85

> Mastering this terminal-fu would enable you to find the flag in a single command: https://play.picoctf.org/practice/challenge/48

> Using your own computer, you could use qemu to boot from this disk!

### My Process

We're given a compressed disk image. Nice, haven't seen this kind of problem before!

After saving it (and making sure to use `gzip -d`, decompressing it as it gives us a `.gz`), we're greeted with—you guessed it—a disk image.

Normally I would have spent some time researching this or checking out the sleuthkit, but I just ended up running `strings dds1-alpine.flag.img | grep pico` first, since I figured that it must have something to do with a form of `strings`. By piping it into `grep`, I could filter out ONLY the text that I would need.

This gets me:
```
$ ffffffff81399ccf t pirq_pico_get
$ ffffffff81399cee t pirq_pico_set
$ ffffffff820adb46 t pico_router_probe
$ SAY picoCTF{f0r3ns1c4t0r_n30phyt3_a6f4cab5}
```
There's the flag!

**Flag:** `picoCTF{f0r3ns1c4t0r_n30phyt3_a6f4cab5}`