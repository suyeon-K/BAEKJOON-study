def solution(priorities, location):
    answer = 0
    out = []
    lst = [chr(65+i) for i in range(len(priorities))]
    
    q = list(zip(lst,priorities))
    
    x = lst[location]

    while (len(out) != len(priorities)-1):
        max = q[1][1]
        for t in q:
            if max < t[1]:
                max = t[1]

        if q[0][1] >= max:
            out.append(q[0][0])
            del q[0]
        else:
            q.append(q[0])
            del q[0]

    out.append(q[0][0])

    for i in range(len(out)):
        if out[i] == x:
            answer = i + 1
            break

    return answer

priorities = list(map(int,input().split()))
location = int(input())

print(solution(priorities,location))