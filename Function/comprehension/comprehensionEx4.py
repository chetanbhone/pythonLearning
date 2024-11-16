# program for getting values from keyboard
print("enter your values here...")
PositiveLst=[ float(val) for val in input().split() if float(val)>0]
print(PositiveLst)
NegativeList=[float(val) for val in input().split() if float(val)<0 ]
print(NegativeList)