# create selector
selector = plt.brush_int_selector()
def update_range(*ignore):
    if selector.selected is not None and len(selector.selected) == 2:
        xmin, xmax = selector.selected
        mask = (x > xmin) & (x < xmax)
        hist.sample = y[mask]
selector.observe(update_range, 'selected')
