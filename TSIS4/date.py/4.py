#Write a Python program to calculate two date difference in seconds.
from datetime import datetime, time

first = datetime(2025, 2, 13)
second = datetime(2025, 2, 14)

difference = (second.timestamp()-first.timestamp())

print(f"two date difference in seconds: {difference}")