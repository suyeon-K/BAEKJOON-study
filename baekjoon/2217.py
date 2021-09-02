N = int(input())

min_weight = 10000

for _ in range(N):
    temp = int(input())
    if temp < min_weight:
        min_weight = temp

print(min_weight*N)
