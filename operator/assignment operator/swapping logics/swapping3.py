# swapping lofic thre <<<<<<<<< using additon and substraction >>>>>>>>>
x=float(input("enter value of x "))
y=float(input("enter value of y "))
print("*"*50)
print("the value of x is {} ".format(x))
print("the value of y is {} ".format(y))
print("*"*50)
# swapping
x=x+y
y=x-y
x=x-y
print("swapped value of x is {} ".format(x))
print("swapped value of y is {} ".format(y))
print("*"*50)
