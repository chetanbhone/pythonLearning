#check Weather the number is PRIME or not
n=int(input("enter your number here"))
print("-"*40)
if(n<1):
    print("{} is navlid input".format(n))
else:
    res="number is PRIME"
    for val in range(2,n):
        if(n%val==0):
            res="number is not PRIME"
            break

print("{} {}".format(n,res))
print("-"*40)