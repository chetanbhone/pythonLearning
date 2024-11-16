# check weather the number is prime or not using ternary operator in break statement
n=int(input("enter your number here"))
i=2
res=True
while(i<n):
    if(n%i==0):
        res=False
        break
    i+=1
r= "PRIME" if res else "NOT PRIME"
print("{} is {}".format(n,r))