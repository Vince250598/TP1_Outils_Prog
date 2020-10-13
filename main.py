import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Police_Department_Incidents_-_Previous_Year__2016_.csv')

data['Time'] = pd.to_datetime(data['Time'], format='%H:%M').dt.time

print(data.info())
print(data['Category'].unique())

by_time = data.groupby(data.index.Time).mean()
hourly_ticks = 4 * 60 * 60 * np.arrange(6)
by_time.plot(xticks=hourly_ticks)
plt.show()

