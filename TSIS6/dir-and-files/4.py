#Write a Python program to count the number of lines in a text file.

with open("C:\\Users\Huawei\\Desktop\\PP2_TSIS\\TSIS6\\dir-and-files\\lalala.txt", 'r') as f:
    lines = len(f.readlines())
    print(lines)