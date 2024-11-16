# program to demonstrate varaible length args
def demo(*kvr):
    print("-"*40)
    print("the number of values {}".format(len(kvr)))
    for val in kvr:
        print(val)
    print("-"*40)
demo(10,20,30,40)