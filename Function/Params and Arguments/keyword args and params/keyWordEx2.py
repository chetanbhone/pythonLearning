# program for demonstarte keyword length argument with default params
def keywordArgs(a,b,c,d="MH"):
    print("\t\t{}\t\t{}\t\t{}\t\t{}".format(a,b,c,d))
keywordArgs(90,80,d="hyd",c=100)
keywordArgs(d="hyd",a=90,b=80,c=100)
keywordArgs(a=90,b=80,c=100,d="hyd")
keywordArgs(80,90,c=100,d="hyd")