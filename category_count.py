import matplotlib.pyplot as plt


def category_count(data):
    # regroupement des données par categorie du crime, ensuite on tri par ordre descendant, on créé le graphique à bars et on met l'axe des y sur une échelle logarithmique
    by_category = data.groupby(data.Category).size()
    by_category = by_category.sort_values(ascending=False)
    by_category.plot(kind='bar')
    plt.yscale('log')
    plt.show()
