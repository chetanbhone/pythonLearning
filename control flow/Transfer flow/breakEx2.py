# print PYTH using break in while loop
s="PYTHON"
print("-"*40)
i=0
while(i<len(s)):
    if(s[i]=="O"):
        break
    else:
        print("{}".format(s[i]),end="")
        i+=1
else:
    print("This is from whiile loop")  # not executes
print()
print("-"*40)

