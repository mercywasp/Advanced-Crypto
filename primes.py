#!/usr/bin/env python3
import random

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

print('Generated random prime numbers: ', randomPrime)
print("The value of p is: ", p)
print("The value of q is: ", q)