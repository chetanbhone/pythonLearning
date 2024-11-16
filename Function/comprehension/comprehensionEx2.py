# program for reading values from keyboard and seperate them using spcaes and find square of that
print("enter your values here...")
obj={ float(val):float(val)**2 for val in input().split() if float(val) > 0 }
print("the square of values you  given is ")
for a,b in obj.items():
    print("{} ----> {}".format(a,b))