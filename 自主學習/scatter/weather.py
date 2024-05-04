from matplotlib import pyplot as plt
import pandas as pd
plt.style.use('ggplot')
#import
data=pd.read_csv("C:\\William's project code\\matplotlib\\database\\insurance.csv")
df=pd.DataFrame(data)
charge=df['charges']
age=df['age']
bmi=df['bmi']
#plot
plt.scatter(bmi, charge, c=age, cmap='viridis', s=5)

plt.title('Correlations among age, BMI and insurance charges',fontdict={'font':'Times New Roman', 'size':14})
plt.xlabel('BMI', fontdict={'font':'Times New Roman'})
plt.ylabel('charges', fontdict={'font':'Times New Roman'})
plt.colorbar(label="age", )
plt.savefig('Correlations among age, BMI and insurance charges.png')
plt.show()
