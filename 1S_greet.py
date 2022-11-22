#Irene Stone
#Nov 2022
#Introduction to Recursion

i = 0            #global variable

def greet():
    global i
    print ("hello", i)
    i = i+1
    greet()
    
greet()
#greet()
