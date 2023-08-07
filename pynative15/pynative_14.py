# Print downward Half-Pyramid Pattern with Star (asterisk)
# * * * * *  
# * * * *  
# * * *  
# * *  
# *

for i in range(5, 0, -1):
    for j in range(0, i):
        print("*", end=' ')
    print(" ")