num = int(input("Enter your number: "))

def oddeven(num):
    if num % 2 == 0 and num % 4 != 0:
        print(f"{num} is even number.")
    elif num % 2 == 0 and num % 4 == 0:
        print(f"{num} is even and is divisible by 4.")
    else:
        print(f"{num} is odd.")

oddeven(num)