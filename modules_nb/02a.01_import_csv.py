# 02A.01 - load data into notebook

# load data via file
# Source data: https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv
df_total = pd.read_csv('../data/Ridership_by_Route_Cumulative_Monthly.csv')

# load data via url
# https://stackoverflow.com/questions/32400867/pandas-read-csv-from-url/41880513#41880513
# url = ""
# df_total = pd.read_csv(url)

# filter by line type
# https://stackoverflow.com/questions/11869910/pandas-filter-rows-of-dataframe-with-operator-chaining
df_core = df_total[df_total['LineType'] == 'Core']

# output table info
def data_profile(df, msg):
    print(msg, '\n')
    print('Dataframe Shape:', df.shape, '\n')
    print(df.info(), '\n')
    print('Dataframe Data Types:\n')
    print(df.dtypes, '\n')

# data profile
data_profile(
    df_total,
    '*** Table Info: VTA Ridership - Cumulative Monthly Total from 2005-2018 ***'
)

# output unique values
def show_unique(col, msg):
    print('\n', msg, '\n')
    print(col.unique())

show_unique(
    df_total['Routes'],
    '*** Unique Values: VTA Ridership - Train Route ***'
)
show_unique(
    df_total['LineType'],
    '*** Unique Values: VTA Ridership - Train Line Type ***'
)

# output summary stats
def summary_stats(col, msg):
    print('\n', msg, '\n')
    print(col.describe())

summary_stats(
    df_total['Boardings'],
    '*** Summary Stats: VTA Ridership - Train Boardings for All Routes ***'
)
summary_stats(
    df_core['Boardings'],
    '*** Summary Stats: VTA Ridership - Train Boardings for Core Lines ***'
)
