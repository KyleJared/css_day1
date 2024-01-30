# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:41:35 2024

@author: Jared
"""

"""
Looking at:
    1. Lists
    2. Dictionaries
    3. Data Frames - specific to pandas
"""

import pandas as pd

file = pd.read_csv("country_data.csv")

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
#print("Ave age = ",mean(age))

# gender list
gender = ["M","M","F","M","F","F","F","M","M","F","M"]
print(gender[0])
print(gender[1])
print(gender[2])
print(gender[-1])

#Dictionaries
mammals = {"cat": "a cute animal","lion": "king of the jungle", "elephant": "a gigantic herbivore"}

print(mammals["cat"])

# Data Frames

fruits = ["apple", "banana", "orange", "grape", "kiwi"]
size_nm = [9.8, 10.1, 13.2, 8.7, 20.5]

fruit_size = {
    'fruits': fruits,
    'size': size_nm
    }

fruit_df = pd.DataFrame(fruit_size)

print(fruit_df['fruits'])

print(fruit_df['size'].min())

print(fruit_df[fruit_df["size"] > 10])

prices = [10.00, 12.50, 16.00, 23.00, 7.00]

fruit_df['prices'] = prices

fruit_df.drop(columns=["size"],inplace=True)






