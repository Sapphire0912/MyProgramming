# 使用 DFS

import numpy as np

def random_maze(maze, m, n):
    if maze != 0:
        print(maze.index)


def set_size(m, n):
    # 設定隨意大小的迷宮
    maze = np.random.randint(0, 2, (m, n))
    return random_maze(maze, m, n)

def main():
    # 格式(x y)
    size = input("設定產生mxn的迷宮: ")
    size = size.split(' ')
    m, n = int(size[0]), int(size[1])
    set_size(m, n)

main()