def solution(array, commands):
    answer = []

    for _,x in enumerate(commands):
        temp = sorted(array[x[0]-1:x[1]])
        answer.append(temp[x[2]-1])
    return answer




array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array,commands))