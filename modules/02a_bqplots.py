# generate some fake data
n = 5000
x = np.linspace(0.0, 10.0, n)
np.random.seed(0)
y = np.cumsum(np.random.randn(n)*10).astype(int)

# create histogram
fig_hist = plt.figure(title='Histogram')
hist = plt.hist(y, bins=25)
hist.bins = 10;

# create histogram slider
slider = widgets.IntSlider(description='Bins number', min=1, max=100, v_model=30)
