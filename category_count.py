import matplotlib.pyplot as plt


def category_count(data):
    by_category = data.groupby(data.Category).size()
    by_category = by_category.sort_values(ascending=False)
    by_category.plot(kind='bar')
    plt.yscale('log')
    plt.show()
