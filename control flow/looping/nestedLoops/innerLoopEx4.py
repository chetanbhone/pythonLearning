# program for deonstracting loop in loop ----> while in for loop
for i in range(5,0,-1):
    print("-"*40)
    print("outer loop : value of i = {}".format(i))
    j=4
    while(j>=1):
        print("inner loop : value of j = {}".format(j))
        j-=1
    else:
        print("inner loop else block")
else:
    print("-"*40)
    print("outer loop else block")
    print("-"*40)