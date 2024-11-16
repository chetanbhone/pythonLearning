# program for taking words from keyboard and finding their length
print("enter your words here...")
obj={ word:len(word) for word in input().split(",")}
for word , len in obj.items():
    print("{} -----> {}".format(word,len))