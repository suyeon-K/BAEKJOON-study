import sys
input = sys.stdin.readline
# readline 그대로 사용하면 IndexError 발생
# readline()은 개행문자(줄 바꿈 문자)를 포함하고 있기 때문에 제거해줘야 한다.
# 따라서, 오른쪽 공백을 제거해주는 rstrip 사용

a = input().rstrip()
b = input().rstrip()

# 영어 대소문자 26+26=52 
lstA = [0]*52
# lstB = [0]*52

for i,j in zip(a,b):
    if i.isupper():
        lstA[ord(i)-65] += 1  # A(65)가 0번째 인덱스
    else:
        lstA[ord(i)-71] += 1  # a(97)가 26번째 인덱스
    
    if i.isupper():
        lstA[ord(j)-65] -= 1
    else:
        lstA[ord(j)-71] -= 1


# for i in b:
#     if i.isupper():
#         lstB[ord(i)-65] += 1
#     else:
#         lstB[ord(i)-71] += 1

for i in range(52):
    if sum(lstA[i]) == 0:
        print('YES')
        break

else:
    print('NO')