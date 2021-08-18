# https://programmers.co.kr/learn/courses/30/lessons/42578 위장

from itertools import combinations

"""
상의 : (빨,노, 안입는 경우) 하의 : (청바지, 안입는 경우) 

(빨 상의 + 바지를 안입는 경우)
(노 상의 + 바지를 안입는 경우)
(청바지 + 상의를 안입는 경우)
(빨 상의 + 청바지)
(노 상의 + 청바지)

(2+1)*(1+1) - 1
옷추가 + 안입는 경우 = 2
"""

def solution(clothes):
    answer = 1
    clothes_dic = {}
    for _, name in clothes:
        if name in clothes_dic.keys():
            clothes_dic[name] += 1
        else:
            clothes_dic[name] = 2

    nums = list(clothes_dic.values())
    
    for x in nums:
        answer *= x

    return (answer-1)


def solution1(clothes):
    answer = 0
    clothes_dic = {}
    for x in clothes:
        if x[-1] in clothes_dic.keys():
            clothes_dic[x[-1]].append(x[0])
        else:
            clothes_dic[x[-1]] =[x[0]]

    nums = []
    for _,v in clothes_dic.items():
        nums.append(len(v))

    combi = []
    for i in range(1,len(nums)+1):
        combi.extend(list(combinations(nums,i)))
    
    for x in combi:
        temp = 1
        for y in x:
            temp *= y
        answer += temp

    return answer

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes2 = 	[["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes2))



# ----- 다른 사람 풀이 ---------

from collections import Counter
from functools import reduce

def solution(clothes):

    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer