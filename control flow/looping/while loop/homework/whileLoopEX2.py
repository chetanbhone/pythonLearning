# write a python program to generate odd numbers upto n where n is positive
n=int(input("enter your number here"))
if(n<0):
    print("{} is invalid input".format(n))
else:
    print("odd numbers from 1 to {}".format(n))
    print("-"*40)
    i=1
    while(i<=n):
        print(i)
        i+=2
print("-"*40)
