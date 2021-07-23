# 스택 수열 https://www.acmicpc.net/problem/1874

def sequence(num_list):

    stack = []
    idx = 0  # num_list에서 비교해야할 인덱스 위치
    num = 1  # 스택에 넣을 숫자

    while(num < len(num_list)+1): # 스택의 넣을 숫자는 리스트의 길이만큼!
        if len(stack) == 0: # 스택이 비어있으면 일단 숫자를 push 해야함
            stack.append(num)
            print("+")
            num +=1
            continue

        if stack[-1] == num_list[idx]:  # 스택의 top 숫자와 리스트에서 비교해야햘 숫자가 같으면 pop
            idx += 1  # 리스트에서 비교해야할 숫자 인덱스 + 1
            print("-")
            stack.pop()
        else:  # 비교해서 같지 않다면 숫자 push
            print("+")
            stack.append(num)
            num +=1  # 스택에 넣어줄 숫자 + 1
    
    while(len(stack)>0):  # 남은건 원하는대로 정렬된 것뿐!
        print("-")
        stack.pop()



N = int(input())
num_list = []

for _ in range(N):
    num_list.append(int(input()))

option = True  # 수열로 정렬이 가능한지 그렇지 않은지 설정하는 옵션 변수


# 수열로 만들 수 있는지 확인하는 부분
temp=[num_list[0]]

for i in range(1,N):
    if temp[-1] < num_list[i]:
        if temp[0] > num_list[i]:
            option = False
            break
        else:
            temp = []
            temp.append(num_list[i])
    else:
        temp.append(num_list[i])



if option:
    sequence(num_list)
else:
    print("NO")