# Find the Greatest Common Denominator of two numbers
# using Euclid's algorithm

def gcd(a,b):
    while(b!=0):
        t = a
        a = b
        b = t % a

    # return a = Because a is A GCD
    return a
# try out the function with a few examples
print(gcd(68,112))  # should be
print(gcd(32,4))    # should be 8
