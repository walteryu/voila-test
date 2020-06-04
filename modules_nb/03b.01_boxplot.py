# 03B.01 - create box plots

# set plot size and title
plt.figure(figsize=(16, 12))

# create boxplot
def boxplot(y_col, x_col, df, msg):
    sns.boxplot(
        y=y_col,
        x=x_col,
        data=df
    )
    plt.title(msg)
    plt.show()

boxplot(
    "LineType",
    "Boardings",
    df_total,
    'VTA Ridership - Cumulative Monthly Total (2005-2018): Train Boardings by Line Type'
)

# create heatmap
# remove duplicates:
# https://stackoverflow.com/questions/13035764/remove-rows-with-duplicate-indices-pandas-dataframe-and-timeseries
# df_total = df_total.loc[~df_total.index.duplicated(keep='first')]
# df_total = df_total.pivot('DayofWeek', 'Period', 'Boardings')
# sns.heatmap(df_total)
