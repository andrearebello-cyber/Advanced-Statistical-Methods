#Problems based on normal distribution

# Importing required libraries
 
import numpy as np
import matplotlib.pyplot as plt
 
# Creating a series of data of in range of 1-50.
x = np.linspace(1,50,200)

print(x)
#Creating a Function.
def normal_dist(x , mean , sd):
    prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
    return prob_density

def SND(x,u,sd):
    return (x-u)/sd
 
#Calculate mean and Standard deviation.
mean = np.mean(x)
sd = np.std(x)
print("Mean :",mean)
print("SD :",sd)
#Apply function to the data.
pdf = normal_dist(x,mean,sd)
print("PDF",pdf)
print("--------------------------")
print("Standard Normal Distribution")
print("Formula:")
print("Z = (X-U)/SD")
print("--------------------------")
print("Mean : ", 30)
print("SD : ", 5)
print("Therefore, Z = ",SND(26,30,5))

# # Function to calculate Standard Normal Distribution (Z-score)
# def SND(x, u, sd):
#     return (x - u) / sd 

# print("--------------------------")
# print("Standard Normal Distribution")
# print("Formula: Z = (X - U) / SD") 

# # Taking User Inputs
# try:
#     X = float(input("Enter the value of X (observation): "))
#     U = float(input("Enter the value of U (Mean): "))
#     SD = float(input("Enter the value of SD (Standard Deviation): "))

#     # Calculating Z
#     Z = SND(X, U, SD)

#     print("--------------------------")
#     print(f"Results for X={X}, Mean={U}, SD={SD}:")
#     print(f"Therefore, Z = {Z}") 
#     print("--------------------------")

# except ValueError:
#     print("Please enter valid numerical values.")