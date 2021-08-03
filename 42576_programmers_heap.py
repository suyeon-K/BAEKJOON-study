def solution1(participant, completion):
    answer = ''

    for _,v in enumerate(completion):
        if v in completion:
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


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))