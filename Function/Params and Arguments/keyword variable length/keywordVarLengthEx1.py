# program for demonstracting keyword var length
def disp(**kvr):
    print("-"*40)
    print("the length of kvr is ".format(len(kvr),type(kvr)))
    for key , val in kvr.items():
        print("{} ---> {}".format(key,val))

disp(name="kvr",game="vollyball",price=1000)