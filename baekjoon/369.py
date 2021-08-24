n = int(input())
cnt = 0

for i in range(1, n+1):
    i = str(i)
    print(i)
    cnt += i.count('3')
    print(id(cnt))
    cnt += i.count('6')
    print(id(cnt))
    cnt += i.count('9')
    print(id(cnt))
    
print(cnt)