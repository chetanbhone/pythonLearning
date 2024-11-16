# swapping logic 5 <<<<<<< XOR >>>>>>>>>>
x=int(input("enter value of x "))
y=int(input("enter value of y "))
print("*"*50)
print("the value of x is {} ".format(x))
print("the value of y is {} ".format(y))
print("*"*50)
# swapping
x=x^y
y=x^y
x=x^y
print("the swapped value of x is {} ".format(x))
print("the swapped value of y is {} ".format(y))
print("*"*50)