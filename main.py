import pandas as pd

# fichiers contenant les fonctions
import time_count
import day_of_week_count
import category_count
import month_count
import district_count
import time_period_count
import location_heatmap

data = pd.read_csv('Police_Department_Incidents_-_Previous_Year__2016_.csv')
data['Time'] = pd.to_datetime(data['Time'], format='%H:%M').dt.time
data['Date'] = pd.to_datetime(data.Date)
