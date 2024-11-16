#program for generating 1 to N number where n is positive
n=int(input("enter your number"))
if(n<0):
    print("{} is invalid ".format(n))
else:
    i=1
    while(i<=n):
        print(i)
        i+=1
    else:
      print("i am else part  of while loop")
    print("else part of if else")
print("other part pf programming")

