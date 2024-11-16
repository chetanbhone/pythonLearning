# prpogram for demonstracting globals
a=100
def demo():
    a=10
    dictobj=globals()
    print("invisible global variables")
    for g ,v in dictobj.items():
        print("{} ---- {}".format(g,v))
    print("-"*40)
    print("local variable value of a is {}".format(a))
    print("-"*40)
    print("global variable value of a is {}".format(dictobj['a']))   # type 1
    print("global variable value of a is {}".format(dictobj.get('a')))  # type 2
    print("globl variable value of a is {}".format(globals()['a']))   # type 3
    print("global variable value of a is {}".format(globals().get('a')))   # type 3
demo()