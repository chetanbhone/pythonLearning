# program for demonstrating use of PASS to print only PYHON in while loop
s="PYTHON"
print("-"*40)
i=0
while(i<len(s)):
    if(s[i]=="T"):    # write pass in not compulsary
       i+=1
    else:
        print("{}".format(s[i]),end="")
        i+=1
print()
print("-"*40)