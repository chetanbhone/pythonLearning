# print reverse of line without using slicing and reverse() function
line=input("enter your line here")
print("-"*40)
print("the line is {}".format(line))
s=""
for ch in range(-1,-(len(line)+1),-1):
    s+=line[ch]
print("the reverse of line is {} ".format(s))
if s==line:
    print("{} is palindrom ".format(line))
else:
    print("{} is not palindrom ".format(line))
print("-"*40)