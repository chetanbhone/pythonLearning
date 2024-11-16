# print even number from 0 to n using for loop
n=int(input("enter your range here"))
if(n<=0):
    print("{} is invalid number")
print("-"*40)
for val in range(2,n+1,2) :   # for even set range from (1 to n+1 wth steping 2)
    print(val)
print("-"*40)