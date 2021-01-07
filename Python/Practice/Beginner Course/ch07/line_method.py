from bokeh.plotting import figure, show
# syntax: figure(...).line(list...[,parameter])
# parameter:
#     line_color: 設定線條顏色
#     line_width: 設定線條寬度
#     line_alpha: 設定線條透明度(0為完全透明, 1.0為完全不透明)
#     line_dash : 設定虛線模式, 其值為一個列表[point, blank] blank的值越小, 虛線會越密集
#     legend: 設定圖例名稱

# figure parameter:
#     title: 設定圖表標題

p = figure(width = 800, height = 400, title = "零用錢統計")
p.title.text_color = "blue"
p.title.text_font_size = "20pt"

p.xaxis.axis_label = "年齡"
p.xaxis.axis_label_text_color = "violet"
p.yaxis.axis_label = "零用錢"
p.yaxis.axis_label_text_color = "violet"

dash = [12, 4]
x1 = [1, 5, 7, 9, 13, 16]
y1 = [15, 50, 80, 40, 70, 50]
x2 = [2, 6, 8, 11, 14, 16]
y2 = [10, 40, 30, 50, 80, 60]
p.line(x1, y1, line_width = 4, line_color = "red", line_alpha = 0.3, line_dash = dash, legend_label = "男性")
p.line(x2, y2, line_width = 4, legend_label = "女性")
show(p)