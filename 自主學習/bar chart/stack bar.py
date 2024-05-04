from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime

plt.figure(figsize=(7,5))
df=pd.DataFrame(pd.read_csv("C:\William's project code\matplotlib\database\Tokyo Medals 2021.csv"))
df=df.sort_values(by='Rank By Total',ascending=False)
df=df.tail(7)
gold=df['Gold Medal']
silver=df['Silver Medal']
bronze=df['Bronze Medal']

x=np.arange(7)
x_label=df['Country']

b=list(np.add(gold,silver))
plt.barh(x, gold, label='Gold',height=0.5)
plt.barh(x, silver, left= gold, label='Silver', height=0.5)
plt.barh(x, bronze, left=b, label='Bronze', height=0.5)


plt.title('Top 5 country ranked by total medals in Tokyo 2020')

plt.legend(edgecolor='none')
plt.xlabel('medals')
plt.yticks(x,list(x_label), fontsize=8, rotation=25)
plt.tight_layout()
plt.savefig('Top 5 country ranked by total medals in Tokyo 2020(stack bar).png')
plt.show()




