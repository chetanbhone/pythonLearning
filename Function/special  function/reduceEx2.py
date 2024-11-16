import functools
print("enter your values here to get sum of all of values")
lst=[int(val) for val in input().split()]
total=functools.reduce(lambda x,y:x+y , lst)
print("the original list is {}".format(lst))
print("the sum is {}".format(total))


