
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.dates as mdates

df=pd.read_csv("C:\William's project code\matplotlib\database\covid\day_wise.csv")
data=pd.DataFrame(data)
df=data.head(100)
print(df)
com=df["New cases"]
dea=df["New deaths"]


t=pd.to_datetime(df["Date"])


plt.plot_date(t,com,label="New Reported cases",color="r",linestyle="solid",markersize="0.5")
print(t)
plt.plot_date(t,dea,label="New Reported Deaths",color="b",linestyle="solid",markersize="0.5")

# fmt = mdates.DateFormatter('%b, %d %Y') # define the formatting
# plt.gca().xaxis.set_major_formatter(fmt) # apply the format to the desired axis
# plt.gcf().autofmt_xdate()

plt.legend()
plt.title("Covid-19 Comfirmed cases and Deaths")
plt.xlabel("Date")
plt.ylabel("headcount")
plt.yticks(rotation=20)
plt.xticks(rotation=40)
plt.tight_layout()
plt.savefig("Covid-19 Comfirmed cases and Deaths.jpg")
plt.show()


