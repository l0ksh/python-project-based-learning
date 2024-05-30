a = "zeez"

def reverse(s):
    # easiest way to reverse a string
    return s == s[::-1]

if reverse(a):
    print("The given string is a palindrome")
else:
    print("The given string is not a palindrome.")

    
