from pylab import plot, show
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

df1 = pd.read_csv('city_data_sg.csv')
df2 = pd.read_csv('global_data.csv')
df3 = pd.read_csv('city_data_fuzhou.csv')
year_sg, avg_temp_sg = df1['year'], df1['avg_temp']
nor1=(avg_temp_sg-min(avg_temp_sg))/(max(avg_temp_sg)-min(avg_temp_sg))
year_fz, avg_temp_fz = df3['year'], df3['avg_temp']
nor2=(avg_temp_fz-min(avg_temp_fz))/(max(avg_temp_fz)-min(avg_temp_fz))
year_glo, avg_temp_glo = df2['year'], df2['avg_temp']
nor3=(avg_temp_glo-min(avg_temp_glo))/(max(avg_temp_glo)-min(avg_temp_glo))

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(year_sg,avg_temp_sg,'blue',label='Singapore')
axs[0, 0].set_title('Singapore Weather')
axs[0, 0].set_xticks(np.linspace(min(year_sg),max(year_sg),5, endpoint=True))
axs[0, 0].legend(loc=4, fontsize='small')
axs[0, 0].set_ylabel('Temperature ($^\circ$C)')

axs[0, 1].plot(year_fz,avg_temp_fz,'green',label='Fuzhou China')
axs[0, 1].set_title('Fuzhou China Weather')
axs[0, 1].legend(loc=4, fontsize='small')
axs[0, 1].set_ylabel('Temperature ($^\circ$C)')
axs[0, 1].set_xticks(np.linspace(min(year_fz),max(year_fz),5, endpoint=True))

axs[1, 0].plot(year_glo,avg_temp_glo,'red',label='Global')
axs[1, 0].set_title('Global Weather')
axs[1, 0].legend(loc=4, fontsize='small')
axs[1, 0].set_xticks(np.linspace(min(year_glo),max(year_glo),6, endpoint=True))
axs[1, 0].set_xlabel('Year')
axs[1, 0].set_ylabel('Temperature ($^\circ$C)')

axs[1, 1].set_title('Comparison')
axs[1, 1].legend(loc=4, fontsize='small')
axs[1, 1].set_xticks(np.linspace(min(year_glo),max(year_glo),6, endpoint=True))
axs[1, 1].set_xlabel('Year')
axs[1, 1].set_ylabel('Temperature Normalization')
axs[1, 1].plot(year_sg,nor1,'blue',label='Singapore')
axs[1, 1].plot(year_fz,nor2,'green',label='Fuzhou China')
axs[1, 1].plot(year_glo,nor3,'red',label='Global')
plt.subplot_tool()
plt.legend(loc=4, fontsize='small')
plt.show()




