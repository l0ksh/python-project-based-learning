#x = range(2, 11)
# for e in x:
#     print(e)

# Here "x" is type 'range'. Range can also be looped by using a for loop.
num = int(input("Enter a number: "))
divisor_list = range(1,11)
result = []

def divisors(num):
    for e in divisor_list:
        if num % e == 0:
            result.append(e)
    print(result)

divisors(num)