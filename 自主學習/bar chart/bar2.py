import numpy as np
from matplotlib import pyplot as plt
import pandas as pd 

plt.style.use("ggplot")
df=pd.DataFrame(pd.read_csv("C:\William's project code\matplotlib\database\Rankings.csv"))

data=df.sort_values(by='W',ascending=False)
fig=plt.figure(figsize=(13,6))
data['Rk']=[31-k for k in data["Rk"]]
plt.barh(data['Rk'], data['W'], color='blue', height=0.75)
for i in range(30):
    plt.text(data['W'][i], data['Rk'][i]-0.25,str(data['W'][i]))

plt.title('Rk and Wins for each team in 2023')
plt.xlabel('wins',fontsize=15)
plt.yticks(data['Rk'],data['Tm'],fontsize= 8)
plt.gcf().text(0.77,0.04, 'credit:Baseball Reference')
plt.show()
# print(data.loc[:,["Tm",'W','L','W-L%','Rdiff','Luck']])