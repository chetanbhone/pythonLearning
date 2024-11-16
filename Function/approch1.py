# addition of two numbers using function
# input = taking input from function call
# process = process inside function defination ---------> same everywhere
# output = give output to function call

def sum(a,b):
    c=a+b
    return c
a=int(input("enter your first number"))
b=int(input("enter your second number"))
res=sum(a,b)   # function call
print("-"*40)
print("sum of {} and {} is {}".format(a,b,res))
print("-"*40)
