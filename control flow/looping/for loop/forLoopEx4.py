# print word in string in reverse order ( iterable oject - range )
word=input("enter your string here")
print("-"*40)
for k in range(len(word)-1,-1,-1):   #using positive indexing
    print(word[k])
print("-"*40)
#     # or with negative indexing
# for k in range(-1,-(len(word)+1),-1):
#     print(word[k])