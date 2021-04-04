# Static ain't always noise

| Points  | Category       | Author |
|---------|----------------|--------|
| **20**  | General Skills | syreal |

### Description
> Can you look at the data in this binary: [static](https://mercury.picoctf.net/static/0f6ea599582dcce7b4f1ba94e3617baf/static)? This [BASH script](https://mercury.picoctf.net/static/0f6ea599582dcce7b4f1ba94e3617baf/ltdis.sh) might help!

### Hints
*None*

### My Process
Now, I'm assuming you're supposed to use the provided bash script to find the flag, but what I did was use the command `strings static | grep pico`. `strings` is a Linux command-line tool useful for getting the string characters into a file, and `grep` takes in text and only returns strings that match the provided text (which in this case is pico). This lets us find the flag.

**Flag:** `picoCTF{d15a5m_t34s3r_6f8c8200}`
