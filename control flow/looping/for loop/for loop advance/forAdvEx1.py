# Find factorial of a given number using for loop - logic 1
n = int(input("Enter a number for factorial: "))
print("-" * 40)

if n < 0:
    print("{} is a negative number".format(n))
elif n == 0:
    print("{} factorial is 1".format(n))
else:
    fact = 1
    for i in range(1, n + 1):  # Start from 1 to n (not 0 to n+1)
        fact *= i
print("The factorial of {} is {}".format(n, fact))

print("-" * 40)
