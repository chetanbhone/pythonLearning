# calculate the sum of all natural number upto number input by user
n=int(input("enter your number here"))
if(n<0):
    print("{} is invalid number")
print("-"*40)
s=0
for val in range(1,n+1):
    s+=val
print("the sum of natural number upto {} is {}".format(n,s))
print("-"*40)