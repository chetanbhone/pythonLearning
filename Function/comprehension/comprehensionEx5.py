# program for getting value from keyboard and seperated by spaces in tuple
print("enter your words here...")
obj=(word for word in input().split())
print(obj,type(obj))     #compreshension technique is not exist in tuple 
obj2=tuple(obj)
print(obj2,type(obj2))