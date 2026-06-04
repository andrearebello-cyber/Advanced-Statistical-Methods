#Property plotting of binomial distribution
import math
import matplotlib.pyplot as plt

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
n = int(input("Enter N (Number of trials):"))
p = float(input("Enter P (Probability of success):"))
r = int(input("Enter r (Number of success in N trial):"))

print("Mean:",n * p)
print("SD:", math.sqrt(n * p * p - 1))
##print(BD(6,1/2,4) * 100 ,"Chance")
print(BD(n,p,r) * 100 ," % Chance")

print("-----------------------------------")
rangee = list(range(n + 1))
print(rangee)
proba_range = [BD(n,p,i) for i in rangee]
print(proba_range)

plt.plot(rangee,proba_range)
plt.bar(rangee,proba_range)
plt.xlabel("Number of Trials")
plt.ylabel("% of Success")
plt.show()
