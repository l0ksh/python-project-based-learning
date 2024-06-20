# def fib(n):
#     """Calculates the fibonacci sequence to n terms"""
#     previous_number = 1
#     current_number = 1
#     next_number = 0 
#     fib = []

#     for i in range(n):
#         next_number = previous_number + current_number

#         fib.append(next_number)
#         previous_number = current_number
#         current_number = next_number
    
#     return fib

# def nth_element_in_fib(n):
#     """Returns the nth element in Fibonacci sequence"""
#     return fib(n)[-1]

# if __name__ == "__main__":
#     number_of_elements = input("How many Fibonacci numbers do you want to generate? ")
    
#     fib_sequence = fib(int(number_of_elements))
#     string_sequence = ""
#     sequence_length = len(fib_sequence)

#     print(fib_sequence)
#     for element in fib_sequence:
#         if fib_sequence.index(element) + 1 == sequence_length:
#             string_sequence += str(element)
#         else:
#             string_sequence += str(element) + ","
    
#     print("\nThe generated sequence is :: " + string_sequence)


user_number = int(input("Enter the number of numbers you want to print: "));


def fibbonacci(times):
    fibbo = [];
    for time in range(times):
        if time == 0:
            fibbo.append(1);
        elif time == 1:
            fibbo.append(1);
        else: # Playing with the indexes of fibbo
            fibbo.append(fibbo[time-1] + fibbo[time-2]);
    print(fibbo);

    

fibbonacci(user_number);