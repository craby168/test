import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data=pd.read_csv("https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Matplotlib/06-Histograms/data.csv")
ages=data["Age"]

plt.style.use("fivethirtyeight")
bins=[0,10,20,30,40,50,60,70,80,90]
plt.hist(ages,bins=bins,color="b",edgecolor="black")

plt.xlabel("Ages")
plt.ylabel("Responders")
plt.title("Responders per age")
plt.savefig("survey(histogram)")
plt.show()
