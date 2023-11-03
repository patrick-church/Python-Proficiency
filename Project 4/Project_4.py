import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def make_subset(df, region = None, vaccine = None, year = None):
    subset = df.copy()
    if region != None:
        subset = subset.loc[subset['Region'].isin(region)]
    if vaccine != None:
        subset = subset.loc[subset['Vaccine'].isin(vaccine)]
    if year != None:
        subset = subset.loc[subset['Year'].isin(year)]
    return subset


def make_plot(series_object, title = '', bar = True):
    plt.title(title)
    if bar is True:
        return sns.barplot(y = series_object.index, x = series_object.values, orient = 'h')
    if bar is False:
        plt.xticks(rotation = 90)
        return sns.lineplot(x = series_object.index, y = series_object.values)
