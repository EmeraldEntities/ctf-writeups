# Trivial Flag Transfer Protocol

| Points | Category  | Author |
|--------|-----------|--------|
| **90** | Forensics | Danny  |

### Description
> Figure out how they moved the [flag](https://mercury.picoctf.net/static/fb24ddcfaf1e297be525ba7474964fa5/tftp.pcapng).

### Hints
> What are some other ways to hide data?

### My Process
Another Wireshark problem? Oh pico devs, you're spoiling us...

After opening the provided `pcapng` with Wireshark, we're greeted with some packets. More importantly, we're greeted with a ton of TFTP packets... makes sense, since this problem is called (T)rivial (F)lag (T)ransfer (P)rotocol.

TFTP (Trivial File Transfer Protocol) is a protocol designed to transfer files, and sends them unencrypted onto the network. Let's go to Wireshark -> Home -> Export Objects -> TFTP and see if we can recover any of these objects.

![Objects!](https://github.com/EmeraldEntities/ctf-writeups/blob/main/picoctf-2021/trivial-flag-transfer-protocol/writeup-files/tftp.png?raw=true)

After exporting these objects, let's inspect them. `instructions.txt` and `plan` look like a good start... I bet you `plan` is just a `txt` but not labelled as one.

`GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA`

`VHFRQGURCEBTENZNAQUVQVGJVGU-QHRQVYVTRAPR.PURPXBHGGURCUBGBF`

Wonderful. Let's run this through a ROT13 decoder, since it's a common cipher and I suspect this is encoded with that.

`TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN`

`IUSEDTHEPROGRAMANDHIDITWITH-DUEDILIGENCE.CHECKOUTTHEPHOTOS`

There we go! This looks like a conversation between two parties about disguising the flag. One thing I notice is that the phrase `DUEDILIGENCE` follows a dash. That's an interesting way to put it, but let's put it away in our brainholes for now and look at `program.deb`.

After extraction it, you'll see this program is actually Steghide! Steghide is another fairly popular stego tool used for disguising, and yes, extracting, files from images. We can assume that Steghide was used to hide a file in an image. Two problems though—which image, and what's the password?

This is where I began to massively overthink. I focused in on `picture2.bmp` because it looked SIGNIFICANTLY larger than the rest (35mb to 3mb), but this was a massive mistake. I tried variations of `DUEDILIGENCE` on Steghide trying to extract it and nothing worked. I tried ignoring Steghide and running `binwalk` or other stego tools. Nothing worked.

Finally, I resorted to creating brute-force applications to test all three pictures at the same time. After finding this [excellent steghide brute-force repository by Va5c0](https://github.com/Va5c0/Steghide-Brute-Force-Tool) (hope I didn't violate the license oops), I used the code as a guide to write code to brute force every file with a txt of potential passwords I brainstormed...

```python
def Steg_brute():
    dicc = "potential_passwords.txt"
    ifile = "picture2.bmp"
    
    nlines = len(open(dicc).readlines())
    print("brute forcing")
    with open(dicc, 'r') as passFile:
        for line in passFile.readlines():
            password = line.strip('\r\n')
            lpassword = password.lower()
            test("picture1.bmp", password)
            test("picture1.bmp", lpassword)
            test("picture2.bmp", password)
            test("picture2.bmp", lpassword)
            test("picture3.bmp", password)
            test("picture3.bmp", lpassword)
            
def test(ifile, password):
    ofile = ifile.split('.')[0] + "_flag.txt"
    r = commands.getoutput("steghide extract -sf %s -p '%s' -xf %s" % (ifile, password, ofile))
    print(color.INFO + "testing " + ifile)
    print(color.BLUE + password)
    print(color.FAIL + r)
    if not "could not extract" in r:
        print(color.GREEN + "\n\n " + r + color.ENDC)
        print("\n\n [+] " + color.INFO + "Information obtained with password:" + color.GREEN + " %s\n" % password + color.ENDC)

Steg_brute()
```

... and presto.

![Blessing!](https://github.com/EmeraldEntities/ctf-writeups/blob/main/picoctf-2021/trivial-flag-transfer-protocol/writeup-files/tftp2.png?raw=true)

Turns out all along that the password was really `DUEDILIGENCE`, but it was in `picture3.bmp`! Well, now that we decoded the flag, we can finally open up `picture3_flag.txt` and get our well-deserved flag, as well as a good lesson on never to... [tunnel vision](../tunn3l-v1s10n/).

**Flag:** `picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}`
