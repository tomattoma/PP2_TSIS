#Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not
import os
def check_path(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        print("The file does not exist")

path = input()
check_path(path)