from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

bmi=[]
color=[]
data=pd.read_csv("C:\\William's project code\\matplotlib\\database\\All_seasons.csv", 
                 encoding='latin1', on_bad_lines='skip')
df=pd.DataFrame(data)

h=df["player_height"]
w=df["player_weight"]
for i in range(len(h)):
   b=0
   b=float(w[i])/(float(h[i])/100)**2
   bmi.append(b)


plt.scatter(h,w,c=bmi,s=30, edgecolor="black",alpha=0.25, cmap="rainbow")
bar=plt.colorbar(label="BMI")


plt.title("NBA players' Height,Weight and BMI ")
plt.xlabel("Height(cm)")
plt.ylabel("Weight(kg)")
plt.tight_layout()
plt.savefig("Scatter nba.png")
plt.show()