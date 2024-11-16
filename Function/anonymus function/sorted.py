# make list in accending and decending order
sortnames= lambda names: sorted(names)
print("enter names seperated by commas")
lst=[val for val in input().split(",")]
accending = sortnames(lst)
print(accending)
print(accending[::-1])