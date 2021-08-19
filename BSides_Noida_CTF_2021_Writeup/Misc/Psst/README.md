# Psst 159 Points

# Description
Psst! Want to know a secret? Here, take this...

# Attachments
[challl link](https://github.com/MikelAcker/CTF_WRITEUPS_2021/blob/main/BSides_Noida_CTF_2021_Writeup/Misc/Psst/psst.tar.gz?raw=true) ( Link may be down but I included the file in this dir )

# Solution
We are given with a **gzip** compressed file called `psst.tar.gz`

We can decompress it with `gzip` command

`$ gzip -d psst.tar.gz`

After running above command, it gives a **tar** archive called `psst.tar`

Extract files from it with `tar` command.

`$ tar -xf psst.tar`

Now, there is a directory called `chall` which contains a directory `Security`.

In `Security`, there is a directory `BSides`  and a file `readme_0.txt` which contains a character 'B'.

And, in `BSides` directory there is also a directory and a file which also contains a character.

So, what we have to do is go to a directory, collect a character from a file and go to another directory and collect another character.

You can do it *manually* 🙂🙂🙂

But I will use *python script* to do that

```python
# solve.py
# Save the script in 'chall' directory and run it

import os

# There is only one directory in chall
# So go to it
os.chdir("Security")

# loop until there is only one file
while True:
	# list the directory and store results in items
	items = os.listdir()

	for item in items:
    	# if the item is directory, set next directory to it
		if os.path.isdir(item):
			next_dir = item
      # if the item is a file, read it and print the content
		else:
			with open(item, 'r') as file:
				print(file.read().strip(), end='')  # end='' to not to print new line

	# if there is only one item ( which means only one file ) break the loop
	if len(items) == 1:
		break

	# change to next directory
	os.chdir(next_dir)

print("")
```

Run it and it will print out the flag
```bash
$ python3 solve.py
BSNoida{d1d_y0u_u53_b45h_5cr1pt1ng_6f7220737461636b6f766572666c6f773f}
```

*flag*: `BSNoida{d1d_y0u_u53_b45h_5cr1pt1ng_6f7220737461636b6f766572666c6f773f}`
