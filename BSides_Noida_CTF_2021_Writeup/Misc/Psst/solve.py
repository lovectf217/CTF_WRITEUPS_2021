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
