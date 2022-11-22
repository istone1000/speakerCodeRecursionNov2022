# LCCS Python Fundamental Skills Workshop
# Nov 2022
# Purpose: A programme to find the sum of the first N numbers

def sumOfN(n):
    if n == 0:
        return 0
    return n + sumOfN(n-1)

print(sumOfN(7))