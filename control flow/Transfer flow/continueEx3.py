# program for demonstrating the need of CONTINUE for print only PYHN in for loop
s="PYTHON"
print("-" *40)
for ch in s:
    if(ch=="T") or (ch=="O"):
        continue
    else:
        print("{}".format(ch),end="")
print()
print("-"*40)