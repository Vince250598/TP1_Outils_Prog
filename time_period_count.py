import pandas as pd
import matplotlib.pyplot as plt


def crimes_by_time_period(data):
    # On récupère le top 10 des category où il y a le plus crime
    top10 = data.Category.value_counts()[:10].index.tolist()
    data_top10_categories = data[data['Category'].isin(top10)]
    print(data_top10_categories.Category.unique())

    # On regroupe par temps et categorie et on compte les crimes par categorie poiur chaque tranche de 4 heures
    by_time_crime = data_top10_categories.groupby(['Time', 'Category'])
    agg_counts = by_time_crime.size().unstack()
    agg_counts.index = pd.to_timedelta(agg_counts.index.astype(str))
    agg_counts = agg_counts.resample('4H').sum()

    # On ramène le tout en pourcentage et on créé notre graphique à bar multiples
    agg_counts = agg_counts.div(agg_counts.sum(axis=1), axis=0)

    agg_counts.plot(kind='bar')
    plt.legend(bbox_to_anchor=(0, 1), loc='upper left', ncol=3)
    plt.show()
