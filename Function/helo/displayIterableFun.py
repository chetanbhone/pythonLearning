#program for display iterable object data
def disp(obj):
    print("-"*50)
    print("type of oject {}".format(type(obj)))
    print("-"*50)
    if(type(obj) in [int,float,bool,complex]):
        print("{} is Non Iterable object format ".format(obj))
    elif(type(obj)!=dict and type(obj) in [str,bytes,bytearray,list,set,frozenset,tuple,range]):
        for val in obj :
            print("\t{}".format(val))
    elif(type(obj)==dict):
        for k , v in obj.items():
            print("\t {} \t{}".format(k,v))
    else:
        print("value of object is {}".format(obj))
    print("-"*50)


a={1:"helo",2:"love",3:"lafda",4:"hoka"}
disp(a)