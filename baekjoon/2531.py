import sys

N, d, k, c = map(int, sys.stdin.readline().rsplit())

num = []

for _ in range(N):
    num.append(int(sys.stdin.readline()))

start_idx = 1
end_idx = k+1

max_num = len(list(set(num[start_idx:end_idx] + [c])))

while end_idx != k:
    if start_idx < end_idx:
        temp = len(list(set(num[start_idx:end_idx] + [c])))
    else:
        temp = len(list(set(num[start_idx:] + num[:end_idx] + [c])))

    max_num = max(max_num, temp)

    if end_idx == len(num):
        end_idx = 1
    else:
        end_idx += 1
    start_idx += 1

print(max_num)