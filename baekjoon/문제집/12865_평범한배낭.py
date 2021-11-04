# Knapsack https://huiyu.tistory.com/entry/DP-01-Knapsack%EB%B0%B0%EB%82%AD-%EB%AC%B8%EC%A0%9C

from itertools import combinations
import sys

N, K = map(int, sys.stdin.readline().split())

# things = []

# for _ in range(N):
#     W, V = map(int, input().split())
#     things.append((W,V))

things = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

things = sorted(things, key=lambda x : (x[0],-x[1]))

# temp = []
# for i in range(1,N+1):
#     for j in combinations(things,i):
#         sum_num = sum([x[0] for x in j ])
        
#         if sum_num <= K:
#             temp.append(sum([x[1] for x in j]))

temp = [sum([x[1] for x in j ]) for i in range(1,N+1) for j in combinations(things, i) if sum([x[0] for x in j ]) <= K ]

print(max(temp))