# https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    answer = 0
    out = []
    lst = [chr(65+i) for i in range(len(priorities))]
    
    # 문서이름과 중요도를 묶음
    q = list(zip(lst,priorities))
    
    # 인쇄를 요청한 문서
    x = lst[location]

    while (len(out) != len(priorities)-1):

        # 중요도가 가장 높은거 찾기
        max = q[1][1]
        for t in q:
            if max < t[1]:
                max = t[1]

        # 중요도 비교
        if q[0][1] >= max:
            out.append(q[0][0])  # 맨뒤로 보내기
            del q[0]
        else:
            q.append(q[0])
            del q[0]

    out.append(q[0][0])

    # 인쇄를 요청한 문서가 몇번째로 인쇄될지 찾기
    for i in range(len(out)):
        if out[i] == x:
            answer = i + 1
            break

    return answer

priorities = list(map(int,input().split()))
location = int(input())

print(solution(priorities,location))