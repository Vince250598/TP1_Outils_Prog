import matplotlib.pyplot as plt


def by_district_count(data):
    by_district = data.groupby(data.PdDistrict).size()
    by_district = by_district.sort_values(ascending=False)
    by_district.plot(kind='bar')
    plt.show()
