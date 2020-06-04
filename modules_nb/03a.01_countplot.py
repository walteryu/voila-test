# 03A.01 - create count plot

# preset plot size
plt.figure(figsize=(12, 8))

# create histogram
def distplot(col, msg):
    # create plot; set size and title
    sns.distplot(col, bins=20, kde=True)
    plt.title(msg)
    plt.show()

distplot(
    df_total['Boardings'],
    'VTA Ridership - Cumulative Monthly Total (2005-2018): Train Boardings'
)

# create countplot and sort categories by value
# https://stackoverflow.com/questions/46623583/seaborn-countplot-order-categories-by-count

# preset plot size
plt.figure(figsize=(12, 8))

def cplot_sort(col, df, sort, msg):
    # create plot; set size and title
    sns.countplot(
        y=col,
        data=df,
        order=sort
    )
    plt.title(msg)
    plt.show()

# set plot size and title
cplot_sort(
    'LineType',
    df_total,
    df_total['LineType'].value_counts().index,
    'VTA Ridership - Cumulative Monthly Total (2005-2018): Train Line Type'
)
