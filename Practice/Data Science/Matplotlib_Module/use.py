# 匯入 matplotlib 
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# 設定樣式
# 使用 plt.style 選用適當且比較美觀的樣式, 設定為classic樣式
plt.style.use('classic')

x = np.linspace(0, 10, 100) # [0, 10]之間產生100個數字
fig = plt.figure()
plt.plot(x, np.sin(x), '-') # '-' 以實線表示
plt.plot(x, np.cos(x), '--') # '--' 以虛線表示

# 儲存圖形到檔案中使用 savefig() 
fig.savefig("./Matplotlib_module/my_figure.png")

plt.show()