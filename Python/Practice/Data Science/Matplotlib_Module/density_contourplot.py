import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.use('seaborn-white')
# 有時候使用等高線或是色彩編碼區域在二維空間中顯示三維資料是很有用的
# Matplotlib 有三個函式可以做到這樣的工作
# plt.contour: 建立等高線圖
# plt.contourf: 建立填色的等高線圖
# plt.imshow: 用來顯示影像

# 三維函數視覺化
# 使用一個函數 z = f(x, y) 展示等高線圖的開始, f為一個陣列broadcasting的例子
def f(x, y):
    return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)

# 等高線圖可以被使用 plt.contour 函式來建立, 它使用3個參數: 格線的x值, y值, z值
# x, y值表示繪圖的位置, z值會被用來當等高層使用
# 或者使用 np.meshgrid的函式 它可以從一維陣列建立一個二維的網格
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# 現在來看看使用標準線條的等高線圖
# plt.contour(X, Y, Z, colors = 'black')

# 預設的情況下, 當使用了一個顏色負值會以虛線來表示, 正值以實線來表示
# 可以透過 cmap 參數 指定一個色彩對應表來對線條進行色彩編碼
# 指定畫出更多的線條, (在資料範圍中繪出20條相同間隔的線)
# plt.contour(X, Y, Z, 20, cmap = 'RdGy')

# RdGy 是 紅色灰階的縮寫, 若要置中的資料, 這個是不錯的選擇
# Matplotlib 有非常多的色彩對應表可以使用, 可以使用ipython 輸入plt.cm.<TAB>來瀏覽

# 使用plt.contourf() 實心等高線圖, 和plt.contour()語法大致相同
# 此外加上 plt.colorbar() 命令, 它可以自動建立額外具有顏色刻度的軸
# plt.contourf(X, Y, Z, 20, cmap = 'RdGy')
# plt.colorbar() # 在 scatterplot 有使用到

# 用上面的方法圖形可能沒有這麼好看, 因為顏色的步進值比較難散而沒有那麼連續, 
# 雖然可以設定等高線數目到一個非常高的值來修正問題, 但是會變得沒有效率. 
# 因為Matplotlib需要在每一階每一步重新繪製新的多邊形, 
# 一個比較好的函式 plt.imshow() 它把資料的二維格點當作一個影像

# plt.imshow(Z, extent = [0, 5, 0, 5], origin = 'lower', cmap = 'RdGy')
# plt.colorbar()
# plt.axis(aspect = 'image') # 課本寫 aspect, 實際上就是value參數

# 使用 imshow() 有一些潛在的狀況
# plt.show() 不接受x, y格點, 因此必須要手動指定在圖表上的影像範圍[xmin, xmax, ymin, ymax]
# plt.imshow() 預設是遵循標準的影像陣列定義, 原點是在左上, 而不是像一般的等高線圖是在左下角
# 使用格點資料時必須要進行轉換
# plt.imshow() 將會自動調整軸的外觀比例以符合輸入的資料, 可以透過設定來改變
# Ex. plt.axis(aspect = 'image') 讓x, y的單位符合

# 合併等高線圖和影像圖是很有用的(地理)
# 使用alpha 設定透明度, 加上等高線圖和標籤, 使用plt.clabel()
contours = plt.contour(X, Y, Z, 5, color = 'black')
plt.clabel(contours, inline = True, fontsize = 8)

plt.imshow(Z, extent = [0, 5, 0, 5], origin = 'lower', cmap = 'Greens', alpha = 0.5)
plt.colorbar()
# 把等高線標籤疊放在影像檔上面

plt.show()
