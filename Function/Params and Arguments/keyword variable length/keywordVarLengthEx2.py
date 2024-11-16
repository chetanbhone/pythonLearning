# program for demonstracting keyword var length
def disp(sno,name,cls,city="PUNE",**kvr):
    print("-"*40)
    print("the number of student is {}".format(sno))
    print("the name of student is {}".format(name))
    print("the class of student is {}".format(cls))
    print("the student belongs to {}".format(city))
    for key, val in kvr.items():
        print("{} ----> {}".format(key,val))
    print("-"*40)

disp(100,"chetan",cls="MCA",city="HYD",demo1="helo",demo2="dear",demo3="love")