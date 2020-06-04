# 03A.02 - create bar plot

# create countplot
plt.figure(figsize=(6, 30))

# aggregate and sort for plot
# https://gist.github.com/fomightez/bb5a9c727d93d1508187677b4d74d7c1
def barplot(y_col, x_col, df, msg):
    sns.barplot(
        y=y_col,
        x=x_col,
        data=df
    )
    plt.title(msg)
    plt.show()

df_total_sort = df_total.groupby(['Period_date'])['Boardings'].aggregate(np.median).reset_index()
barplot(
    'Period_date',
    'Boardings',
    df_total_sort,
    'VTA Ridership - Cumulative Monthly Total (2005-2018): Train Boardings by Date'
)
