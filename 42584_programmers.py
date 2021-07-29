def solution(prices):
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



prices = list(map(int, input().split()))
print(solution2(prices))