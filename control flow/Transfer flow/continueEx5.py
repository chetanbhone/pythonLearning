# program to print the +ve and -ve numbers in list using CONTINUE and PASS
lst=[1,2,3,4,-1,-2,-3,4,5,-5,6,-7,]
print("-"*40)
print("postive numbers from list")
for val in lst:
    if(val<0):
        continue
    else:
        print("\t{}".format(val))
print("-"*40)
print("negative numbers from list")
print("-"*40)
for val in lst:
    if(val>0):pass
    else:
        print("{}".format(val))
print("-"*40)
