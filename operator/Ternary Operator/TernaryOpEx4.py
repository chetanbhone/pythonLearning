# get a numerical value and decide weather it is +ve , -ve , zero
a=int(input("enter value of a"))
value = " the value positive value " if (a>0) else " the value is negative value " if (a<0) else " the value is zero"
print("*"*50)
print("{}".format(value))
print("*"*50)