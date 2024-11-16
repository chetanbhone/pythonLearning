#program for accepting list of value from KBD and find their sum and value
n=int(input("how many numbers of value you want"))
if(n<0):
    print("{} is invalid input".format(n))
else:
    lst=[]
    for i in range(1,n+1):
         value=float(input("enter {} value".format(i)))
         lst.append(value)
    else:
        print("-"*40)
        print("content of list {}".format(lst))
print("-"*40)
print("The sum and average")
s=0
for val in lst:
    s+=val
else:
    print("-"*40)
    print("the sum of numbers in list is {}".format(s))
    print("the average of numbers in list is {}".format(s/len(lst)))
    print("-"*40)