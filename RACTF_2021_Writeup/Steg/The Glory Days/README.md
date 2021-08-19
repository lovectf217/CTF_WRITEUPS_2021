# The Glory Days 250 points

# Description
My friend sent me [this audio file](https://github.com/MikelAcker/RACTF_2021_Writeup/blob/main/Steg/The%20Glory%20Days/download.midi?raw=true), I'm sure I recognise it but I think he's tweaked it to hide a message somewhere. Can you take a look?

# Solution
I loaded the given [MIDI](https://en.wikipedia.org/wiki/MIDI) file in [Audacity](https://www.audacityteam.org/) program.

<img src="https://raw.githubusercontent.com/MikelAcker/RACTF_2021_Writeup/main/Steg/The%20Glory%20Days/info1.png">

I couldn't see any interesting things there.

So, I *resized* the *track* to look deeper!

<img src="https://raw.githubusercontent.com/MikelAcker/RACTF_2021_Writeup/main/Steg/The%20Glory%20Days/info2.png">

Still nothing interesting.

I decided to *grey* out all the things and look at them one by one.

<img src="https://raw.githubusercontent.com/MikelAcker/RACTF_2021_Writeup/main/Steg/The%20Glory%20Days/info3.png">

The No.2 is pretty interesting.

<img src="https://raw.githubusercontent.com/MikelAcker/RACTF_2021_Writeup/main/Steg/The%20Glory%20Days/info4.png">

It looks like [Morse Code](https://en.wikipedia.org/wiki/Morse_code).

I wrote them down and tried to decode it in [CyberChef](https://gchq.github.io/CyberChef/)
```
--- .--- --.- .-- --. ..... -.. --. .--. -. --. -..- -.- ....- --.. .-. -- -. .--. ..- ..--- -- -.. ... -.- -. ... ...- -.... - .-.. ..-. --- -. .--- - .. --.. --.. - .--. ..-
```

<img src="https://raw.githubusercontent.com/MikelAcker/RACTF_2021_Writeup/main/Steg/The%20Glory%20Days/info5.png">

The result is a *base32* string.

Let's decode it again!

<img src="https://raw.githubusercontent.com/MikelAcker/RACTF_2021_Writeup/main/Steg/The%20Glory%20Days/info6.png">

Now there is the flag.

*flag*: `ractf{Mus1c_M0rSe_MesS4g3}`
