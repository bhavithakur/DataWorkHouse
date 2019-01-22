mport pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig,ax=plt.subplots()
def animate(i):
	data = pd.read_csv("C:\\finacnialData.csv")
	byPeriod = data.groupby('Period')
	netSales = byPeriod.apply(lambda x:x[x['FinancialElements']=='Net Sales']['Amount'].sum())
	period=pd.unique(data.Period.ravel())
	index=np.arrange(len(period))
	ax.clear()
	ax.plot(index,netSales,'r')
	plt.xticks(index,period,rotation='vertical')
	plt.title("Month Wise Total Expenditure")
	ax.set_xlabel("Month")
	ax.set_ylabel("Net Amount")

ani=animation.FuncAnimation(fig,animate,interval=500)
plt.show()
