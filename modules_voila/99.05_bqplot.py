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

# create histogram
fig_hist = plt.figure(
    title='VTA Train Boardings - Monthly Cumulative Total from 2005-2018'
)
hist = plt.hist(y, bins=25)

# vta data page layout
widgets.link((hist, 'bins'), (slider, 'value'))

fig_lines = plt.figure( title='Line Chart')
lines = plt.plot(x, y)

fig_lines.layout.width = 'auto'
fig_lines.layout.height = 'auto'
fig_hist.layout.width = 'auto'
fig_hist.layout.height = 'auto'

grid_layout = widgets.GridspecLayout(5, 2)

# grid_layout[:2, :] = fig_lines
# grid_layout[2:4, :] = fig_hist
grid_layout[:2, :] = fig_hist
grid_layout[2, 1] = slider

grid_layout.layout.height = '1000px'

grid_layout
