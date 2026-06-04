#Analysis of Variance
##AVONA ONE WAY
import math

data = [[8,10,7,14,11],[7,5,10,9,9],[12,9,13,12,14]]

n = len(data)

x_bars = [sum(i)/len(i) for i in data]

x_bar_bar = sum(x_bars)/n

print("--------------------------------")
print("Variance Between sample:")

total_ssc = [ ((i - x_bar_bar)**2)*len(data[0]) for i in x_bars]
total_ssc = sum(total_ssc)
print("Sum of squares between samples:",total_ssc)
msc = total_ssc/(len(data)-1) #MSC = SSC/C-1
print("Mean Sum of squares between samples:",msc)

print("--------------------------------")
print("Variance Within sample:")
total_sse_s = [[(j - x_bars[data.index(i)])**2 for j in i] for i in data]
total_sse = [sum(i) for i in total_sse_s]
##for i in data:
##    for j in i:
##        print(data.index(i))
##        print((j - x_bars[data.index(i)])**2)
total_sse = sum(total_sse)
print("Sum of squares within samples:",total_sse)
total_n = len(data) * len(data[0]) #COL * ROW

mse = total_sse/(total_n - (len(data))) #MSE = SSE/n-c
print("Mean Sum of squares within samples:",mse)

print("--------------------------------")
print("Calculating F:")
F = msc/mse
print("Calculated F Value is",F)
