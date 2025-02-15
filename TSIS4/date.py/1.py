#Write a Python program to subtract five days from current date.
from datetime import datetime, timedelta

x = datetime.now()
result = x - timedelta(days = 5)
print(f"five days from current date: {result}")