# program for odd number from to given range in reverse order usinf for loop
n=int(input("enter your range here "))
if(n<=0):
    print("{} is invalid number".format(n))
print("-"*40)
if(n%2==0):
   n-=1
for val in range(n,0,-2):
    print(val)
print("-"*40)