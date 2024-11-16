# swappping logic two <<<<< using multiplication and division >>>>>>>
x=float(input("enter value of x "))
y=float(input("enter value of y "))
print("*"*50)
print("the value of x is {}".format(round(x)))
print("the value of y is {} ".format(round(y)))
print("*"*50)
# swapping
x=x*y
y=x//y
x=x//y
print("the swapped values of x is {} ".format(x))
print("the swapped value of y is {} ".format(y))
print("*"*50)