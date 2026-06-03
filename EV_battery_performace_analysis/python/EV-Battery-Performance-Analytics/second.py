import pandas as pd

df = pd.read_csv("battery_dataset.csv")

print("Average SOH:", round(df["SOH"].mean(),2))
print("Average Capacity:", round(df["Capacity"].mean(),2))
print("Average Voltage:", round(df["Voltage"].mean(),2))
print("Average Temperature:", round(df["Temperature"].mean(),2))
# command for terminal
# cd "C:\Users\dewan\python\EV-Battery-Performance-Analytics"
#  python second.py