# generate some fake data
def seed_data(n):
    # n = 5000
    x = np.linspace(0.0, 10.0, n)
    np.random.seed(0)
    y = np.cumsum(np.random.randn(n)*10).astype(int)
    return(x,y)

x, y = seed_data(2000)
