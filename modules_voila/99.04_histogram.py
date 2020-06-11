# create histogram
fig_hist = plt.figure(title='Histogram')
hist = plt.hist(y, bins=25)

# histogram bins
hist.bins = 10;

# create histogram slider
slider = widgets.IntSlider(
    description='Bins number',
    min=1,
    max=100,
    v_model=30
)
