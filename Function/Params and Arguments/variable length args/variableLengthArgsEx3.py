# program to demonstrate variable length args with postitional args and default arguments
def disp(sno,name,*kvr,branch="MCA"):
    print("number of student is {}".format(sno))
    print("the name of student is {}".format(name))
    for val in kvr:
        print(val)
    print("student belong to {}".format(branch))

disp(1001,"snehal",10,20,30,40,branch="BCA")
