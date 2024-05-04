from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

data=pd.read_csv("C:\\William's project code\\matplotlib\\database\\diabetes_prediction_dataset.csv"
                 )
df=pd.DataFrame(data)
#processing
m=[]
f=[]
d_m=[]
d_f=[]

# for i in range(len(df)):
#     if df.iloc[i]["gender"]=='Male' and df.iloc[i]["diabetes"]==0:
#         m.append(df.iloc[i]['blood_glucose_level'])
#     elif df.iloc[i]["gender"]=='Female' and df.iloc[i]["diabetes"]==0:
#         f.append(df.iloc[i]['blood_glucose_level'])    
#     elif df.iloc[i]["gender"]=='Male' and df.iloc[i]["diabetes"]==1:
#         d_m.append(df.iloc[i]['blood_glucose_level'])
#     elif df.iloc[i]["gender"]=='Female' and df.iloc[i]["diabetes"]==1:
#         d_f.append(df.iloc[i]['blood_glucose_level'])

m = df[(df['age'] <45) & (df['diabetes'] == 0)]['blood_glucose_level'].tolist()
f = df[(df['age'] >=45) & (df['diabetes'] == 0)]['blood_glucose_level'].tolist()
d_m = df[(df['age'] <45) & (df['diabetes'] == 1)]['blood_glucose_level'].tolist()
d_f = df[(df['age'] >=45) & (df['diabetes'] == 1)]['blood_glucose_level'].tolist()

#plot
plt.violinplot([m,f,d_m,d_f])

plt.text(0.85,205,"under 45")
plt.text(1.8,205, "over 45")
plt.text(2.85,113, "under 45")
plt.text(3.8,113, "over 45")
plt.title("Blood glucose level regarding patients age and diabetes condition", pad=20)
plt.gcf().text(0.45, 0.9, "unit:mg/dL", fontdict={'size':10})
plt.ylabel("Glucose level")
plt.xticks([1.5, 3.5], ["Without diabetes", "With diabetes"])
plt.savefig("Blood glucose level regarding patients' age and diabetes condition.png")
plt.show()
