# program for accepting a line of text and find the lenggth of each word
def getline():
    line=input("enter your line here")
    return line
def wordsLength(line):
    words=line.split(" ")
    for word in words:
        print("{} ---> {}".format(word,len(word)))

line=getline()
wordsLength(line)



