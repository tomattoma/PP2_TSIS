#Write a Python program to write a list to a file.

list = ['2', '3', '4', '0']

with open("C:\\Users\Huawei\\Desktop\\PP2_TSIS\\TSIS6\\dir-and-files\\lalala.txt", 'w') as f:
    for line in list:
        f.write(f"{line}\n")
        print(f"{line} write successful")