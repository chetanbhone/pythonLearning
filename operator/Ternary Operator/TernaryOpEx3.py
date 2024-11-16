#program for deciding wheather value if palindrom or not
a=input("enter a value to check palindrom or not ")
value = "is a palindrom" if a==a[::-1] else "not a palindrom"
print("*"*50)
print("{} {}".format(a,value))
print("*"*50)