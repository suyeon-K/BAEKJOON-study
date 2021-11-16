import sys

N, M = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))

f = max(lst)
b = sum(lst)

answer = b

def count_lesson(m):
    count = 0
    temp = 0

    for i,x in enumerate(lst):
        temp += x

        if temp > m:
            temp = x
            count += 1
    
    return count

while f <= b:
    m = (f+b)//2

    count = count_lesson(m)

    if count <= M-1:
        b = m - 1
        answer = min(answer,m)
    else:
        f = m + 1

print(answer)