# program for finding product of n natural number
n=int(input("enter your number here for finding the sum"))
print("-"*40)
if n<0:
    print("{} is invalid number".format(n))
else:
    prod=1
    for i in range(1,n+1):
     print(i)
     prod*=i
print("product of {} natural number is {}".format(n,prod))
print("-"*40)