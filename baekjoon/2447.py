def star(n):
    if n == 3:
        for i in range(n):
            for j in range(n):
                if (i%3 == 1) and (j%3 == 1):
                    print(" ",end="")
                else:
                    print("*", end="")
            print()
    else:
        for i in range(3):
            for j in range(3):
                if (i%3 == 1) and (j%3 == 1):
                    print(" ",end="")
                else:
                    star(n//3)
            print()
        
star(9)

# 풀이 1 : 시간초과
import sys
from typing import Mapping

N = int(sys.stdin.readline())

def star(x,y,n):
    if ((x//n)%3 == 1) and ((y//n)%3 == 1):
        print(" ",end="")
    else:
        if n // 3 == 0:
            print("*",end="")
        else:
            star(x,y,n//3)


for i in range(N):
    for j in range(N):
        star(i,j,N)
    print()


# 풀이 2

import sys

N = int(sys.stdin.readline())

def draw_star(n) :
    global Map
    
    if n == 3 :
        Map[0][:3] = Map[2][:3] = [1]*3
        Map[1][:3] = [1, 0, 1]
        return

    a = n//3

    draw_star(a)

    for i in range(3) :
        for j in range(3) :
            if i == 1 and j == 1 :
                continue
            for k in range(a) :
                Map[a*i+k][a*j:a*(j+1)] = Map[k][:a] # 핵심 아이디어

Map = [[0 for i in range(N)] for i in range(N)]

draw_star(N)

for i in Map :
    for j in i :
        if j :
            print('*', end = '')
        else :
            print(' ', end = '')
    print()


# 풀이 3
from sys import*
setrecursionlimit(10**6)
def draw(x, y, n):
   if n == 1:
       dohwaji[x][y]='*'
       return
   div = int(n/3)            #더 작은 부분 그릴 때 n을 3으로 나눈 값
   #기본패턴의 8가지 좌표를 시작으로 더 작은 부분을 그림
   draw(x, y, div)
   draw(x, y+div, div)
   draw(x, y+div+div, div)
   draw(x+div, y, div)
   draw(x+div, y+div+div, div)
   draw(x+div+div, y, div)
   draw(x+div+div, y+div, div)
   draw(x+div+div, y+div+div, div)

#    for i in range(3):
#     for j in range(3):
#        if i==1 and j==1: continue  #(x+1, y+1)은 그리지 않고 건너 뜀
#        draw(x+div*i, y+div*j, div)


n=int(input())
dohwaji = [[' 'for i in range(n)] for _ in range(n)]
draw(0, 0, n)                #(0,0)을 시작좌표로, n만큼의 길이의 모양 그림
for i in range(n):           

   print(''.join(dohwaji[i]))