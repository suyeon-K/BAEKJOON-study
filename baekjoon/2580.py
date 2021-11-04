import sys

sudoku = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]
zeros = [(i,j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

def is_possible(i,j):
    nums = [1,2,3,4,5,6,7,8,9]

    # 가로 세로 없애기
    for k in range(9):
        if sudoku[i][k] in nums:
            nums.remove(sudoku[i][k])
        if sudoku[k][j] in nums:
            nums.remove(sudoku[k][j])

    # 3*3 없애기
    i //= 3
    j //= 3

    for p in range(i*3, (i+1)*3):
        for q in range(j*3, (j+1)*3):
            if sudoku[p][q] in nums:
                nums.remove(sudoku[p][q])

    return nums

solve = False

def solution(x): 
    global solve

    if solve:
        return
    
    if x == len(zeros):
        for row in sudoku:
            print(*row)
        solve = True
        return
    else:
        (i,j) = zeros[x]
        possible_nums = is_possible(i,j)

        for num in possible_nums:
            sudoku[i][j] = num
            solution(x+1)
            sudoku[i][j] = 0

solution(0)