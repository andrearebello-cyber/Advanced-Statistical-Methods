#t test, normal test, F test
##Student T Test
import math

data = [63,63,64,65,66,69,69,70,70,71]
mu = 65
tabular_t = 2.262

print("Data:",data)
X_bar = sum(data)/len(data)
n = len(data)
print("X BAR:",X_bar)
X_min_X_bar_squ = [(i-X_bar)**2 for i in data]
print("X-X BAR^2:",X_min_X_bar_squ)
total_x_min_xbar = sum(X_min_X_bar_squ)
print("Total X-X^2:",total_x_min_xbar)
print("---------------------------")
print("Calculating SD:")
sd = math.sqrt(total_x_min_xbar/(n-1))
print("Standard Deviation(S,SD):",sd)
print("---------------------------")
print("Formula t = (Xbar - mu)* root(n)/sd")
t = (X_bar - mu) * math.sqrt(n)/sd
print("Calculated T Value :",t)
print("---------------------------")
if (t > tabular_t):
    print("We Reject Hypothesis, Mean is not", mu)
else:
    print("We Accept Hypothesis, Mean is ", mu)
############################################################
##F Test
print("################")
print("F TEST")

sam1 = [60,65,71,74,76,82,85,87]
sam2 = [61,66,67,85,78,63,85,86,88,91]

x1_bar = sum(sam1)/len(sam1)
x2_bar = sum(sam2)/len(sam2)

x1_min_x1_bar_sqr = [(i - x1_bar)**2 for i in sam1]
x2_min_x2_bar_sqr = [(i - x2_bar)**2 for i in sam2]

x1_min_x1_bar_sqr = sum(x1_min_x1_bar_sqr)
x2_min_x2_bar_sqr = sum(x2_min_x2_bar_sqr)
print(x1_min_x1_bar_sqr)
print(x2_min_x2_bar_sqr)

print("Calculating S1^2 and S2^2:")
S1_sqr = x1_min_x1_bar_sqr/(len(sam1) - 1)
S2_sqr = x2_min_x2_bar_sqr/(len(sam2) - 1)

print("S1^2",S1_sqr)
print("S2^2",S2_sqr)

if (S1_sqr > S2_sqr):
    F = S1_sqr/S2_sqr
else:
    F = S2_sqr/S1_sqr

print("Calculated F value:",F)

df1 = len(sam1) - 1
df2 = len(sam2) - 1

print("df1 ", df1," and df2", df2)
