# Print characters from a string that are present at an even index number

# Write a program to accept a string from the user and display characters 
# that are present at an even index number.

def evenIndex(str):
    for i in range(len(str)):
        if i % 2 == 0:
            print(str[i])

evenIndex("pynative")