# validation for marks
while(True):
    marks=input("enter your number here")
    if(marks.isdigit() and int(marks) in range(1,101)):
        print("marks of student is {}".format(marks))
        break
    print("{} is invalid marks".format(marks))