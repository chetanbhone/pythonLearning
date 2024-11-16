findMax=lambda a,b: a if a>b else b if b>a else "Both are equal"
findMin=lambda a,b: a if a<b else b if b<a else "both are equal"

# main program
a,b=float(input("enter value of a ")) , float(input("enter value of b"))
max=findMax(a,b)
min=findMin(a,b)
print("the maximum among a and b is {}".format(max))
print("the minimum among a and b is {}".format(min))
