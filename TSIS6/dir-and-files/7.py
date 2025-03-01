#Write a Python program to copy the contents of a file to another file

import os
with open("", 'r') as firstfile, open("", 'a') as secondfile:
    for line in firstfile:
        secondfile.write(line)