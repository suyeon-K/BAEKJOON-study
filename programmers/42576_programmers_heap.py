# https://programmers.co.kr/learn/courses/30/lessons/42576 (완주하지 못한 선수)

def solution1(participant, completion):
    answer = ''

    for _,v in enumerate(completion):
        participant.remove(v)

    answer = participant[0]

    return answer
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (2.65ms, 10.3MB)
# 테스트 4 〉	통과 (8.35ms, 10.3MB)
# 테스트 5 〉	통과 (8.21ms, 10.2MB)

# 테스트 1 〉	실패 (시간 초과)
# 테스트 2 〉	실패 (시간 초과)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	실패 (시간 초과)
# 테스트 5 〉	실패 (시간 초과)


def solution2(participant, completion):
    answer = ''

    for _,v in enumerate(completion):
        if v not in completion:
            answer = v
            break
        participant.remove(v)

    if len(participant) != 0:
        answer = participant[0]

    return answer
# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (2.49ms, 10.2MB)
# 테스트 4 〉	통과 (10.23ms, 10.3MB)
# 테스트 5 〉	통과 (8.16ms, 10.2MB)
# 테스트 1 〉	실패 (시간 초과)
# 테스트 2 〉	실패 (시간 초과)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	실패 (시간 초과)
# 테스트 5 〉	실패 (시간 초과)

def solution3(participant, completion):
    answer = ''

    for _, x in enumerate(participant):
        if x in completion:
            completion.remove(x)
        else:
            answer = x
            break

    return answer

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i,v in enumerate(participant):
        if i >= len(completion) or (v != completion[i]) :
            answer = v
            break

    return answer


"""

A A C D

A C D


"""



participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))

# --------------- other solutions --------------------


import collections


def solution4(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


def solution5(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

def solution6(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]