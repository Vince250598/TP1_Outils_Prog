import matplotlib.pyplot as plt


def by_district_count(data):
    # On regroupe les données par le district du poste de police, on trie dans l'ordre descendant et on créé notre graphique à bars
    by_district = data.groupby(data.PdDistrict).size()
    by_district = by_district.sort_values(ascending=False)
    by_district.plot(kind='bar')
    plt.show()
