#program for finding the chars in line
line=input("enter your line here")
print("-"*40)
print("line is {}".format(line))
noa=0
for ch in line:
    if(ch.isalpha()):
        noa+=1
else:
    print("the number of alpha in line is {}".format(noa))
print("-"*40)