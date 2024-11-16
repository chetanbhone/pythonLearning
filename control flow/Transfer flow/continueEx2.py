# program to demonstating need of continue for print only PYHON using while loop using continue statement
s="PYTHON"
print("-"*40)
i=0
while(i<len(s)):
    if(s[i]=="T"):
        i+=1
        continue
    print("{}".format(s[i]),end="")
    i+=1
print()
print("-"*40)
