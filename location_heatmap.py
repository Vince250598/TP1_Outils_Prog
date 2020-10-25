import matplotlib.pyplot as plt
import numpy as np


def crime_location_heatmap(data):
    # On regroupe les données par coordonnées X,Y et on compte les valeur pour chacune
    newData = data.groupby(['X', 'Y']).size()

    # On créé notre histogram2d, on défini les limites du graphiques et on créé notre graphique heatmap
    heatmap, xedges, yedges = np.histogram2d(newData.index.get_level_values('X'), newData.index.get_level_values('Y'),
                                             bins=100)
    extent = [newData.index.get_level_values('X').min(), newData.index.get_level_values('X').max(),
              newData.index.get_level_values('Y').min(), newData.index.get_level_values('Y').max()]

    plt.imshow(heatmap, extent=extent)
    plt.show()
