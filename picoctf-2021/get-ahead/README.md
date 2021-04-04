# GET aHEAD

| Points | Category         | Author    |
|--------|------------------|-----------|
| **40** | Web Exploitation | madStacks |

### Description
> Find the flag being held on this server to get ahead of the competition http://mercury.picoctf.net:34561/

### Hints
> Maybe you have more than 2 choices

> Check out tools like Burpsuite to modify your requests and look at the responses

### My Process

Upon visiting the site, we are greeted with a flash of red temporarily blinding me and reminding me of my own mortality, as well as two funny little buttons.

By the *very subtle title* we can assume that this challenge has something to do with HEAD and GET http requests.<sup id="a1">[[1]](#f1)</sup>

Knowing this, I'm going to open up inspect element on the site and navigate to the network tab. Here, whenever I send a request and receive a response, I can click on the response and examine the http request/response sent.

I click on the red button, and when I click the `index.php` response and click view source for request, I see `GET /index.php HTTP/1.1`. Okay, I do the same with the blue one and see `POST /index.php HTTP/1.1`.

Great, we know that the location these requests are going to is `/index.php`, and that `GET` and `POST` are being used as flags to change the webpage's background colour. Using [curl](https://en.wikipedia.org/wiki/CURL) (one of my goto Linux terminal tools to deal with messing around with HTTP requests and headers), I want to send a `HEAD` request to `http://mercury.picoctf.net:34561/index.php` and see if the flag is in the headers.<sup id="a2">[[2]](#f2)</sup>

When I put in `curl -I http://mercury.picoctf.net:34561/index.php`, I get:

```
HTTP/1.1 200 OK

flag: picoCTF{r3j3ct_th3_du4l1ty_8f878508}
Content-type: text/html; charset=UTF-8
```

Awesome, there's our flag!

**Flag:** `picoCTF{r3j3ct_th3_du4l1ty_8f878508}`

***

<b id="f1">1.</b> If you don't know what HTTP methods are, [check out Mozilla's docs on this.](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) [↩︎](#a1)

<b id="f2">2.</b> If you don't know what HTTP headers are, [Mozilla is all you need.](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers) [↩︎](#a2)
