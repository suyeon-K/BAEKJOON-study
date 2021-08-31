def solution(n, lost, reserve): # 1 ~ n
    answer = 0

    # 체육복을 갖고 있으면 True 없으면 False
    students = [False if i in lost else True for i in range(n+2)]

    reserve.sort()
    
    # 빌려줄 수 있는 사람들에 대해서 for문을 돌림
    for s in reserve: # reserve : [ 3, 4] lost [4,5]

        # 만약 여벌의 체육복을 갖고 있는 학생 중 자신의 체육복 한벌을 잃어버린 경우, 여분은 자기가 입음
        if students[s] == False:
            students[s] = True
        else:
            # 자기 앞 번호의 학생(s-1)이 체육복을 잃어버린 경우 자기(s)의 여벌 옷을 빌려줌
            if students[s-1] == False:
                students[s-1] = True
            else:
                # 자기 뒷 번호의 학생(s+1)이 체육복을 잃어버린 경우 자기(s)의 여벌 옷을 빌려줌
                if (students[s+1] == False)&((s+1 not in reserve)): # 다음 번호 학생이 옷을 잃어버렸지만 여벌옷을 갖고 있을 수도 있으므로 확인해줘야함
                    students[s+1] = True

    answer = sum(students) - 2  # 임시로 추가해둔 0번째 인덱스의 True값 빼주기

    return answer

lost = [2,4]
reserve = [1,3,5]
n = 5

n2 = 5 
lost2 = [2, 3, 4] 
reserve2 = [1, 2, 3]

# print(solution(n,lost,reserve))
print(solution(n2,lost2,reserve2))


print(sum([True,True,False]))



def solution2(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]  # 여벌 옷이 있는 학생 중 잃어버리지 않은 학생들의 번호
    _lost = [l for l in lost if l not in reserve]  # 체육복을 잃어버린 학생 중 여벌 옷이 없는 학생들의 번호
    
    # 여벌 옷이 있는 학생들에 대해서 for문을 돌림
    for r in _reserve: 
        f = r - 1  # 앞번호
        b = r + 1  # 뒷번호
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)  # 전체 학생 중 체육복을 잃어버렸는데 빌리지도 못한 학생들의 수를 뺌