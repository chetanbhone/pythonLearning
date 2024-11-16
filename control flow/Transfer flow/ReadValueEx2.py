# program for readig dynamic value from KBD using while loop
print("enter values (press @ to STOP)")
i=0
lst = []
print("-"*40)
while(True):
    i+=1
    value=input("enter {} values".format(i))
    if(value=="@"):
        break
    lst.append(float(value))
print("the values in list is {}".format(lst))
print("-"*40)