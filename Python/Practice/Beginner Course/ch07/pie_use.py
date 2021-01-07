import matplotlib.pyplot as plt
# pie 為 圓餅圖
# syntax: [modulename].pie(data,[parameter...])
# parameter: 
#     labels : 每一個項目標題組成的列表
#     colors : 每一個項目顏色組成的列表
#     explode: 每一個項目凸出數值的元組, 0代表正常顯示 (執行就知道了)
#     labeldistance: 項目標題與圓心的距離是半徑的多少倍
#     autopct: 項目百分比的格式, "% integer.float %%" integer 為幾位整數, float為幾位小數
#     shadow: 布林值, True表示圖形有陰影
#     startangle: 開始繪圖的起始角度 (右邊為0度逆時針旋轉)
#     pctdistance: 百分比文字與圓心的距離是半徑的多少倍 

label = ['East', 'South', 'North', 'West']
sizes = [5, 10, 20, 15]
color = ["red", "green", "blue", "yellow"]
explodes = (0, 0, 0.05, 0)
plt.pie(sizes, explode = explodes, labels = label, colors = color, \
    labeldistance = 1.1, autopct = "%3.1f%%", shadow = True, \
    startangle = 90, pctdistance = 0.6)
plt.axis("equal") # 讓x, y軸的單位相等
plt.legend()
plt.show()

