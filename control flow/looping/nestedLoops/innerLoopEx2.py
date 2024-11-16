# program for demonstracting loop in loop  ---> while in while loop
i=1
while(i<=5):
    print("-"*40)
    print("outer loop : value of i = {}".format(i))
    i+=1
    j=1
    while(j<=4):
       print("inner loop : value of j = {}".format(j))
       j+=1
    else:
        print("inner loop else block")
else:
    print("-"*40)
    print("outer loop else block")
    print("-"*40)