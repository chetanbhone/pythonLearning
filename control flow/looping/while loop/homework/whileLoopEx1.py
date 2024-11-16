#write a program which geneate even numbers upto n where n is positive value
n=int(input("enter your number"))
if(n<0):
    print("{} is invalid input".format(n))
else:
    print("even numbers from 1 to {}".format(n))
    print("-"*40)
    i=2
    while(i<=n):
        print(i)
        i+=2
print("-"*40)