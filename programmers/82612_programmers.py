# https://programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    answer = -1

    x = 0
    for i in range(count):
        x += price*(i+1)

    if money > x:
        return 0

    answer = x - money
    return answer

def solution2(price, money, count):
    return max(0, count*(price+price*count)/2-money)