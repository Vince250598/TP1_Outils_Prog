import matplotlib.pyplot as plt
import numpy as np


def crime_location_heatmap(data):
    newData = data.groupby(['X', 'Y']).size()
    print(newData)

    heatmap, xedges, yedges = np.histogram2d(newData.index.get_level_values('X'), newData.index.get_level_values('Y'),
                                             bins=100)
    extent = [newData.index.get_level_values('X').min(), newData.index.get_level_values('X').max(),
              newData.index.get_level_values('Y').min(), newData.index.get_level_values('Y').max()]

    plt.imshow(heatmap, extent=extent)
    plt.show()
