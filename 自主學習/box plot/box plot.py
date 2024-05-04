from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
#import
data=pd.read_csv("C:\\William's project code\\matplotlib\\database\\exam\\Expanded_data_with_more_features.csv")
df=pd.DataFrame(data)
plt.style.use('ggplot')

math=df['MathScore']
m1=math.median()
write=df['WritingScore']
m2=write.median()
read=df['ReadingScore']
m3=read.median()
#plot

plt.boxplot([math,write,read], boxprops={'color':'darkgoldenrod', 'linewidth':3}, 
            flierprops={'markersize':4, 'markerfacecolor':'green', 'linestyle':'None'},
            medianprops={'linewidth':2.5, 'color':'skyblue'}, showmeans=False)
plt.text(0.9,m1, f'{m1}')
plt.text(1.9,m2, f'{m2}')
plt.text(2.9,m3, f'{m3}')

plt.xticks([1,2,3], ['Math', 'Writing', 'Reading'])
plt.xlabel('subject')
plt.ylabel('score')
plt.title("Student's exam score", {'font':'Times New Roman', 'size':18})
plt.savefig("Student's exam score")
plt.show()
