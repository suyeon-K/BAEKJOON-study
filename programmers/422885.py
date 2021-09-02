def solution(people, limit):
    answer = 0
    temp = people[:]
    min_num = min(temp)
    for x in temp:
        if x > limit - min_num:
            people.remove(x)
            answer += 1

    
    return answer

people = [70, 50, 80, 50]
limit = 100
print(solution(people, limit))