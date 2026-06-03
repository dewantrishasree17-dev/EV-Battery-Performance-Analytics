import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("battery_dataset.csv")

plt.figure(figsize=(10,5))

plt.scatter(df["Temperature"], df["SOH"])

plt.xlabel("Temperature (°C)")
plt.ylabel("SOH (%)")
plt.title("Temperature vs Battery Health")

plt.show()
# command for terminal
# cd "C:\Users\dewan\python\EV-Battery-Performance-Analytics"
#  python fifth.py