# program for demonstaring the CONTINUE for print PYHN using while loop
s="PYTHON"
print("-"*40)
for ch in s:
    if ch in ["T","O"]:
        continue
    else:
        print("{}".format(ch),end="")
print()
print("-" *40)

# # or using while loop
# i=0
# while(i<len(s)):
#     if (s[i]=="T") or (s[i]=="O"):
#         i+=1
#     else:
#         print("{}".format(s[i]),end="")
#         i+=1
