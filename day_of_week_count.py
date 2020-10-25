import matplotlib.pyplot as plt


def day_of_week_count(data):
    # regroupement des données selon le jour de la semaine et on tri par ordre descendant pour faciliter la lecture du graphique à bars
    by_day_of_week = data.groupby(data.DayOfWeek).size()
    by_day_of_week = by_day_of_week.sort_values(ascending=False)
    by_day_of_week.plot(kind='bar')
    plt.show()
