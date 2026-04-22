import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather.csv")

plt.figure(figsize=(8,5), num="Vertical")
plt.bar(df["Month"], df["Temperature"])
plt.xlabel("Month")
plt.ylabel("t")
plt.title("The temperature for each month")


plt.figure(figsize=(8,5), num="Horizontal")
plt.barh(df["Month"], df["Temperature"])
plt.xlabel("t")
plt.ylabel("Month")
plt.title("The temperature for each month")


plt.figure(figsize=(8,5), num="Line Graph")
plt.plot(df["Month"], df["Temperature"], marker="o")
plt.xlabel("Month")
plt.ylabel("t")
plt.title("The temperature for each month")

plt.show()