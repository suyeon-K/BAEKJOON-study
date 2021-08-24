# https://www.acmicpc.net/status?user_id=sykwak7&problem_id=1049&from_mine=1

# N = 기타줄 개수 / M = 기타줄 브랜드 개수
N, M = map(int, input().split())
g_lst = []

# 기타줄 묶음 가격과 낱개 가격
for i in range(M):
    x, y = map(int, input().split())
    g_lst.append((x,y))


# # 낱개 최소금액과 묶음 최소 금액 찾기
# min_1 =g_lst[0][1]
# min_6 =g_lst[0][0]

# for i in g_lst:
#     if min_1 > i[1]:
#         min_1 = i[1]
#     if min_6 > i[0]:
#         min_6 = i[0]

g_1 = sorted(g_lst, key= lambda x:x[1])
g_6 = sorted(g_lst)

print("g_1",g_1)
print("g_6",g_6)

min_1 =g_1[-1][1]
min_6 =g_6[-1][0]

if min_1*6 < min_6:  # 만약 묶음보다 낱개 6개 사는게 더 저렴한 경우
    min_6 = min_1*6

# 최소 지불 가격
price = 0

while(N>0):
    if N >=6:
        N-=6
        price += min_6
    else:
        if N*min_1 > min_6:  # 낱개보다 묶음이 더 저렴한 경우
            price += min_6
        else:
            price += N*min_1
        
        N = 0

print(price)

'''
안녕하세요
'''