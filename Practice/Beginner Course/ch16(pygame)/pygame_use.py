# url: https://blog.techbridge.cc/2019/10/19/how-to-build-up-game-with-pygame-tutorial/
import pygame

# 啟動pygame
pygame.init()

# 建立繪圖視窗作為圖形顯示區域
# syntax: name = pygame.display.set_mode(windows_size) windows_size is a tuple (width, height)
screen = pygame.display.set_mode((640, 320))

# 設定視窗標題
pygame.display.set_caption("繪圖視窗標題")

# 建立畫布
# syntax: name = pygame.Surface(screen.get_size()) screen.get_size可取得繪圖視窗尺寸
#         name = name.convert()
background = pygame.Surface(screen.get_size())
background = background.convert()

# 為畫布填滿顏色
# syntax: canvas_variable.fill((R,G,B))
background.fill((255, 255, 255))

# 畫布填滿顏色後, 必須以視窗變數的blit方法繪製於視窗中
# syntax: windows_variable.blit(canvas_variable, position) position is tuple(x,y) (0,0)為左上角頂點
screen.blit(background, (0,0))

# 最後要更新繪圖視窗內容, 才能顯示繪製的圖形
# syntax: pygame.display.update()
pygame.display.update()

# 偵測關閉繪圖視窗
# pygame.event為事件處理
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()