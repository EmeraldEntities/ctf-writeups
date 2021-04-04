# Wave a flag

| Points | Category       | Author |
|--------|----------------|--------|
| **10** | General Skills | syreal |

### Description
> Can you invoke help flags for a tool or binary? [This program](https://mercury.picoctf.net/static/f95b1ee9f29d631d99073e34703a2826/warm) has extraordinarily helpful information...

### Hints
> This program will only work in the webshell or another Linux computer.

> To get the file accessible in your shell, enter the following in the Terminal prompt: `$ wget https://mercury.picoctf.net/static/f95b1ee9f29d631d99073e34703a2826/warm`

> Run this program by entering the following in the Terminal prompt: `$ ./warm`, but you'll first have to make it executable with `$ chmod +x warm`

> -h and --help are the most common arguments to give to programs to get more information from them!

> Not every program implements help features like -h and --help.

### My Process

After downloading the file, I ran `./warm -h` on WSL as suggested by the description and got this message:

`Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_f0668f62}`

There's the flag. I admit, I got a bit attached to the program in the second it took to run the command.

**Flag:** `picoCTF{b1scu1ts_4nd_gr4vy_f0668f62}`