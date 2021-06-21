"""import csv
import statistics
import math

with open("./Data/class1.csv", newline="") as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)
marks1 = []
for row in data:
    marks1.append(int(row[1]))

mean1 = statistics.mean(marks1)
print("Mean of class 1 is ", mean1)

import pandas
import plotly.express as px

df = pandas.read_csv("./Data/class1.csv")

fig = px.scatter(df, x="Student Number", y="Marks")
fig.update_layout(shapes=[dict(type="line", x0=0, x1=len(marks1), y0=mean1, y1=mean1)])
fig.show()"""

"""Standard Deviation = >
 first of all find the mean of dataset
 second, subtract each data point from the mean and square the difference
 All the squared differences are summed up.
 Divide it by (n-1) where n is number of data points
 finally do the sqaure root of the division."""

"""squared_marks = []
for data in marks1:
    value = mean1 - data
    product = value * value
    squared_marks.append(product)

sum_of_squared_marks = sum(squared_marks)

division_result = sum_of_squared_marks / (len(marks1) - 1)
standard_deviation = math.sqrt(division_result)

print("Standard deviation for class 1 is : ", standard_deviation)"""


import csv
import statistics

with open("./Data/class2.csv", newline="") as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)
marks2 = []
for row in data:
    marks2.append(int(row[1]))

mean2 = statistics.mean(marks2)
print("Mean of class 2 is ", mean2)

import pandas
import plotly.express as px

df = pandas.read_csv("./Data/class2.csv")

fig = px.scatter(df, x="Student Number", y="Marks")
fig.update_layout(shapes=[dict(type="line", x0=0, x1=len(marks2), y0=mean2, y1=mean2)])
fig.show()

"""Standard Deviation = >
first of all find the mean of dataset
second, subtract each data point from the mean and square the difference
All the squared differences are summed up.
Divide it by (n-1) where n is number of data points
finally do the sqaure root of the division."""


import math

products = []
for data in marks2:
    value = mean2 - data
    square = value * value
    products.append(square)

sumOfProducts = sum(products)
division = sumOfProducts / (len(marks2) - 1)
standard_deviation2 = math.sqrt(division)

print("Standard Deviation for class 2 is: ", standard_deviation2)
