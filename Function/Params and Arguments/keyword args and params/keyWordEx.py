# program to demonstrate the keyword arguments
def keywordsArgs (a,b,c,d):
    print("\t\t{}\t\t{}\t\t{}\t\t{}".format(a,b,c,d))
    print("------"*40)

keywordsArgs(b=90,c=100,a=120,d=110)
keywordsArgs(123,234,c=90,d=70)
keywordsArgs(a=10,b=70,c=40,d=100)
