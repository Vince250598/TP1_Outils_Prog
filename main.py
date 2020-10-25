import pandas as pd

# fichiers contenant les fonctions
import time_count
import day_of_week_count
import category_count
import month_count
import district_count
import time_period_count
import location_heatmap

# Lecture du csv
data = pd.read_csv('Police_Department_Incidents_-_Previous_Year__2016_.csv')

# conversion aux bon formats des données de type date
data['Time'] = pd.to_datetime(data['Time'], format='%H:%M').dt.time
data['Date'] = pd.to_datetime(data.Date)
