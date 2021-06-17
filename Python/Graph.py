import pandas as pd
import plotly.express as pe

df = pd.read_csv("./Data/data.csv")

figure1 = pe.bar(df, x="Country", y="InternetUsers", color="Country")
figure1.show()

df2 = pd.read_csv("./Data/line_chart.csv")

figure2 = pe.line(df2, x="Year", y="Per capita income", color="Country")
figure2.show()

figure3 = pe.scatter(
    df, x="Population", y="Per capita", color="Country", size="Percentage"
)

figure3.show()
