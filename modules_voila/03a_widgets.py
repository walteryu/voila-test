# tutorial code for widget implementation
# source: https://github.com/voila-gallery/ipympl/blob/master/ipympl.ipynb

# note: change var name to avoid conflict with bqplot
import matplotlib.pyplot as mplt

# Enabling the `widget` backend.
# This requires jupyter-matplotlib a.k.a. ipympl.
# ipympl can be install via pip or conda.
%matplotlib widget

# Testing matplotlib interactions with a simple plot
fig = mplt.figure()
mplt.plot(np.sin(np.linspace(0, 20, 100)));
