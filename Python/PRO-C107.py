import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("Data\PRO-C107.csv")

mean = df.groupby("level")["attempt"].mean()
print(mean)

fig = go.Figure(
    go.Bar(x=mean, y=["Level 1", "Level 2", "Level 3", "Level 4"], orientation="h")
)
# fig.show()

# Analysis of performance of student TRL_987
studentDF = df.loc[df["student_id"] == "TRL_987"]

mean2 = studentDF.groupby("level")["attempt"].mean()
print(mean2)

fig2 = go.Figure(
    go.Line(x=["Level 1", "Level 2", "Level 3", "Level 4"], y=mean2)
)
fig2.show()