# Python Wrangling

| Points | Category       | Author |
|--------|----------------|--------|
| **10** | General Skills | syreal |

### Description
> Python scripts are invoked kind of like programs in the Terminal... Can you run [this Python script](https://mercury.picoctf.net/static/325a52d249be0bd3811421eacd2c877a/ende.py) using [this password](https://mercury.picoctf.net/static/325a52d249be0bd3811421eacd2c877a/pw.txt) to get [the flag](https://mercury.picoctf.net/static/325a52d249be0bd3811421eacd2c877a/flag.txt.en)?

### Hints
> Get the Python script accessible in your shell by entering the following command in the Terminal prompt: `$ wget https://mercury.picoctf.net/static/325a52d249be0bd3811421eacd2c877a/ende.py`

> `$ man python`

### My Process

After downloading the files, I ran `python3 ende.py` to see what options it needed, and then ran `python3 ende.py -e flag.txt.en` with the password to get the flag.

**Flag:** `picoCTF{4p0110_1n_7h3_h0us3_ac9bd0ff}`