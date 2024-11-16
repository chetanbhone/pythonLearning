# program for find the special char in line
line = input("Enter your line here: ")
print("-" * 40)
print("The line is: {}".format(line))

splitLine = line.split(" ")
s = ""
noSpaces = s.join(splitLine)
noa = 0
nod = 0
length = len(noSpaces)

for ch in noSpaces:
    if ch.isalpha():
        noa += 1
    elif ch.isdigit():
        nod += 1

special_char = length - (nod + noa)

print("Length: {}".format(length))
print("nod + noa is: {}".format(nod + noa))
print("The number of alphabets in the line is: {}".format(noa))
print("The number of digits in the line is: {}".format(nod))
print("The number of special characters in the line is: {}".format(special_char))
print("-" * 40)

# another logic  CVG
# special_char_count = 0
#     for ch in line:
#         if not ch.isalnum() and not ch.isspace():  # Check if it's not alphanumeric and not a space
#             special_char_count += 1