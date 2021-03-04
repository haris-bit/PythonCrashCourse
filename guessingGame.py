import random 

guess = 0

num = random.randint(1, 100)    
guess = int(input("Enter a number between 1-100: "))

while guess!=num:
    if guess==num:
        print("Congrats! You Won!")
        break
    elif guess>num:
        print("Try a Smaller Number")
        guess = int(input("Enter a number between 1-100: "))
    elif guess<num:
        print("Try a Bigger Number")
        guess = int(input("Enter a number between 1-100: "))

