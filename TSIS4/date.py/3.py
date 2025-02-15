#Write a Python program to drop microseconds from datetime.
from datetime import datetime


now = datetime.now()
today_is = now.strftime("%Y-%m-%d %H:%M:%S")

print(today_is)