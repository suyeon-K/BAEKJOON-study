T = int(input())

for i in range(1,T+1):
    N = int(input())
    P = list(map(int,input().split()))

    sale = []

    # while(N>0):
    #     temp = P.pop(0)
    #     if temp//0.75 in P:
    #         sale.append(temp)
    #         P.remove(temp//0.75)
    #         N -= 1
    
    while(len(P)>0):
        temp = P.pop(0)
        if temp//0.75 in P:
            sale.append(temp)
            P.remove(temp//0.75)

    print(f'Case #{i}: ', end = "")
    print(*sale, sep = ' ')