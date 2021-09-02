
def solution(n,times):
    cases = sorted([x*(i+1) for i in range(n) for x in times])
    return cases[n-1]

"""
times = [7,10]
x = 7
n = 6
0, 7, 14, 21, ...
7, 14, 21, ....
[7,10,14,20,21,28,30,35,40,...]

"""

# 이분탐색
def solution2(n, times):
    answer = 0
    
    # 최소 시간 = 1, 최대 시간 = (오래걸리는 심사 시간 *n)
    min_time, max_time = 1, max(times) * n

    # 이분탐색 조건
    while (min_time <= max_time):

        # 타깃값과 비교할 중앙값
        # 여기서 타깃값은 입국심사가 끝나는 최적의 시간
        mid_time = (min_time+ max_time) // 2
        people = 0

        # mid 분 내에 각 심사권이 입국심사한 인원 수
        for time in times: # times = [7,10]
        
            people += mid_time // time
            # mid_time = 30
            # people = people + (30//7)
            # 30분 동안 한 심사원(7분동안 심사하는 심사원)은 총 4명의 사람을 심사할 수 있다.

            # 심사 가능한 인원수가 대기 인원보다 많은 경우(남는 시간이 없도록 mid값이 작아지게 max_time을 줄임)
            if people >= n:
                answer = mid_time
                max_time = mid_time - 1
                break
        
        # 심사 가능한 인원수가 대기 인원보다 적은 경우(mid값이 커지도록 min_time을 늘림)
        if people < n:
            min_time = mid_time + 1
            
    return answer


n = 6
times = [7,10]
print(solution(n,times))

m = 3 
times2 = [1, 2, 3] 
print(solution(m,times2))