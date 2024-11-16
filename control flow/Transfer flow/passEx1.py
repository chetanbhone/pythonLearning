# program for demonstrating the use of PASS in for loop - for write only PYHON
s="PYTHON"
print("-"*40)
for ch in s:
    if(ch=="T"):pass
    else:
        print("{}".format(ch),end="")
print()
print("-"*40)