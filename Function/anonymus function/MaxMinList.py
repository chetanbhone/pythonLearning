# find maximum and minimum among list using predefined functions
findMax=lambda lst: max(lst)
findMin= lambda lst: min(lst)
print("enter a values seperated by spaces")
lst=[float(val) for val in input().split()]
max=findMax(lst)
min=findMin(lst)
print("the greatest among list is {}".format(max))
print("the smallest among list is {}".format(min))
