from itertools import combinations

def solution(clothes):
    answer = 1
    clothes_dic = {}
    for cloth, name in clothes:
        if name in clothes_dic.keys():
            clothes_dic[name] += 1
        else:
            clothes_dic[name] = 2

    nums = list(clothes_dic.values())

    print(nums)
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