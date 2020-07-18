from bokeh.plotting import show, figure, output_file
# syntax: output_file("filename.html")
# ^可以自訂網頁名稱(修改網址的部分)
output_file("lineout.html")
p = figure(width = 800, height = 400)
listx = [1, 5, 7, 9, 13, 16]
listy = [15, 30, 50, 60, 80, 90]
p.line(listx, listy)
show(p)