import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def time_count(data):
    by_time = data.groupby(data.Time).size()
    by_time.index = pd.to_timedelta(by_time.index.astype(str))
    by_time = by_time.resample('1H').sum()

    by_time.plot(kind='bar')
    plt.show()


def day_of_week_count(data):
    by_day_of_week = data.groupby(data.DayOfWeek).size()
    by_day_of_week.plot(kind='bar')
    plt.show()


def category_count(data):
    by_category = data.groupby(data.Category).size()
    by_category.plot(kind='bar')
    plt.yscale('log')
    plt.show()


def by_month_count(data):
    by_date = data.groupby(data.Date).size()
    by_date.index = pd.to_datetime(by_date.index)
    by_date = by_date.resample('1M').sum()
    by_date.index = by_date.index.month_name()
    by_date.plot(kind='bar')
    plt.show()


def by_district_count(data):
    by_district = data.groupby(data.PdDistrict).size()
    by_district.plot(kind='bar')
    plt.show()


data = pd.read_csv('Police_Department_Incidents_-_Previous_Year__2016_.csv')
data['Time'] = pd.to_datetime(data['Time'], format='%H:%M').dt.time
print(data.info())





