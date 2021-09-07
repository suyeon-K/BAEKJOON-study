def solution(jobs):
    for i in range(len(jobs)):
        jobs[i].append(0)

    
    for i,x in enumerate(jobs):
        jobs = sorted(jobs, key=lambda x:(x[0],x[1]))
        end_time = jobs[i][0] + jobs[i][1]
        for j in range(i+1,len(jobs)):
            if jobs[j][0] <= end_time:
                jobs[j][2] += (end_time - jobs[j][0])
                jobs[j][0] = end_time

    total_response_time = 0
    for i in range(len(jobs)):
        total_response_time += (jobs[i][1] + jobs[i][2])

    return total_response_time//len(jobs)



jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))






import heapq
from collections import deque

def solution(jobs):
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    q = []
    heapq.heappush(q, tasks.popleft())
    current_time, total_response_time = 0, 0
    while len(q) > 0:
        dur, arr = heapq.heappop(q)
        current_time = max(current_time + dur, arr + dur)
        total_response_time += current_time - arr
        while len(tasks) > 0 and tasks[0][1] <= current_time:
            heapq.heappush(q, tasks.popleft())
        if len(tasks) > 0 and len(q) == 0:
            heapq.heappush(q, tasks.popleft())
    return total_response_time // len(jobs)