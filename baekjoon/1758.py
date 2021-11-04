N = int(input())

c = []

for i in range(N):
    c.append(int(input()))

c = sorted(c, reverse=True)

tip = 0

for i,x in enumerate(c):
    temp = x - i
    if temp > 0:
        tip += temp

print(tip)

# 팁 - (순서-1)