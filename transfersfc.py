import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'TransferData.csv')
TeamValues = df.groupby(['Joined','Year'])['Values'].sum()
Barcelona = TeamValues['FC Barcelona']
Real = TeamValues['Real Madrid']

bar_cumul = [0]
real_cumul = [0]
for price in Barcelona:
    bar_cumul.append(bar_cumul[-1] + price)
for price in Real:
    real_cumul.append(real_cumul[-1] + price)

bar_cumul.pop(0)
real_cumul.pop(0)
    
Barcelona = Barcelona.rename('Values').reset_index()
Real = Real.rename('Values').reset_index()
Barcelona['Cumulative'] = bar_cumul
Real['Cumulative'] = real_cumul

fig, ax = plt.subplots()

years = list(range(1980, 2020))

plt.plot(Barcelona['Year'], Barcelona['Cumulative'], color = "#A70042", label = "FC Barcelona")
plt.plot(Real['Year'], Real['Cumulative'], color = "#FEBE10", label = "Real Madrid")
plt.legend(loc="upper left", prop = {'size': 12})

plt.xlabel('Year', fontsize = 20)
plt.ylabel('Transfer Value(£ millions)', fontsize = 20)
plt.title('Barcelona vs Real Madrid Transfers', fontsize = 30)
plt.xticks(range(1980, 2021, 2) ,fontsize=12)
plt.yticks(fontsize=12)

plt.grid()
ax.xaxis.grid(color='#F8F8F8')
ax.yaxis.grid(color='#F8F8F8')


ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

fig.set_size_inches(21, 12, forward=True)
fig.savefig('BarcelonaVsRealMadridCumul.png', dpi=100)