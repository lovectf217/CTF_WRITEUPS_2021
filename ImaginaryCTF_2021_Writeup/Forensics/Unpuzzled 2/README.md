# Unpuzzled 2 100 Points

# Description
Puzzler7's evil twin is hiding one more secret. Find it for us. (Note: the flag for this challenge ends with 6148}.)

Note: DO NOT stalk/OSINT puzzler7#7657. This will not help you solve this challenge, and will only lead you away from the right solution.

# Solution
This is a pretty normal osint challenge.

In last [Unpuzzled 1](https://github.com/MikelAcker/ImaginaryCTF_2021_Writeup/tree/main/Forensics/Unpuzzled%201) challenge, we have already osinted *unpuzzler7* and found his **giter** account and repo '[cyberpatriot-stuff](https://giters.com/realunpuzzler7/cyberpatriot-stuff?amp=1)' from google search.I advise you to read that challenge first if you haven't.

At the profile page, we can see a link to a website.


<img src="https://raw.githubusercontent.com/MikelAcker/ImaginaryCTF_2021_Writeup/main/Forensics/Unpuzzled%202/info1.png">

https://website.unpuzzler7.repl.co/

But there is no flag there!

<img src="https://raw.githubusercontent.com/MikelAcker/ImaginaryCTF_2021_Writeup/main/Forensics/Unpuzzled%202/info2.png">

So, I decided to check his repl profile.

But a problem is that I can't find the *search bar* in repl.

After googling,I found people asking the same problem.And,luckily I found the answer in https://replit.com/talk/ask/How-do-I-find-a-friend-on-repl/20894

So we can search him with
```
https://replit.com/@Unpuzzler7/
```

<img src="https://raw.githubusercontent.com/MikelAcker/ImaginaryCTF_2021_Writeup/main/Forensics/Unpuzzled%202/info3.png">

There are some repls but I checked the **Discord Bot** one first because it is the only one that has description.

[Discord Bot repl](https://replit.com/@Unpuzzler7/DiscordBot?v=1)

<img src="https://raw.githubusercontent.com/MikelAcker/ImaginaryCTF_2021_Writeup/main/Forensics/Unpuzzled%202/info4.png">

In the **code** tab, there is a file called *flags* but there is no flag

But,after checking all the files, I found a interesting base64 string in **keep_alive.py**.

<img src="https://raw.githubusercontent.com/MikelAcker/ImaginaryCTF_2021_Writeup/main/Forensics/Unpuzzled%202/info5.png">

```
aWN0ZntyM3BsMXRfMXNudF90aDNfcGw0YzNfdDBfc3QwcjNfczNjcjN0c18xY2IyNjE0OH0=
```

And I decoded it and found the flag
```bash
echo "aWN0ZntyM3BsMXRfMXNudF90aDNfcGw0YzNfdDBfc3QwcjNfczNjcjN0c18xY2IyNjE0OH0=" | base64 -d
ictf{r3pl1t_1snt_th3_pl4c3_t0_st0r3_s3cr3ts_1cb26148}
```

flag ```ictf{r3pl1t_1snt_th3_pl4c3_t0_st0r3_s3cr3ts_1cb26148}```
