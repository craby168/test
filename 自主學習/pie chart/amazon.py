from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
#import
fig=plt.figure(figsize=(8,5))
df=pd.read_csv("C:\\William's project code\\matplotlib\\database\\Amazon\\Amazon Sale Report.csv")
# df.fillna(0, inplace=True)
se=kur=wes=top=eth=blo=bot=sar=dup=0
#catoggorize
for i in range(1,len(df)):
    if df.iloc[i]['Category']=='Set':
        se+=df.iloc[i]['Amount'] 
    elif df.iloc[i]['Category']=='Kurta':
        kur+=df.iloc[i]['Amount']
    elif df.iloc[i]['Category']=='Western Dress':
        wes+=df.iloc[i]['Amount'] 
    elif df.iloc[i]['Category']=='Top':
        top+=df.iloc[i]['Amount'] 
    elif df.iloc[i]['Category']=='Ethnic Dress':
        eth+=df.iloc[i]['Amount']  
    elif df.iloc[i]['Category']=='Blouse':
        blo+=df.iloc[i]['Amount'] 
    elif df.iloc[i]['Category']=='Bottom':
        bot+=df.iloc[i]['Amount']
    elif df.iloc[i]['Category']=='Saree':
        sar+=df.iloc[i]['Amount']  
    elif df.iloc[i]['Category']=='Dupatta':
        dup+=df.iloc[i]['Amount']       
    else:
        continue
#set variables
cat=['Set', 'Western Dress', 'Top', 'others']
amount=[int(se),int(wes),int(top),int(eth)+int(blo)+int(bot)+int(sar)+int(dup)]
print(amount)
#plt!
# plt.pie(amount, labels=cat, startangle=90, shadow=True, counterclock=False,explode=[0,0,0,0.2], 
#         autopct=lambda p:f"{int((p*sum(amount)/100)/1000)}k ({p:.1f}%)", 
#         textprops={'font':"times new roman"}, wedgeprops={'edgecolor':'white'})

# plt.title('Amazon sales data',pad=20, fontdict={'size':'18'})
# plt.gcf().text(0.12, 0.03, 'source:https://www.kaggle.com/datasets/thedevastator/unlock-profits-with-e-commerce-sales-data')
# plt.savefig('Amazon.png')
# plt.show()



 

# plt.pie(rev, labels=com, startangle=90, shadow=True, counterclock=False, 
#         autopct=lambda p:f"{int(p*sum(rev)/100)} ({p:.1f}%)", explode=[0,0,0,0,0,0.15], 
#         textprops={'font':"times new roman"}, wedgeprops={'edgecolor':'black'})


# plt.title('Top 6 tech company revenue (in billion)', pad=13)
# plt.gcf().text(0.8, 0.1, 'source:Copilot', fontdict={'font':"times new roman", 'size':'7'})
# plt.savefig('Top 6 tech company revenue (in billion).jpg')
# plt.show()


