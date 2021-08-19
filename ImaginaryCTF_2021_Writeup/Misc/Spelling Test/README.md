# Spelling Test 100 Points

# Description
I made a spelling test for you, but with a twist. There are several words in words.txt that are misspelled by one letter only. Find the misspelled words, fix them, and find the letter that I changed. Put the changed letters together, and you get the flag. Make sure to insert the "{}" into the flag where it meets the format.

NOTE: the words are spelled in American English

# Attachments
https://imaginaryctf.org/r/CBC8-words.txt

# Solution
If you look at the given file, you will see some **misspelled** words

```
Given Word:   convirgence
Correct Word: convergence
```
Misspelled letter here is 'i'
```
Given Word:   translatcr
Correct Word: translator
```
Here is 'c'
```
Given Word:   addretsing
Correct Word: addressing
```
Here is 't'
```
Given Word:   approachfs
Correct Word: approaches
```
And, here is 'f'

Now, we get the start of our flag "ictf"

All we have to do now is to find other **misspelled** words, collect the **misspelled** letter and get the flag

But, I will create python script called "solve.py" using **autocorrect** module to automate this

```python
from autocorrect import Speller

check = Speller(lang="en")
flag = ""

with open("./words.txt", 'r') as file:
	for line in file:
		word = list(line[:-1])   # [:-1] to remove new line
		correct = list(check(line[:-1]))

		if word != correct:   # Found misspelled word
			index = 0

                        # trying to get the index of misspelled letter
			while word[index] == correct[index]:
				index += 1

			flag += word[index]   # append misspelled letter to flag

# we have to insert '{' after "ictf" and '}' at the end to meet the format
print(flag[:4] + '{' + flag[4:] + '}')
```

It will give out the flag
```
ictf{youpassedthespellingtest}
```
