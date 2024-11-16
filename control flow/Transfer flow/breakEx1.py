# print break statement in for loop with using break statement
s="PYTHON"
print("-"*40)
for ch in s :
    if(ch=="O"):
        break
    else:
        print("{}".format(ch),end="")
else:
    print("i am form else part of for loop")     # not executes
print()  # for new line
print("-"*40)