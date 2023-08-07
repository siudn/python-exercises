# Given two integer numbers return their product only if the product is 
# equal to or lower than 1000, else return their sum.
# Write a program to iterate the first 10 numbers, and in each iteration, 
# print the sum of the current and previous number.

previousNum = 0

for i in range(10):
    print("current number", i, "previous number", previousNum, "sum", i + previousNum)
    previousNum = i