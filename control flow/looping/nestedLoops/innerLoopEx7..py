# program for obtaining list of prime numbers from list of numbers entered by user ----> using nestedLoop
n=int(input(("how mauny number you want to enter")))
if(n<0):
    print(f"{n} is an invalid number.")
else:
    lst=[]
    for i in range(1,n+1):
        num=int(input("enter {} number".format(i)))
        lst.append(num)
    else:
        print("the numbers in list {}".format(lst))
        print("-"*40)
        ps=[]
        for val in lst:
            if(val <= 1):pass
            else:
                res=True
                for i in range(2,val):
                    if(val%i==0):
                        res=False
                        break
                if(res):
                    ps.append(val)

        else:
            print("prime numbers = {}".format(ps))