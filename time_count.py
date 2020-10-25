import pandas as pd
import matplotlib.pyplot as plt


def time_count(data):
    by_time = data.groupby(data.Time).size()
    by_time.index = pd.to_timedelta(by_time.index.astype(str))
    by_time = by_time.resample('1H').sum()

    by_time.plot(kind='bar')
    plt.show()
