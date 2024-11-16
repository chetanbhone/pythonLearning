# program for demonstarcting loop in loop ---> for in while loop
i=5
while(i>1):
    print("-"*40)
    print("outer loop : value of i = {}".format(i))
    i-=1
    for j in range(4,0,-1):
        print("inner loop: value of j = {}".format(j))
    else:
       print("else block of inner loop")
else:
    print("else block of outer loop")
    print("-"*40)