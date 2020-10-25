import pandas as pd
import matplotlib.pyplot as plt


def time_count(data):
    # On regroupe les données par temps, ensuite on converti en delta de temps et on compte les nombre de crimes pour chaque heures. On créé ensuite notre graphique
    by_time = data.groupby(data.Time).size()
    by_time.index = pd.to_timedelta(by_time.index.astype(str))
    by_time = by_time.resample('1H').sum()

    by_time.plot(kind='bar')
    plt.show()
