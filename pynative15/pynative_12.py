# Calculate income tax for the given income by adhering to the below rules
# Taxable Income	Rate (in %)
# First $10,000	    0
# Next $10,000	    10
# The remaining	    20

def taxFunction(given):
    incomeTax = 0
    if given <= 10000:
        return incomeTax
    elif given <= 20000:
        incomeTax = (given - 10000) * 0.1
        return incomeTax
    else:
        given -= 20000
        incomeTax += given * 0.2 + 1000
        return incomeTax

print(taxFunction(45000))