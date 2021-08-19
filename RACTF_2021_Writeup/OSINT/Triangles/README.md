# Triangles 100 points

# Given Image
<img src="https://raw.githubusercontent.com/MikelAcker/RACTF_2021_Writeup/main/OSINT/Triangles/info1.jpg">

# Solution
Search the image with **google reverse image search**.

It says it is **palazzo cosentini** [link](https://www.google.com.mm/search?tbs=sbi:AMhZZivbs1gFRpB8wAI9WlI3AkGmTA92YcK1qPW0487kIQP2-btaR2HFMYpJy1uNRZm3Si9HNGRE7_19el1Yz6Gxpt0ZVvMWmedgFGiYFSqgUNC9h9j7hwM6Hojk5a1SvcX0UbY4BI-oQV9WP5dQ80fJNhRcaBpLyqpMRB9kmFuENad8ol03RGVw1atUvV1FAsSZuAWXlZ1e4CZYwTsAE9egXk5JgQOAx7y8660Q4zqGNO1nSISUZijZlpUFAK78xz5RwLQvN7cTpDCwD6QB-cFOrjf9zvneaM5GJ26isFKL5X12Y14grW8pVc3SPyrC7YUzvOUAk5EOG).

Now search **palazzo cosentini** in *google map* [map link](https://www.google.com.mm/maps/place/Palazzo+Cosentini/@36.9267665,14.7344974,17z/data=!3m1!4b1!4m5!3m4!1s0x1311999df7357997:0x700f5a852df15e3!8m2!3d36.9267676!4d14.7366924).

Now *zoom in* closer until you can't anymore [map link](https://www.google.com.mm/maps/place/Palazzo+Cosentini/@36.9267459,14.736531,21z/data=!4m5!3m4!1s0x1311999df7357997:0x700f5a852df15e3!8m2!3d36.9267676!4d14.7366924)

Extract latitude and longitude from the url `36.9267459,14.736531`.

And put them in our challange web page `jump` input.

<img src="https://raw.githubusercontent.com/MikelAcker/RACTF_2021_Writeup/main/OSINT/Triangles/info2.png">

*Zoom in* until you can see *selections* and click `jump`.

<img src="https://raw.githubusercontent.com/MikelAcker/RACTF_2021_Writeup/main/OSINT/Triangles/info3.png">

Now, select the location you saw from *google map*

<img src="https://raw.githubusercontent.com/MikelAcker/RACTF_2021_Writeup/main/OSINT/Triangles/info4.png">

And, that's it!!!
