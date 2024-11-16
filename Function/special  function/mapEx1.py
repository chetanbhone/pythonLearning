def squares(val):
    return(val**2)

print("enter you number here that you want to make squares")
lst=[int(val) for val in input().split()]
newlst=tuple(map(squares,lst))
both=zip(lst,newlst)
for a,b in both:
    print("{:<10}{:<10}".format(a,b))
print("-"*40)

# {:<10}{:<10 added 10 spaces between a and b here ...