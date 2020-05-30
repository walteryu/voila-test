widgets.link((hist, 'bins'), (slider, 'value'))

fig_lines = plt.figure( title='Line Chart')
lines = plt.plot(x, y)

fig_lines.layout.width = 'auto'
fig_lines.layout.height = 'auto'
fig_hist.layout.width = 'auto'
fig_hist.layout.height = 'auto'

grid_layout = widgets.GridspecLayout(5, 3)

grid_layout[:2, :] = fig_lines
grid_layout[2:4, :] = fig_hist
grid_layout[4, 1] = slider

# grid_layout[:2, :] = fig_lines
# grid_layout[2:4, :] = fig_hist
# grid_layout[4, 1] = slider

grid_layout.layout.height = '1000px'

grid_layout
