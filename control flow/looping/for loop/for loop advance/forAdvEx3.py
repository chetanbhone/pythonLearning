# find the factorial of a given number using while loop - logic 3
n = int (input("enter number for factorial "))
print("-"*40)
if n<0:
    print("{}  is invalid ".format(n))
elif n==0:
    print("{} factorial is 1".format(n))
else :
    fact=1
    i=1
    while(i<=n):
      fact*=i
      i+=1
    else:
     print("{} factorial is {}".format(n,fact))
print("-"*40)