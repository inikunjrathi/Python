import plotly.express as px
import csv
import numpy as np

"""
with open(
    "Data\Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv",
    newline="",
) as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)

icecreamsales = []
temperature = []

for row in data:
    temperature.append(float(row[0]))
    icecreamsales.append(float(row[1]))

fig = px.scatter(x = temperature, y = icecreamsales)
fig.show()

coorelation = np.corrcoef(temperature, icecreamsales)
print(coorelation[1,0])
"""
"""
with open("Data\cups of coffee vs hours of sleep.csv", newline="") as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)

coffee = []
sleep = []
weeks = []

for row in data:
    coffee.append(float(row[1]))
    sleep.append(float(row[2]))
    weeks.append(float(row[0]))

fig = px.bar(x=coffee, y=sleep, color=weeks)
fig.show()
correlation = np.corrcoef(coffee, sleep)
print(correlation[0, 1])
"""
with open(
    "Data\Size of TV,_Average time spent watching TV in a week (hours).csv", newline=""
) as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)

size = []
time = []

for row in data:
    size.append(float(row[0]))
    time.append(float(row[1]))

fig = px.bar(x=size, y=time, color=size)
fig.show()
correlation = np.corrcoef(size, time)
print(correlation[0, 1])
