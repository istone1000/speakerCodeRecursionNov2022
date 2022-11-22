#Irene Stone
#Nov 2022
#Factorial

def fact(n):             #n is the parameter
    if n == 0:
        return 1
    return n * fact (n-1)                          #ask what do we want n multiplied by? one less than it?


result =fact(5)
print(result)
