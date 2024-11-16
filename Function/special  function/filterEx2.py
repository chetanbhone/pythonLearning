# Function to filter positive numbers
pos = lambda x: x > 0
# Function to filter negative numbers
neg = lambda k: k < 0

print("Enter the values for list:")
# Taking input as a list of integers
lst = [int(val) for val in input().split()]

# Filtering positive numbers into a tuple
pslist = tuple(filter(pos, lst))
# Filtering negative numbers into a tuple
nglist = tuple(filter(neg, lst))

print("-----" * 20)
print("Original list:", lst)
print("-----" * 20)
print("List of positive numbers:", pslist)
print("-----" * 20)
print("List of negative numbers:", nglist)
print("-----" * 20)
