# Check Palindrome Number
# Write a program to check if the given number is a palindrome number.
# A palindrome number is a number that is same after reverse. For example 
# 545, is the palindrome numbers

def palindrome(num):
    return str(num) [0:] == str(num) [::-1]

print(palindrome(545))
print(palindrome(6455))
print(palindrome(786))
print(palindrome(787))