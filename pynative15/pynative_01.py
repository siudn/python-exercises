#Calculate multiplication and sum of two numbers
#Given two integer numbers return their product only if the 
#product is equal to or lower than 1000, else return their sum.

def multOrSum(num1, num2):
    sum = num1 + num2
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return sum

print(multOrSum(20,30))
print(multOrSum(40,30))
