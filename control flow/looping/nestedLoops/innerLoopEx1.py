# program for demonstracting Loop in loop called inner Loop -----> for in for loop
for i in range(1,6):
    print("-"*40)
    print("outer loop : value of i = {}".format(i))
    print("-"*40)
    for j in range(1,4):
        print("inner Loop : value of j = {}".format(j))
    else:
        print("else block of inner loop")
        print("-" *40)
else:
    print("else block of outer loop")
    print("-"*40)
