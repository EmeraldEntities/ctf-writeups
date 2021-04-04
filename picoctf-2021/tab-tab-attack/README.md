# Tab, Tab, Attack

| Points  | Category       | Author |
|---------|----------------|--------|
| **20**  | General Skills | syreal |

### Description
> Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: [Addadshashanammu.zip](https://mercury.picoctf.net/static/9689f2b453ad5daeb73ca7534e4d1521/Addadshashanammu.zip)

### Hints
> After \`unzip\`ing, this problem can be solved with 11 button-presses...(mostly Tab)...

### My Process
After downloading and using `unzip` to unzip the file, we see:
```
Archive:  addadshashanammu.zip
   creating: Addadshashanammu/
   creating: Addadshashanammu/Almurbalarammi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/
  inflating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet
```

Just save yourself some time and mental anguish and use tab to complete the file... Or copy and paste `Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/`. Either way, just run `./fang-of-haynekhtnamet` to get:

`*ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_2bcfb2ab}`

There's the flag!

**Flag:** `picoCTF{l3v3l_up!_t4k3_4_r35t!_2bcfb2ab}`