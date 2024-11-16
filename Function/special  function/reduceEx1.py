import functools
def sumof(x,y):
    return x+y

lst=[int(val) for val in input().split()]
total=functools.reduce(sumof,lst)
print("original list {}".format(lst))
print("total of list {}".format(total))