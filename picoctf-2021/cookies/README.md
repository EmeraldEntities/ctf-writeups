# Cookies

| Points | Category         | Author    |
|--------|------------------|-----------|
| **40** | Web Exploitation | madStacks |

### Description
> Who doesn't love cookies? Try to figure out the best one. http://mercury.picoctf.net:29649/

### Hints
*None*

### My Process
Going to the site, we see a pretty simple cookie judging site. The title suggests this has something to do with HTTP cookies, [^1] so we'll check our cookies regularly. Let's put in `snickerdoodle`, the default cookie it suggests.

The website tells us it loves snickerdoodles cookies, and we get a browser cookie called `name` with a value of `0`. Okay, let's try `gingerbread`. The website tells us it loves gingerbread cookies, and the value swaps to `23`! What if we put in my favourite kind of cookie, `oujfa8jm4faj8dfj1`? Well, value becomes `-1` and we are given an error text.

At this point, I realized that the value must be some sort of index for the cookie, and the server must be looking at the value to determine what to display on the website. `snickerdoodle` must be `0` and some other cookie (or the flag!) must be at the end, with `-1` indicating error. Editing the value to be some insanely high number gives us `-1`, so I simply start from 0 and start manually increasing the value/index.

Sure enough, once I set the value to `18`, the flag is displayed loud and proud on the webpage. They never mention whether they like this kind of cookie or not, though.

**Flag:** `picoCTF{3v3ry1_l0v3s_c00k135_a1f5bdb7}`

[^1]: No clue what cookies are? To sum it up quickly, cookies are just a way the server can store some information for each client on a browser. The issue is, cookies can be edited client-side using an extension, so you don't want to store sensitive information on there! For an in-depth look into cookies, [check out Mozilla's docs on them](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies).