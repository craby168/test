import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
days=np.arange(0,11,)
case1=[]
case2=[]
mean=[]

for j in range(11):
    case1.append(np.random.randint(2000,4000))
    case2.append(np.random.randint(2000,4000))
    mean.append(np.random.randint(2750,3250))

fig,(sub0,sub1)=plt.subplots(nrows=1,ncols=2,sharey=True,figsize=(8,4))

# print(f"days={days} /n case1={case1} /n case2={case2}")

sub0.plot(days,case1,marker='H',color='g',label='case1')
sub0.plot(days,mean, marker='D', color='r', label='avg')
sub0.legend(loc='upper left', edgecolor='none')


sub1.plot(days,case2, marker='H', color='blue',label='case2')
sub1.plot(days,mean,marker='D', color='r', label='avg')
sub1.legend(loc='upper right',edgecolor='none')

plt.xlabel('days')
plt.ylabel('value')
plt.title('comparison')
plt.tight_layout()
plt.show()


