# Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a 
# given list is same. If numbers are different then return False.

def firstAndLast(given):
    return given[0] == given[-1]

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

print(firstAndLast(numbers_x))
print(firstAndLast(numbers_y))