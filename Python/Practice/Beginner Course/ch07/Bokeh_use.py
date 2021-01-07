from bokeh.plotting import figure, show
fig = figure(width=800, height=400)
listx = [1, 5, 7, 9, 13, 16]
listy = [15, 30, 50, 60, 80, 90]
fig.line(listx, listy)
show(fig)