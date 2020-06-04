# 03B.02 - create time series

# set plot size and title
plt.figure(figsize=(18, 12))

# create time series plot
def time_series(x_col, y_col, df, msg):
    sns.lineplot(
        x=x_col,
        y=y_col,
        data=df
    )
    plt.title(msg)
    plt.xticks(rotation=45)
    plt.show()

time_series(
    'Period',
    'Boardings',
    df_total,
    'VTA Ridership - Cumulative Monthly Total (2005-2018): Train Boardings by Line Type'
)
