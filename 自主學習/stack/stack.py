#stack chart
from matplotlib import pyplot as plt
import numpy as np


minutes=[1,2,3,4,5,6,7,8,9]

player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

labels=["player1","player2","player3"]
colors=["g","r","b"]

plt.stackplot(minutes,player1,player2,player3,labels=labels,colors=colors)

plt.legend(loc="lower left")
plt.title("Stack chart")
plt.show()
plt.savefig("stack chart")