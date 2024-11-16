# program for demonstracting the need of continue statement --- print only PYHON sikp T
s="PYTHON"
print("-"*40)
for ch in s:
    if(ch=="T"):
        continue
    print("{}".format(ch), end="")
else:
    print()
    print("-"* 40)
