from itertools import combinations

def min_distance(rocks):
    rocks.sort()
    temp = []

    for i in range(1,len(rocks)):
        temp.append(rocks[i]-rocks[i-1])
        
    return min(temp)


def solution(distance, rocks, n):
    mins = []
    comb = combinations(rocks, n)
    
    for i,v in enumerate(comb):
        temp = rocks[:]

        for x in v:
            temp.remove(x)

        temp.append(0)
        temp.append(distance)

        num = min_distance(temp)
        mins.append(num)
    
    answer = max(mins)
    return answer

distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2
print(solution(distance,rocks,n))