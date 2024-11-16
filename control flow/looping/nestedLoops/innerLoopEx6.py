# program for generating multiplication table for n random numbers where n is positive ----> using nested loop concept
n=int(input("enter how many numbers table you want"))
if(n<0):
    print("{} is navlid input".format(n))
else:
    lst=[]
    for i in (range(1,n+1)):
       num=int(input("enter {} number ".format(i)))
       lst.append(num)
    else:
        print("-"*40)
        print("numbers in list ".format(lst))
        print("-"*40)
        for num in lst:
            if (num<0):
               print("{} is invalid input".format(num))
            else:
                print("-"*40)
                print("multiplication table for {} ".format(num))
                print("-"*40)
                for i in range(1,11):
                    print("{} * {} = {}".format(num , i , num*i))
                else:
                    print("-"*40)
