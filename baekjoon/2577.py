A = int(input())
B = int(input())
C = int(input())

N = A * B * C
N = str(N)

lst = [0,0,0,0,0,0,0,0,0,0]

for i in N:
    lst[int(i)] +=1
    
for i in lst:
    print(i)