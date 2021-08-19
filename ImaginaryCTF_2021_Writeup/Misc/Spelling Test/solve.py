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
