import pandas as pd
import statistics
import plotly.figure_factory as ff
import random

average = pd.read_csv("Data/newdata.csv")
score = average["average"].tolist()

meanOfPopulation = statistics.mean(score)
medianOfPopulation = statistics.median(score)
modeOfPopulation = statistics.mode(score)
print(meanOfPopulation, medianOfPopulation, modeOfPopulation)

# function to get 1000 random samples.
def samples():
    sampleScores = []
    for i in range(900):
        index = random.randint(0, len(score) - 1)
        sampleScores.append(score[index])
    meanOfSampleScores = statistics.mean(sampleScores)
    return meanOfSampleScores


samplingDistribution = []
for i in range(800):
    mean = samples()
    samplingDistribution.append(mean)

meanOfSamplingDistribution = statistics.mean(samplingDistribution)
medianOfSamplingDistribution = statistics.median(samplingDistribution)
modeOfSamplingDistribution = statistics.mode(samplingDistribution)
print(
    "After doing sampling distribution: \n",
    meanOfSamplingDistribution,
    medianOfSamplingDistribution,
    modeOfSamplingDistribution,
)

fig1 = ff.create_distplot([samplingDistribution], ["Average Scores"], show_hist=False)
fig1.show()
