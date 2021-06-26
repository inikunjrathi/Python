"""
import random

sum = []

for i in range(1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    sum.append(dice1+dice2)

print(sum)

import plotly.figure_factory as ff

fig = ff.create_distplot([sum], ["Results"], show_hist= False)
fig.show()
"""
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("Data\PRO-C108.csv")

weight = df["Weight(Pounds)"].tolist()
height = df["Height(Inches)"].tolist()

heightgraph = ff.create_distplot([height], ["Height"], show_hist=False)
heightgraph.show()

weightgraph = ff.create_distplot([weight], ["Weight"], show_hist=False)
weightgraph.show()