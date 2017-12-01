## 2. Introduction To The Data ##

import pandas as pd
unrate = pd.read_csv("unrate.csv")
unrate["DATE"] = pd.to_datetime(unrate["DATE"])

print(unrate.head(12))

## 6. Introduction to Matplotlib ##

import matplotlib.pyplot as plt

plt.plot()
plt.show()

## 7. Adding Data ##

import matplotlib.pyplot as pt

pt.plot(unrate["DATE"][:12], unrate["VALUE"][:12])

## 8. Fixing Axis Ticks ##

plt.plot

import matplotlib.pyplot as pt

pt.plot(unrate["DATE"][:12], unrate["VALUE"][:12])
pt.xticks(rotation=90)

## 9. Adding Axis Labels And A Title ##

plt.plot

import matplotlib.pyplot as pt

pt.plot(unrate["DATE"][:12], unrate["VALUE"][:12])
pt.xticks(rotation=90)
pt.xlabel("Month")
pt.ylabel("Unemployment Rate")
pt.title("Monthly Unemployment Trends, 1948")