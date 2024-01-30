# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 09:43:33 2024

@author: Jared
"""

import pandas

print("\n Country \n")

file = pandas.read_csv("country_data.csv")

print(file)

print(file.info())

print(file.describe())

print("\n Iris \n")

file2 = pandas.read_csv("iris.csv")

print(file2)

print(file2.info())

print(file2.describe())

print("\n Insurance \n")

file3 = pandas.read_csv("insurance_data.csv",skiprows=5)

print(file3)

print(file3.info())

print(file3.describe())

print("The file 'insurance_data.csv' is not read.It is not in a readable .csv format. The skip function of pandas has been used")

print("\n Housing \n")

#col_names = ["A","B","C"]

#file4 = pandas.read_csv("housing_data.csv",names=col_names)

#print(file4)

#print(file4.info())

#print(file4.describe())

print("Data coulmns do not have headings, so the first data line is used as a column heading")

print("\n Diab \n")

file5 = pandas.read_csv("diab_data.csv")

print(file5)

print(file5.info())

print(file5.describe())



#Storing Data in Python

print("\n This is a new section \n")

# Using Lists
age = [30,40,30,49,22,35,22,46,29,25,39]
print(age)

# Lists indexes start at 0 which has the value of 30
print(age[0])
print(age[1])
print(age[10])

# This will give an error as there is no value at index 11
#print(age[11])

#Basic Statistics
print("Min age = ",min(age))
print("Max age = ",max(age))
print("Len age = ",len(age))
print("Sum age = ",sum(age))
average = sum(age)/len(age)
print("Ave age = ",average)

# gender list
gender = ["M","M","F","M","F","F","F","M","M","F","M"]
print(gender[0])
print(gender[1])
print(gender[2])
print(gender[-1])

#Check out pycuda for using an Nvidia GPU for computations
