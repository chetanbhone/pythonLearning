# addition of two number using function definication
# input = input in function definication
# process = process inside function definication
# output = display inside function call
def sum():
    a=int(input("enter value of a"))
    b=int(input("enter value of b"))
    c=a+b
    return a,b,c
res=sum()
print("the sum of {} and {} is {} ".format(res[0],res[1],res[2]))