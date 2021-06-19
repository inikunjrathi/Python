import csv
from collections import Counter

with open("./Data/SOCR-HeightWeight.csv", newline="") as file:
    reader = csv.reader(file)
    data = list(reader)

data.pop(0)
height = []
for row in data:
    height.append(float(row[1]))


def mean():
    sum = 0.0
    for h in height:
        sum = sum + h
    meanOfHeight = sum / len(height)
    print("Mean of Height: ", meanOfHeight)


def median():
    height.sort()
    if len(height) % 2 == 0:
        median1 = height[int(len(height) / 2)]
        median2 = height[(int(len(height) / 2)) + 1]
        median = (median1 + median2) / 2
        print("Median of Height: ", median)
    elif len(height) % 2 == 1:
        median = height[int(len(height) / 2)]
        print("Median of Height: ", median)


def mode():
    occurences = Counter(height)
    range1 = []
    range2 = []
    range3 = []
    range4 = []
    range5 = []
    for h in height:
        if h >= 50.0 and h <= 60.0:
            range1.append(h)
        elif h > 60.0 and h <= 70.0:
            range2.append(h)
        elif h > 70.0 and h <= 80.0:
            range3.append(h)
        elif h > 80.0 and h <= 90.0:
            range4.append(h)
        elif h > 90.0 and h <= 100.0:
            range5.append(h)

    occurence1 = len(range1)
    occurence2 = len(range2)
    occurence3 = len(range3)
    occurence4 = len(range4)
    occurence5 = len(range5)

    dict = {
        "50 - 60": occurence1,
        "60 - 70": occurence2,
        "70 - 80": occurence3,
        "80 - 90": occurence4,
        "90 - 100": occurence5,
    }
    mode = (60 + 70) / 2
    print("Mode of Height:", mode)


mean()
median()
mode()
