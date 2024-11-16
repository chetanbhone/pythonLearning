# write a python  program which will generate odd numbers in decreasing order where n is positiven = int(input("Enter your number: "))
n = int(input("Enter your number: "))
if n <= 0:
    print("{} is invalid input".format(n))
else:
    if n % 2 == 0:
        n += 1
    while n >= 1:
        print(n)
        n -= 2
