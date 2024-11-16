# global keyowrd in python
a=10
def incr():
    global a # whenever we modifiy global varaibale value we have to use global
    a=10+1
    print(a)
incr()