# input two numerical values and find biggest among them and check for equality
a=float(input("enter value of a"))
b=float(input("enter value of b"))
value= a if (a>b) else b if (b>a) else "both are equal"
print("*"*50)
print("Biggest among {} and {} is {}".format(a,b,value))
print("*"*50)