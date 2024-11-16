#program for generating multiplication table
#take input which number i want
# number * i ---- (i = 1 to 1)
n=int(input("enter a number which table you want "))
if(n<0):
    print("{} is invalid".format(n))
else:
    print("-"*40)
    i=1
    while(i<=10):
        print("{} * {} ={}".format(i,n,i*n))
        i+=1
    else:
        print("-"*40)
print("table ended")