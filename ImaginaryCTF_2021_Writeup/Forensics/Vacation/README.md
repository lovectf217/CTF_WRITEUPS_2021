# Vacation 100 Points

# Description

Roo's cousin was on vacation, but he forgot to tell us where he went! But he posted this image on his social media. Could you track down his location? Submit your answer as ictf{latitude_longitude}, with both rounded to 3 decimal places. Example: ictf{-12.345_42.424} (Note: only the image is needed for this challenge, as this is an OSINT challenge.)

# Attachments

https://imaginaryctf.org/r/EA9D-image.jpg

# Given image
<img src="https://github.com/MikelAcker/ImaginaryCTF_2021_Writeup/blob/main/Forensics/Vacation/chall.jpg" height=500 width=500>

# Solution
At first, I looked the image in **Google** reverse image search but this doesn't help me very much.So, I decided to look at the image closely and I found some interesting things

# National Treasure
<img src="https://github.com/MikelAcker/ImaginaryCTF_2021_Writeup/blob/main/Forensics/Vacation/info1.jpg" height=600 width=250>

Searching for **National Treasure** in google didn't give me much information.So, a few seconds later I tried searching for another thing


# SugarPine Bakery
<img src="https://github.com/MikelAcker/ImaginaryCTF_2021_Writeup/blob/main/Forensics/Vacation/info2.jpg" height=450 width=250>

This time I found some interesting results from searching google.There is only one **Sugar Pine Bakery** shows up in google map tab.

-[Google Map Results](https://www.google.com/maps/search/Sugar+Pine+Bakery/@39.0529785,-120.1662473,11.5z)

-[Link to Actual Map](https://www.google.com/maps/place/Sugar+Pine+Bakery/@38.9462887,-119.9613926,18.75z/data=!3m1!5s0x8099900f0a95e6af:0x53db7f7963212e3e!4m9!1m2!2m1!1sSugar+Pine+Bakery!3m5!1s0x8099900fa055cdd5:0x8fc43935f49d2b39!8m2!3d38.9466063!4d-119.9610917!15sChFTdWdhciBQaW5lIEJha2VyeVoTIhFzdWdhciBwaW5lIGJha2VyeZIBBmJha2VyeQ)

Use street view, land on **Lake Tahoe Blvd** and go around near the **Sugar Pine Bakery**.You will found a flag like **National Tresure** flag in given image

[National Treasure Flag](https://www.google.com/maps/@38.94711,-119.9614202,3a,15.5y,24.33h,91.56t/data=!3m6!1e1!3m4!1soFk1nXrY9AhpaaIpQOhM2g!2e0!7i16384!8i8192)

And there you go!
That is the place in the image.So, the latitude and longitude in the link are

```
38.94711,-119.9614202
```

As the challenge description said we have to round them up in 3 decimal places.So they will become

```
38.947,-119.961
```

And the final **flag** is

```
ictf{38.947_-119.961}
```
