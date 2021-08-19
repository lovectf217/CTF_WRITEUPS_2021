# My Artwork 287 points

# Description
"You can create art and beauty with a computer." - Steven Levy
So, I decided not to use MS Paint anymore and write code instead!
Hope you can see my art before the turtle runs away!
He's pretty fast tbh!
PS: Put the flag in BSNoida{} wrapper.

# Attachments
[chall link](https://storage.googleapis.com/noida_ctf/Misc/art.TURTLE)

# Solution
Looking at the **art.TURTLE** and searching online like `REPEAT 10000 [FD 200`, I found that they are syntax of [MSW Logo](https://en.wikipedia.org/wiki/MSWLogo)

To get the flag, download **MSW LOGO** program, run it and copy the **repeat commands** from **art.TURTLE** and paste in the `commander` window

And, then collect the *characters* it draws

But, I didn't want to download the program.So I used *online logo interpreter* instead

https://www.calormen.com/jslogo/

Copy and paste the **repeat commands** and click **run** button and collect the *characters* it draws

<img src="https://raw.githubusercontent.com/MikelAcker/CTF_WRITEUPS_2021/main/BSides_Noida_CTF_2021_Writeup/Misc/My%20Artwork/info.png">

We will get
`CODE_IS_BEAUTY_BEAUTY_IS_CODE`

So, our flag will be
`BSNoida{CODE_IS_BEAUTY_BEAUTY_IS_CODE}`
