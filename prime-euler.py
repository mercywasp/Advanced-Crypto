#!/usr/bin/env python3
import random

print("Enter the range of values to choose the random prime numbers from below.")

n = int(input("Please enter the start number: "))
m = int(input("Please enter the end number: "))


def primesInRange(n, m):
    prime_list = []
    for i in range(n, m):
        isPrime = True

        for num in range(2, i):
            if i % num == 0:
                isPrime = False
                
        if isPrime:
            prime_list.append(i)
    return prime_list

prime_list = primesInRange(n, m)
randomPrime = random.choices(prime_list, k=2)

p = randomPrime[0]
q = randomPrime[1]

print("The value of p is: ", p)
print("The value of q is: ", q)

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

print("phi(",p,") = ", phi(p), sep = "")
print("phi(",q,") = ", phi(q), sep = "")
