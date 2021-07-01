import pandas as pd
import plotly.figure_factory as ff
import statistics

df = pd.read_csv("Data\PRO-C108.csv")

weight = df["Weight(Pounds)"].tolist()
height = df["Height(Inches)"].tolist()

mean = statistics.mean(weight)
median = statistics.median(weight)
mode = statistics.mode(weight)

print(mean)
print(median)
print(mode)

stddev = statistics.stdev(weight)
print(stddev)

# 1st stddev
lower = mean - stddev
upper = mean + stddev

weight1 = []
for w in weight:
    if w >= lower and w <= upper:
        weight1.append(w)

# percentage of data lying in 1st stddev
percentage1 = (len(weight1) / len(weight)) * 100
print(percentage1)

# 2nd stddev
lower2 = mean - (2 * stddev)
upper2 = mean + (2 * stddev)

weight2 = []
for w in weight:
    if w >= lower2 and w <= upper2:
        weight2.append(w)

# percentage of data lying in 2st stddev
percentage2 = (len(weight2) / len(weight)) * 100
print(percentage2)

# 3rd stddev
lower3 = mean - (3 * stddev)
upper3 = mean + (3 * stddev)

weight3 = []
for w in weight:
    if w >= lower3 and w <= upper3:
        weight3.append(w)

# percentage of data lying in 3rd stddev
percentage3 = (len(weight3) / len(weight)) * 100
print(percentage3)

weightgraph = ff.create_distplot([weight], ["Weight"], show_hist=False)
weightgraph.show()
