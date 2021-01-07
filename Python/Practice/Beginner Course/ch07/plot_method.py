import matplotlib.pyplot as plt
listx1 = [1, 5, 7, 9, 13, 16]
listy1 = [15, 50, 80, 40, 70, 50]
plt.plot(listx1, listy1, label = "Male")

listx2 = [2, 6, 8, 11, 14, 16]
listy2 = [10, 40, 30, 50, 80, 60]
plt.plot(listx2, listy2, color = "red", linewidth = 5, linestyle = "dashdot", label = "Female")
plt.legend() # 設定label屬性 就需要加這行才可以使用

# 設定 x,y 軸的範圍
plt.xlim(0, 20)  # x 0~20
plt.ylim(0, 100) # y 0~100

plt.title("Pocket Money") # 設定圖表標題
plt.xlabel("Age") # 設定x軸的標題
plt.ylabel("Money") # 設定y軸的標題

plt.show()