# program for accepting list of value from KBD and their sumn and average
print("enter values (press @ to stop)")
lst=[]
i=0
while(True):
    i+=1
    value=input("enter {} value".format(i))
    if(value=="@"):
        break
    lst.append(float(value))
print("-"*40)
print("element of list {}".format(lst))
print("-"*40)
print("the sum and average")
s=0
for val in lst:
    s+=val
print("the sum of numbers in list is {}".format(s))
if(len(lst)>0):
    print("the average of numbers in list is {}".format(s/len(lst)))
else:
    print("the average cannot be calculated")
print("-"*40)