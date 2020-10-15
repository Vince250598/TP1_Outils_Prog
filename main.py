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


def crimes_by_time_period(data):
    top10 = data.Category.value_counts()[:10].index.tolist()
    data_top10_categories = data[data['Category'].isin(top10)]
    print(data_top10_categories.Category.unique())

    by_time_crime = data_top10_categories.groupby(['Time', 'Category'])
    agg_counts = by_time_crime.size().unstack()
    agg_counts.index = pd.to_timedelta(agg_counts.index.astype(str))
    agg_counts = agg_counts.resample('4H').sum()

    agg_counts = agg_counts.div(agg_counts.sum(axis=1), axis=0)

    agg_counts.plot(kind='bar')
    plt.legend(bbox_to_anchor=(0, 1), loc='upper left', ncol=3)
    plt.show()


data = pd.read_csv('Police_Department_Incidents_-_Previous_Year__2016_.csv')
data['Time'] = pd.to_datetime(data['Time'], format='%H:%M').dt.time
print(data.info())
