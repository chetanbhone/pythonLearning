print("enter values here to get the squares")
lst=[int(val) for val in input().split()]
newlst=tuple(map(lambda x: x**2 , lst))
both= zip(lst,newlst)
for a ,b in both:
    print("{:<10} {:<10}".format(a,b))
print("---"*40)