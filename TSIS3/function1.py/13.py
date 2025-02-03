import random

print("Hello! What is your name?")
name= input()
print(f"Well, {name}, I am thinking of a number between 1 and 20.")

random_num = random.randint(1,20)
print("Take a guess.")
number= int(input())

cnt=0

while number!=random_num:
    if number < random_num:
        print("Your guess is too low.")
        print("Take a guess.")
        number = int(input())
        cnt+=1
    elif number > random_num:
        print("Your guess is too high.")
        print("Take a guess")
        number = int(input())
        cnt+=1
if(number==random_num):
    print(f"Good job, {name}! You guessed my number in {cnt} guesses!")