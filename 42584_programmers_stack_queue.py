# https://programmers.co.kr/learn/courses/30/lessons/42584 (주식가격)

def solution1(prices):
    answer = []

    for i in range(len(prices)):
        temp = prices.pop(0)
        count = 0
        for x in prices:
            if x < temp:
                count += 1
                break
            count += 1
    
        answer.append(count)

    return answer


def solution2(prices):
    answer = [0 for i in range(len(prices))]
    idx = 0
    s = []

    for price in prices:
        s.append(price)
        for i,x in enumerate(s):
            if x == None:
                continue
            if x > price:
                s[i] = None
                answer[i] = len(s)-i-1


    for i, x in enumerate(s):
        if x != None:
            answer[i] = len(prices)-1 -i

    return answer

def solution3(prices):
    answer = [0] *len(prices)

    for i in range(len(prices)):
        for x in prices[i+1:]:
            answer[i] += 1
            if x < prices[i]:
                break

    return answer

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.07ms, 10.2MB)
# 테스트 3 〉	통과 (1.37ms, 10.3MB)
# 테스트 4 〉	통과 (1.56ms, 10.2MB)
# 테스트 5 〉	통과 (1.90ms, 10.4MB)
# 테스트 6 〉	통과 (0.03ms, 10.1MB)
# 테스트 7 〉	통과 (0.90ms, 10.3MB)
# 테스트 8 〉	통과 (1.11ms, 10.3MB)
# 테스트 9 〉	통과 (0.04ms, 10.2MB)
# 테스트 10 〉	통과 (4.09ms, 10.3MB)

# 효올성 테스트 실패 : 시간초과

def solution4(prices):
    answer = [0] *len(prices)

    for i,p in enumerate(prices):
        for j in range(i+1, len(prices)):
            answer[i] += 1
            if prices[j] < p:
                break

    return answer

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.07ms, 10.1MB)
# 테스트 3 〉	통과 (0.98ms, 10.3MB)
# 테스트 4 〉	통과 (1.15ms, 10.3MB)
# 테스트 5 〉	통과 (1.40ms, 10.4MB)
# 테스트 6 〉	통과 (0.04ms, 10.2MB)
# 테스트 7 〉	통과 (0.73ms, 10.4MB)
# 테스트 8 〉	통과 (0.93ms, 10.3MB)
# 테스트 9 〉	통과 (0.05ms, 10.1MB)
# 테스트 10 〉	통과 (1.37ms, 10.4MB)

# 테스트 1 〉	통과 (140.12ms, 18.8MB)
# 테스트 2 〉	통과 (101.53ms, 17.5MB)
# 테스트 3 〉	통과 (162.72ms, 19.5MB)
# 테스트 4 〉	통과 (125.04ms, 18.2MB)
# 테스트 5 〉	통과 (82.51ms, 16.9MB)

# 시간 효율 : range < emunerate


def solution(prices):
    answer = [0] *len(prices)

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            answer[i] += 1
            if prices[j] < prices[i]:
                break

    return answer

# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.08ms, 10.1MB)
# 테스트 3 〉	통과 (1.13ms, 10.3MB)
# 테스트 4 〉	통과 (1.25ms, 10.3MB)
# 테스트 5 〉	통과 (1.40ms, 10.3MB)
# 테스트 6 〉	통과 (0.08ms, 10.2MB)
# 테스트 7 〉	통과 (1.34ms, 10.2MB)
# 테스트 8 〉	통과 (0.87ms, 10.3MB)
# 테스트 9 〉	통과 (0.05ms, 10.2MB)
# 테스트 10 〉	통과 (1.47ms, 10.3MB)

# 테스트 1 〉	통과 (153.46ms, 18.8MB)
# 테스트 2 〉	통과 (119.10ms, 17.6MB)
# 테스트 3 〉	통과 (180.13ms, 19.5MB)
# 테스트 4 〉	통과 (137.30ms, 18.2MB)
# 테스트 5 〉	통과 (85.44ms, 17MB)

prices = [1,2,3,2,3]
# prices = list(map(int, input().split()))
print(solution4(prices))