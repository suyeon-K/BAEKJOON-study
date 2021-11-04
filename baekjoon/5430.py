from collections import deque

def solution(c,arr):
    for x in c:
        if x == 'R':
            arr = deque(list(arr)[::-1])
        elif x == 'D':
            if len(arr) == 0:
                return "error"
            arr.popleft()
        
        # print(arr)

    return list(arr)

N = int(input())

for _ in range(N):
    c = input()
    x = int(input())

    
    if x==1:
        arr = []
        arr.append(input()[1:-1])
        arr = deque(arr)
    if x==0:
        temp = input()
        arr = deque([])
    else:
        arr = list(input().split(","))
        arr[0] = arr[0][1:]
        arr[-1] = arr[-1][:-1]

        arr = deque(map(int,arr))

    print(solution(c,arr))


from collections import deque
import sys

T = int(sys.stdin.readline()) # 테스트케이스 수

err=False

for _ in range(T):  
    p = sys.stdin.readline() # 함수
    n = int(sys.stdin.readline()) # 배열 속 수의 개수
    arr = sys.stdin.readline()[1:-2].split(",")
    # print(arr)

    if arr[0] != '':
        arr = deque(arr)
    else:
        arr = deque()

    dir=True

    for i in p: # RDD
        if i == "R":
            if dir==True:
                dir = False
            elif dir==False:
                dir = True
        elif i == "D":
            if len(arr) == 0 :
                print("error")
                err = True
                break

            if dir == True:
                arr.popleft()
            elif dir==False:
                arr.pop()
      
    if p.count('R') % 2 != 0 :
        arr.reverse()
        
    if err==False:
        print("[",end="")
        for i in range(len(arr)):
            print(arr[i],end="")
            if i != len(arr)-1:
                print(",",end="")
        print("]")
        
    err=False



