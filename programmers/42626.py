import heapq

def solution1(scoville, K):

    def count(s, k, cnt):
        print(s)
        if min(s) >= K:
            return cnt
        if (len(s) == 1):
            return -1
        
        s.sort()
        min_1 = s.pop(0)
        min_2 = s.pop(0)

        return  count(s+[min_1+(min_2*2)],k,cnt+1)

    return count(scoville,K,0)



import heapq

def solution(scoville, K):

    answer = 0

    heapq.heapify(scoville)

    while(scoville[0] < K):
        print(scoville)
        if (len(scoville) == 1):
            return -1

        answer +=1

        min_1 = heapq.heappop(scoville)
        min_2 = heapq.heappop(scoville)
        heapq.heappush(scoville,min_1+min_2*2)

    return answer



scoville = [1, 2, 3, 9, 10, 12]
scoville2 = [1,1,1,1,1,1,1,1,1]
K = 7
print(solution1(scoville, K))
print(solution1(scoville2, K))