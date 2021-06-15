#!/usr/bin/env python3
import random
from decimal import Decimal

print("Enter the range of values to choose the random prime numbers from below:")

n = int(input("Please enter the start number: "))
m = int(input("Please enter the end number: "))
message = int(input("Please the value of message to encrypt: "))

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

# Calculate n
n = p*q

print("The value of n is:", n)

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

# Calculate the value of the totient
totient = phi(p) * phi(q)
print("The value of the totient is:", totient)

# Calculate e
for e in range(2, totient):
        if gcd(e, totient) == 1:
            break

print("Value of e:",e)
print("Public Key (e,n):", "{ ", e, ",", n, " }")

# function to find extended gcd
def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)

# function to find modular inverse
def modinv(a,m):
	g,x,y = egcd(a,m)
	if g != 1:
		return None
	else:
		return x%m

d = modinv(e, totient)
print("Value of d: ", d)

local_cipher = Decimal(0)
local_cipher = pow(message, e)
cipher_text = local_cipher % n

decrypt_t = Decimal(0)
decrypt_t = pow(cipher_text, d)
decrpyted_text = decrypt_t % n

print("cipher text= "+str(cipher_text))
print("decrypted text= "+str(decrpyted_text))