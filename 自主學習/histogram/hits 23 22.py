from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
#read
data=pd.read_csv("C:\\William's project code\\matplotlib\\database\\baseball\\All season batting 2023.csv")
df=pd.DataFrame(data)

data2=pd.read_csv("C:\\William's project code\\matplotlib\\database\\baseball\\All season batting 2022.csv")
df2=pd.DataFrame(data2)
#fillna
df=df.fillna(0)
df2=df2.fillna(0)
#avg
avg23=df['BA']
avg22=df2["BA"]
#plot
fig, (ax1, ax2)=plt.subplots(1,2)
#ax1
ax1.hist(avg22, bins=np.linspace(0,0.425, 21), color='skyblue', edgecolor='black')
ax1.set_title('2022')
ax1.set_xlabel('Batting Average')
ax1.set_ylabel('Number of players')
ax1.set_xlim(0,0.435)
ax1.set_ylim(0,200)
#ax2
ax2.hist(avg23, bins=np.linspace(0,0.425, 21), color='skyblue', edgecolor='black')
ax2.set_title('2023')
ax2.set_xlabel('Batting Average')
ax2.set_xlim(0,0.435)
ax2.set_ylim(0,200)


fig.suptitle("Comparing batting average in '22 & '23")
plt.savefig("Comparing batting average in '22 & '23")
plt.show()