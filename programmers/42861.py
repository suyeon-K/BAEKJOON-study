from itertools import permutations

def solution(n, costs):
    answer = 0

    load_cost = {}
    for x in costs:
        temp = tuple(sorted([x[0],x[1]]))
        load_cost[temp] = x[2]

    nPr = list(permutations(range(n), n))

    all_case = []

    for case in nPr:
        count = 1
        cost = 0
        for i in range(1,n):
            temp = tuple(sorted([case[i-1],case[i]]))
            if temp not in load_cost.keys():
                break
            count += 1
            cost += load_cost[temp]
        if count == n:
            all_case.append(cost)

    return min(all_case)

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

print(solution(n,costs))