N,M = map(int,input().split(" "))

num = 0

for i in range(N//M+1):
    B = i
    A = N-M*i
    x = 1
    
    if B!=0:
        n = A + B
        for j in range(B):
            x *= (n-j)
        for j in range(B):
            x = x//(j+1)
    num += x
    
print(num%1000000007)
        