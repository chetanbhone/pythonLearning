# program for finding the digit in line
line=input("enter your line here")
print("-"*40)
print("the line is ".format(line))
nod=0
for di in line:
    if(di.isdigit()):
        nod+=1
print("the number of digit in line is {}".format(nod))
print("-"*40)