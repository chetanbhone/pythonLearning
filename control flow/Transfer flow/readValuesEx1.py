# program for reading dynamic values from KBD
n=int(input("enter how many numbers of value you want"))
print("-"*40)
if(n<0):
    print("{} is invalid input".format(n))
else:
    lst = []
    for i in range(1,n+1):
        value=float(input("enter {} value".format(i)))
        lst.append(value)
print("-" *40)
print("the element in list is {}".format(lst))
print("-"*40)