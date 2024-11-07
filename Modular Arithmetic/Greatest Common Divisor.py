#this code will calculate gcd
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Test the code with a = 12 and b = 8
print(f"The GCD of 12 and 8 is {gcd(12, 8)}")

# Calculate gcd(a, b) for a = 66528 and b = 52920
a = 66528
b = 52920
print(f"The GCD of {a} and {b} is {gcd(a, b)}")
