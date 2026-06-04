#Problems based on binomial distribution
import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def BD(n,p,r):
    q = 1 - p
    return nCr(n,r) * p**r * q**(n-r)

print("Binomial distribution")
print("Formula:")
print("P(r) = nCr * p^r * q^(n-r)")
print("-----------------------------------")
n = int(input("Enter N (Number of trials):")) #takes integer
p = float(input("Enter P (Probability of success):"))
r = int(input("Enter r (Number of success in N trial):"))

print("Mean:",n * p)
print("SD:", math.sqrt(n * p * (1-p)))
##print(BD(6,1/2,4) * 100 ,"Chance")
print(BD(n,p,r) * 100 ," % Chance")

print("-----------------------------------")
