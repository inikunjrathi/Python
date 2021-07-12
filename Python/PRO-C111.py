import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

data = pd.read_csv("Data\data0.csv")
datalist = data["Math_score"].tolist()

fig01 = ff.create_distplot([datalist], ["Math Score"])
# fig.show()

meanofpopulation = statistics.mean(datalist)
medianofpopulation = statistics.median(datalist)
modeofpopulation = statistics.mode(datalist)
stdofpopulation = statistics.stdev(datalist)

print(
    "mean, median and mode and standard deviation of the entire dataset is: ",
    meanofpopulation,
    medianofpopulation,
    modeofpopulation,
    stdofpopulation,
)

# converting the dataset population into normal distribution :
# function to get 1000 random samples.
def samples():
    sampleScores = []
    for i in range(900):
        index = random.randint(0, len(datalist) - 1)
        sampleScores.append(datalist[index])
    meanOfSampleScores = statistics.mean(sampleScores)
    return meanOfSampleScores


samplingDistribution = []
for i in range(800):
    mean = samples()
    samplingDistribution.append(mean)

meanOfSamplingDistribution = statistics.mean(samplingDistribution)
medianOfSamplingDistribution = statistics.median(samplingDistribution)
modeOfSamplingDistribution = statistics.mode(samplingDistribution)
stdOfSamplingDistribution = statistics.stdev(samplingDistribution)
print(
    "After doing sampling distribution: \n",
    meanOfSamplingDistribution,
    medianOfSamplingDistribution,
    modeOfSamplingDistribution,
)

# first standard deviation
fstart, fend = (
    meanOfSamplingDistribution - stdOfSamplingDistribution,
    meanOfSamplingDistribution + stdOfSamplingDistribution,
)
sstart, send = (
    meanOfSamplingDistribution - 2 * stdOfSamplingDistribution,
    meanOfSamplingDistribution + 2 * stdOfSamplingDistribution,
)
tstart, tend = (
    meanOfSamplingDistribution - 3 * stdOfSamplingDistribution,
    meanOfSamplingDistribution + 3 * stdOfSamplingDistribution,
)


# first intervention
dataofintervention1 = pd.read_csv("Data/data1.csv")
listofintervention1 = dataofintervention1["Math_score"].tolist()
meanoffirstintervention = statistics.mean(listofintervention1)
fig2 = ff.create_distplot(
    [samplingDistribution], ["Sampled Distribution"], show_hist=False
)
fig2.add_trace(
    go.Scatter(
        x=[meanOfSamplingDistribution, meanOfSamplingDistribution],
        y=[0, 1],
        mode="lines",
        name="MEAN OF SAMPLING DISTRIBUTION",
    )
)
fig2.add_trace(
    go.Scatter(
        x=[meanoffirstintervention, meanoffirstintervention],
        y=[0, 1],
        mode="lines",
        name="MEAN OF FIRST INTERVENTION",
    )
)


# second intervention
dataofintervention2 = pd.read_csv("Data/data.csv")
listofintervention2 = dataofintervention1["Math_score"].tolist()
meanofsecondintervention = statistics.mean(listofintervention2)
fig3 = ff.create_distplot(
    [samplingDistribution], ["Sampled Distribution"], show_hist=False
)
fig3.add_trace(
    go.Scatter(
        x=[meanOfSamplingDistribution, meanOfSamplingDistribution],
        y=[0, 1],
        mode="lines",
        name="MEAN OF SAMPLING DISTRIBUTION",
    )
)
fig3.add_trace(
    go.Scatter(
        x=[meanoffirstintervention, meanoffirstintervention],
        y=[0, 1],
        mode="lines",
        name="MEAN OF FIRST INTERVENTION",
    )
)
fig3.add_trace(
    go.Scatter(
        x=[meanofsecondintervention, meanofsecondintervention],
        y=[0, 1],
        mode="lines",
        name="MEAN OF SECOND INTERVENTION",
    )
)
fig3.show()
