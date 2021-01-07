from bokeh.plotting import figure, show
# syntax: [modulename].figure(...).circle(list_x,list_y[,parameter])
# parameter:
#     size: 若為一個數值, 表示每個點的大小相同; 若是一個列表, 表示每個點依序指定每個點的大小
#     color: 同上, 更改點的顏色
#     alpha: 同上, 更改點的透明度(0 ~ 1.0數字越大越不透明)

p = figure(width = 800, height = 400) 
p.title.text_font_size = "18pt"
p.xaxis.axis_label = "X 軸"
p.yaxis.axis_label = "Y 軸"
x = [1, 5, 7, 9, 13, 16]
y = [15, 50, 80, 40, 70, 50]
sizes = [10, 20, 30, 30, 20, 10]
colors = ["red", "blue", "purple", "gray", "orange", "pink"]
p.circle(x, y, size = sizes, color = colors, alpha = 0.5)
show(p)

# Extra: 散點圖的其他點的形狀
#   circle, circle_x, circle_cross
#   square, square_x, square_cross
#   inverted_triangle, triangle
#   asterisk, cross, x
#   ...etc.