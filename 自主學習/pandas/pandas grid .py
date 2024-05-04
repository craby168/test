import pandas as pd
br_list=pd.read_csv("C:\William's project code\matplotlib\自主學習\BR.csv")

data=pd.DataFrame(br_list)
sort1=data.sort_values(by=["OPS","BA"], ascending=False)

print(sort1.loc[:,['Tm','BA','OPS']])



