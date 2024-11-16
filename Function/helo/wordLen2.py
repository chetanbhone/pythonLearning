# program for geting words from line and find length of words
def getline():
    line=input("enter your line here")
    return line
def wordLen():
    line=getline()
    words=line.split()
    for word in words:
        print("{} ---> {}".format(word,len(word)))
wordLen()