# Chess: Knight walking

# create chessboard
chess = [[0 for i in range(8)] for j in range(8)]

# 8 direction
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

# set first position
st_pos = input("Enter First_pos(x,y): ")
st_pos = st_pos.split(',')
x, y = int(st_pos[1]), int(st_pos[0])

# generate degree_map: n moving methods at the point
degree_map = [[0 for i in range(8)] for j in range(8)]
for i in range(8):
    for j in range(8):
        degree = []
        for k in range(8):
            if 0 <= i + dx[k] <= 7 and 0 <= j + dy[k] <= 7:
                degree.append((i + dx[k], j + dy[k]))
            else:
                continue
        degree_map[i][j] = len(degree)

# for l in range(len(degree_map)):
#     print(degree_map[l]) <- check result

def walk(x, y, chess, degree_map):
    for n in range(8*8):
        degree_map[x][y] = 0
        chess[x][y] = n + 1

        if chess[x][y] == 8*8:
            break

        # find a legal path
        path = []
        for i in range(8):
            if 0 <= x + dx[i] <= 7 and 0 <= y + dy[i] <= 7:
                path.append((dx[i], dy[i]))
            else:
                continue
        
        # minus feasible path
        possible_path = []
        possible_path_degree = []
        for k in range(len(path)):
            degree_map[x + path[k][0]][y + path[k][1]] -= 1
            possible_path.append(path[k])
            possible_path_degree.append(degree_map[x + path[k][0]][y + path[k][1]])
        
        while min(possible_path_degree) < 0:
            min_index = possible_path_degree.index(min(possible_path_degree))
            del possible_path[min_index]
            del possible_path_degree[min_index]
        
        min_index = possible_path_degree.index(min(possible_path_degree))
        move = possible_path[min_index]

        x += move[0]
        y += move[1]
    return chess

result = walk(x, y, chess, degree_map)
for i in range(len(result)):
    for j in range(len(result[i])):
        print("%3d" % result[i][j], end = ' ')
    print('\n')