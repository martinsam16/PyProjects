from pandas import DataFrame as df

demo = df.from_csv(path="SampleDataset/CountSummaryTraffic.csv")

print(demo.keys())
print(demo.describe())