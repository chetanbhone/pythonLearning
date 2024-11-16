# check palindrom or not
print("enter a words seperated by spaces")
lst=[val for val in input().split(",")]
print("Given words {}".format(lst))
palwords=tuple(filter(lambda word: word==word[::-1],lst))
print("palindrom words {}".format(palwords))