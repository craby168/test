#import_csv
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter
from datetime import datetime

plt.style.use("ggplot")
data=pd.read_csv("C:\William's project code\matplotlib\database\covid\day_wise.csv")
df=pd.DataFrame(data).head(100)

date=pd.to_datetime(df["Date"])
df["Date"]=date
print(date)
fig=plt.figure(figsize=(7,4))
plt.bar(df["Date"], df['Confirmed'], color='r' )
plt.gcf().text(0.82, 0.05, 'credit:kaggle.com',fontsize=8)
plt.gcf().text(0.45, 0.87, 'from 1/22~4/30',fontsize=8)

plt.title('Confirmed cases in the US by date', pad=20)
plt.xlabel('Date')
plt.xticks(rotation=20, fontsize=6)
plt.ylabel('Cases(Mil)')
plt.tight_layout()
plt.savefig('Confirmed cases in US first 100 days')
plt.show()
