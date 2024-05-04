#pie chart
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# import pandas as pd

slices=[60,40]
labels=["stock_A","stock_B"]
plt.pie(slices,labels=labels)
plt.title("Simple pie chart")
plt.show()

