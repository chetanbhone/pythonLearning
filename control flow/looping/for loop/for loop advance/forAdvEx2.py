# find factorial of given number using for loop - logic 2
n= int(input("enter a  number for find the factorial"))
print("-"*40)
if n<0:
    print("{} is invalid number".format(n))
elif n==0:
    print("{} factorial is 1".format(n))
else:
    fact=1
    for i in range(n,0,-1):
        fact*=i
    print("factorial of {} is {}".format(fact))
print("-"*40)



