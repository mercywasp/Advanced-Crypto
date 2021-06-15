#!/usr/bin/env python3

n = int(input("Please enter the value of n number: "))

# Function to return gcd of a and b
def gcd(a, b):
 
    if (a == 0):
        return b
    return gcd(b % a, a)
 
# Euler Totient Function
def phi(n):
 
    result = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result+=1
    return result

print("phi(",n,") = ", phi(n), sep = "")

