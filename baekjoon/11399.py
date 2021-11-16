N = int(input())
arr = list(map(int,input().split()))

arr = sorted(arr,reverse=True)
answer = 0

for i,x in enumerate(arr):
    answer += (i+1)*x

print(answer)