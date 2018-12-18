# Find the greatest common denominator of two numbers
# Using Euclid's Algorithm


def gcd(a, b):
    while (b != 0):
        t = a
        a = b
        b = t % b

    return a

# Examples
print(gcd(60, 96)) # should be 12
print(gcd(20, 8)) # should be 4
