# program for generating multiplication table for n positive number using nested loop concept
n=int(input("enter how many numbers of table you want"))
if(n<0):
    print("{} is invalid input".format(n))
else:
    for i in range(1,n+1):
        print("multiplication table of {}".format(i))
        for j in range(1,11):
            print("{} *{} = {}".format(i,j,i*j))
    else:
      print("-"*40)