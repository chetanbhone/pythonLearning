# program for accepting a line of text and find length of each word
def getline():
    line=input("enter your line here...")
    return line
def getWordsLength():
    line=getline()
    words=line.split()
    return words
def countWordsLength():
    words=getWordsLength()
    if(len(words)==0):
        print("No data is present")
    else:
        d={}    # empty dictionary
        for word in words:
            d[word]=len(word) # passing value to key
        else:
            print("-"*40)
            for word, wordlen in d.items():
                print("{} ---> {}".format(word,wordlen))
            print("-"*40)

countWordsLength()