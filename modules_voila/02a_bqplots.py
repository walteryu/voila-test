# generate some fake data
def seed_data(n):
    # n = 5000
    x = np.linspace(0.0, 10.0, n)
    np.random.seed(0)
    y = np.cumsum(np.random.randn(n)*10).astype(int)
    return(x,y)

x, y = seed_data(2000)

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
