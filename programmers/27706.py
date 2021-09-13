def up(task, x, y, row, col):
    d = 0
    if task == "L":
        y = (y+1) % col
        d= 4
    elif task == "R":
        y = (y+col-1) % col
        d = 2
    else:
        x = (x+1) % row
        d=3
    return x,y,d
        
def down(task, x, y, row, col):
    d= 0
    if task == "R":
        y = (y+1) % col
        d = 4
    elif task == "L":
        y = (y+col-1) % col
        d = 2
    else:
        print(x,row,(x+row-1) % row)
        x = (x+row-1) % row
        d = 1
        
    return x,y,d
        
def right(task, x, y, row, col):
    d = 0
    if task == "L":
        x = (x+row-1) % row
        d = 3
    elif task == "R":
        x = (x+1) % row
        d = 1
    else:
        y = (y+col-1) % col
        d = 2
    return x,y,d
        
def left(task, x, y, row, col):
    if task == "R":
        x = (x+row-1) % row
        d = 3
    elif task == "L":
        x = (x+1) % row
        d= 1
    else:
        y = (y+1) % col
        d = 4
    return x,y,d
        
def solution(grid):
    answer = []
    x,y = 0,0
    direction = 0
    
    row_len = len(grid[0])
    col_len = len(grid)
    

    for i in range(1,5):

        dir_grid = []
        for row in range(len(grid)):
            temp = []
            for col in range(len(grid[row])):
                temp.append(0)
            dir_grid.append(temp)

        direction = i
        count = 0

        while (True):
            dir_grid[x][y] += 1
            temp = True
            for row in dir_grid:
                for i in row:
                    if i < 2:
                        temp = False

            if temp:
                answer.append(count)
                break

            count +=1

            if direction == 1:
                x,y,direction = down(grid[x][y],x,y,row_len, col_len)
            elif direction == 2:
                x,y,direction = right(grid[x][y],x,y,row_len, col_len)
            elif direction == 3:
                x,y,direction = up(grid[x][y],x,y,row_len, col_len)
            elif direction == 4:
                x,y,direction = left(grid[x][y],x,y,row_len, col_len)
            
            
    
    return answer

        

# def solution(grid):
#     answer = []
#     x,y = 0,0
#     direction = 0
    
#     row_len = len(grid[0])
#     col_len = len(grid)
#     print(row_len,col_len)
    

#     for i in range(1,5):

#         dir_grid = []
#         for row in range(len(grid)):
#             temp = []
#             for col in range(len(grid[row])):
#                 temp.append([0,0,0,0])
#             dir_grid.append(temp)

#         direction = i
#         print("intial direction : ",direction)
#         count = 0
#         while (True):
#             dir_grid[x][y][direction-1] += 1
#             print(dir_grid)
#             if dir_grid[x][y][direction-1] == 3:
#                 if x == 0 & y == 0:
#                     for row in range(len(grid)):
#                         for col in range(len(grid[row])):
#                             if sum(dir_grid[row][col]) <3:
#                                 break
#                     answer.append(count)
#                 break

#             print("\nbefore : ",x,y)
#             print("direction : ",direction)
#             count +=1
#             if direction == 1:
#                 x,y,direction = down(grid[x][y],x,y,row_len, col_len)
#             elif direction == 2:
#                 x,y,direction = right(grid[x][y],x,y,row_len, col_len)
#             elif direction == 3:
#                 x,y,direction = up(grid[x][y],x,y,row_len, col_len)
#             elif direction == 4:
#                 x,y,direction = left(grid[x][y],x,y,row_len, col_len)
            
#             print("after : ",x,y)

#             print()
            
    
#     return answer

print(solution(["S"]))
# print(solution(["SL","LR"]))

# print(solution(["R","R"]))