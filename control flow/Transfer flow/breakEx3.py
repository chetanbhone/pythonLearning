# print MISS  in MISSISSIPPI using break

s="MISSISSPPI"
print("using for loop")
print("-"*40)
cnt = 0
for ch in s:
    if(ch=="I"):
        cnt+=1
    if(cnt==2):
        break
    else:
        print("{}".format(ch),end="")
else:
    print("this is form else block of for loop") # not executes
print()
print("-"*40)

#---------------------------------------------------------
# using while loop
print("using while loop")
#---------------------------------------------------------
s="MISSISSIPPI"
print("-"*40)
cnt=0
i=0
while(i<len(s)):
    if(s[i]=="I"):
        cnt+=1
    if(cnt==2):
        break
    else:
        print("{}".format(s[i]),end="")
        i += 1
else:
    print("else block of while loop")   # not executes
print()
print("-"*40)