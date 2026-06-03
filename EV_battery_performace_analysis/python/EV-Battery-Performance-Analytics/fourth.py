import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("battery_dataset.csv")

plt.figure(figsize=(10,5))

plt.scatter(df["Cycle"], df["Capacity"])

plt.xlabel("Charge Cycle")
plt.ylabel("Capacity (Ah)")
plt.title("Battery Capacity Degradation Over Cycles")

plt.show()
# command for terminal
# cd "C:\Users\dewan\python\EV-Battery-Performance-Analytics"
#  python fourth.py