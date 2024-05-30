import random as rd

noofguessess = 1

def Guess(num):
    if num == random_num:
        print(f"Congratulations !! You guessed it right.")
    elif num < random_num:
        print("Too low")
    elif num > random_num:
        print("Too high")
    else:
        print("Plese enter valid number !!!")

while True: # game on
    random_num = rd.randint(1,9)
    user_num = int(input("Guess a number ! "))
    Guess(user_num)
    noofguessess += 1
    if input("Another round (Y/N)") == "N":
        break

print(f"You played {noofguessess} times !!!")