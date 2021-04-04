# Obedient Cat

| Points  | Category       | Author |
|---------|----------------|--------|
| **15**  | General Skills | syreal |

### Description
> There is a nice program that you can talk to by using this command in a shell: `$ nc mercury.picoctf.net 21135`, but it doesn't speak English...

### Hints
> You can practice using netcat with this picoGym problem: [what's a netcat?](https://play.picoctf.org/practice/challenge/34)

> You can practice reading and writing ASCII with this picoGym problem: [Let's Warm Up](https://play.picoctf.org/practice/challenge/22)

### My Process

Running the netcat gives you this:<sup id="a1">[[1]](#f1)</sup> 

```
112
105
99
111
67
84
70
123
103
48
48
100
95
107
49
116
116
121
33
95
110
49
99
51
95
107
49
116
116
121
33
95
97
102
100
53
102
100
97
52
125
10
```

Putting that ASCII into CyberChef `From Charcode` with a base of `10` with delimiter set as `Line feed` gives us the flag.[^1]

**Flag:** `picoCTF{g00d_k1tty!_n1c3_k1tty!_afd5fda4}`

***

<b id="f1">1.</b> In case you still don't know, [Wikipedia](https://en.wikipedia.org/wiki/Netcat) has a good article about whatever the heck a netcat is. [↩︎](#a1)