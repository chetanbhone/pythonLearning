n = int(input("Enter your number here: "))
if n < 0:
    print("{} is invalid input".format(n))
else:
    if n % 2 != 0:
        n -= 1  # Adjust n to be even if it's odd
while n >= 2:
    print(n)
    n -= 2  # Decrease by 2 to get the next even number
