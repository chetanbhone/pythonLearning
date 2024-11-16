#program for generate the  multiplication table using for loop
n=int(input("what table you want"))
if(n<=0):
    print("{} is invalid input".format(n))
print("-"*40)
for val in range(1,11,1):
    print("{} * {} = {}".format(val,n,val*n))
print("-"*40)
