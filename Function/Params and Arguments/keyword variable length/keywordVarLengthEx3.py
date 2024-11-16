# program to demonstrate keyword varibale length with * and ** use
def disp(sno,name,cls,*kvr,city="PUNE",**love):
    print("-"*40)
    print("positional arguments ")
    print("the number of student is {} ".format(sno))
    print("the name of student is {}".format(name))
    print("the student belongs to {}".format(cls))
    print("-"*40)
    print("variable length arguments")
    for val in kvr:
        print(val)
    print("-"*40)
    print("default arguemnts ")
    print("the student lives in {}".format(city))
    print("-"*40)
    print("keyword variable length auguments")
    for key , val in love.items():
        print("{} ----> {}".format(key,val))

disp(100,"chetan","MCA",10,20,30,40,demo1="helo",demo2="dear",demo3="love",city="Banglore")