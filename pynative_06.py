# Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only 
# those numbers which are divisible by 5

given = [10, 20, 33, 46, 55]

for i in given:
    if i % 5 == 0:
        print(i)
