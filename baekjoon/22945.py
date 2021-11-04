# (개발자 A와 개발자 B 사이에 존재하는 다른 개발자 수) × min(개발자 A의 능력치, 개발자 B의 능력치)
# 1 4 2 5
N = int(input())
en = list(map(int,input().split()))

left_idx = 0
right_idx = N-1

score = 0

while left_idx < right_idx:

    temp = (right_idx - left_idx - 1)*min(en[left_idx],en[right_idx])

    if temp > score:
        score = temp

    if en[left_idx] < en[right_idx]:
        left_idx += 1
    else:
        right_idx -= 1

print(score)