import pandas as pd

df = pd.read_csv("battery_dataset.csv")

print(df.isnull().sum())
# command for terminal
# cd "C:\Users\dewan\python\EV-Battery-Performance-Analytics"
#  python fourth.py