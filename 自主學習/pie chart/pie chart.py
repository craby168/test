#pie chart
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

plt.style.use("fivethirtyeight")
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode=[0,0,0,0,0]

plt.pie(slices,labels=labels,explode=explode,autopct="%1.1F%%",
       )
 # wedgeprops={'edgecolor':'black'}
plt.title("Dev for each language")
plt.savefig("各程式語言使用人數")
plt.show()
