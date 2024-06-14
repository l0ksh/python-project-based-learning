num = int(input("Enter a number to check if it is prime or not !!! "))

divisor_list = range(2,11)
result = []

def prime(num):
    for e in divisor_list:
        if num % e == 0:
            result.append(e)
    if len(result) == 1:
        print(f"The number {num} is prime.")
    else:
        print(f"The number {num} is not prime")

prime(num)