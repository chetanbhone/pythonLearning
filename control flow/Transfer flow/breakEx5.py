# check weather the number is prime or not using break in while loop
n=int(input("enter your number here"))
print("-"*40)
if(n<2):
    print("{} is invalid number".format(n))
else:
 i=2
 res="number is PRIME"
 while(i<n):
    if(n%i==0):
        res="number is NOT prime"
        break
    i+=1
print("{} {}".format(n,res))
print("-"*40)