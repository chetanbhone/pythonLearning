# program for find the word for line
line=input("enter your line here")
words=line.split()
print("-"*40)
for word in words:
    print(word)
print("-"*40)
numw=len(words)
print("the number of words in line is {}".format(numw))
print("-"*40)