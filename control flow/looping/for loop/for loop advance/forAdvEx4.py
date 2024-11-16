# find factorial for given number using while loop - logic 4
n = int(input("Enter a number for factorial: "))
print("-" * 40)

if n < 0:
    print("{} is invalid".format(n))
elif n == 0:
    print("{} factorial is 1".format(n))
else:
    fact = 1
    tn = n  # Keep the original value of n
    while n > 0:
        fact *= n
        n -= 1
print("{} factorial is {}".format(tn, fact))

print("-" * 40)

