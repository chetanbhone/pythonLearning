# program to demonstrte variable length arguments with positional arguments
def disp(sno,name,*kvr):
    print("-"*40)
    print("\t\tstudent number is {}".format(sno))
    print("\t\tname of the student is {}".format(name))
    print("\t\tlength of touple is {}".format(len(kvr)))
    for val in kvr:
        print("\t\t\t{}".format(val),type(val))
    print("-"*40)

disp(100,"chetan","helo",1,2,3,4,2+3j,2.13)
