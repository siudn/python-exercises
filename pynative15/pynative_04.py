# Remove first n characters from a string
# Write a program to remove characters from a string 
# starting from zero up to n and return a new string.

def remove_chars(str, n):
    if n < len(str):
        return str[n:]
    else:
        return "ERROR"

print(remove_chars("pynative",4))
print(remove_chars("pynative",2))