# program to print multiplication of given number
while(True):
        def mul(n):
            if(n<0):
                print("{} is invalid input".format(n))
            else:
                print("-"*40)
                print("multiplication table for {} is ".format(n))
                for val in range(1,11):
                   print("{} * {} = {}".format(n,val,n*val))
                print("-"*40)

        n=int(input("enter your number here"))
        if(n>0):
            mul(n)
            break

