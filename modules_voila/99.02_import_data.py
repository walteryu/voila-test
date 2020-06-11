# import data
import pandas as pd
df_total = pd.read_csv('../data/Ridership_by_Route_Cumulative_Monthly.csv')

# generate some fake
# n = 2000
# x = np.linspace(0.0, 10.0, n)
# np.random.seed(0)
# y = np.cumsum(np.random.randn(n)*10).astype(int)

# vta open data
x = df_total['Routes']
y = df_total['Boardings']
