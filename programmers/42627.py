import heapq

def solution(jobs):
    for i in range(len(jobs)):
        jobs[i].append(0)

    waiting_time = 0
    for i,x in enumerate(jobs):
        jobs = sorted(jobs, key=lambda x:(x[0],x[1]))
        end_time = jobs[i][0] + jobs[i][1]
        for j in range(i+1,len(jobs)):
            if jobs[j][0] <= end_time:
                jobs[j][2] += (end_time - jobs[j][0])
                jobs[j][0] = end_time

    for i in range(len(jobs)):
        waiting_time += (jobs[i][1] + jobs[i][2])

    return waiting_time//len(jobs)

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))