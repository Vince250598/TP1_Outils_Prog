import pandas as pd
import matplotlib.pyplot as plt


def by_month_count(data):
    # On regroupe les données par date, ensuite on compte pour chaque mois, on trie par ordre descendant et on créé notre graphique à bars
    by_date = data.groupby(data.Date).size()
    by_date.index = pd.to_datetime(by_date.index)
    by_date = by_date.resample('1M').sum()
    by_date.index = by_date.index.month_name()
    by_date = by_date.sort_values(ascending=False)
    by_date.plot(kind='bar')
    plt.show()
