#import_csv
from matplotlib import pyplot as plt
# import numpy as np
# import pandas as pd
# from collections import Counter

# plt.style.use("dark_background")
data=pd.read_csv("https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Matplotlib/02-BarCharts/data.csv")
ids=data["Responder_id"]
res=data["LanguagesWorkedWith"]

count=Counter()

for lang in res:  
    count.update(lang.split(";"))
    
language=[]
popularity=[]

for item in count.most_common(10):
    language.append(item[1])
    popularity.append(item[0])

language.reverse()
popularity.reverse()
plt.barh(popularity,language,color="r")
# plt.ylabel("Language")
plt.xlabel("people")

plt.xkcd()
plt.savefig("dev language")
