# find max and min using userdefined functions
def cbMax(lst):
    maxVal=lst[0]
    for val in lst:
        if val>maxVal :
            maxVal=val
    return maxVal

def cbMin(lst):
    minVal=lst[0]
    for val in lst:
        if val < minVal :
            minVal=val
    return minVal

findMax=lambda lst:cbMax(lst)
findMin=lambda lst:cbMin(lst)

print("enter numbers seperated by spaces")
lst=[ float(val) for val in input().split()]
bigVal=findMax(lst)
smVal=findMin(lst)
print(lst)
print("maximum number among list is {}".format(bigVal))
print("minimum number among list is {}".format(smVal))

