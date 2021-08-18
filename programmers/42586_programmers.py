# https://programmers.co.kr/learn/courses/30/lessons/42586 기능개발

def solution(progresses, speeds):
    answer = [1]

    days = []
    for i,v in enumerate(progresses):  # 남은날 계산
        x = (100-v)//speeds[i]

        if (100-v)%speeds[i] != 0:
            x += 1
        
        days.append(x)

    temp = days[0]
    
    for i in range(1,len(days)):  # 기능 배포 횟수
        if temp >= days[i]:
            answer[-1] += 1
        else:
            temp = days[i]
            answer.append(1)

    return answer

progresses = list(map(int,input().split()))
speeds = list(map(int,input().split()))

print(solution(progresses, speeds))