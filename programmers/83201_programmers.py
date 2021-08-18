# 위클리 챌린지
# (상호 평가) https://programmers.co.kr/learn/courses/30/lessons/83201

from numpy.lib.function_base import average
import pandas as pd
import numpy as np

# 학점 계산 함수
def get_score(num):
    if num >= 90:
        return 'A'
    if num >= 80:
        return 'B'
    if num >= 70:
        return 'C'
    if num >= 50:
        return 'D'
    return 'F'


def solution(scores):
    answer = ''
    
    # 행렬 바꾸기
    # 원래 행 : 매긴 점수, 열 : 받은 점수 / 행 : 받은 점수, 열 : 매긴 점수
    scores_df = pd.DataFrame(scores)
    scores_t = scores_df.transpose().values.tolist()
    # scores_t = list(map(list, zip(*scores)))
    # scores_t =[ [i[j] for i in scores] for j in range(len(scores))]
    
    
    # 받은 점수를 기반으로 학점을..!
    for i, x in enumerate(scores_t):

        temp = x

        # 유일한 최대값, 최소값이면 삭제
        if x.count(x[i]) == 1:
            max_num = max(x)
            min_num = min(x)
            
            if (max_num == x[i]) or (min_num == x[i]):
                del temp[i]


        # 평균구하고 학점 구하기
        score = get_score(average(temp))
        # score = get_score(sum(temp)/len(temp))
        
        answer += score
            
    return answer

"""
    A    B    C    D    E
[A [100, 90, 98,  88,  65],
 B [50,  45, 99,  85,  77],
 C [47,  88, 95,  80,  67],
 D [61,  57, 100, 80,  65],
 E [24,  90, 94,  75,  65]]
"""

scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
scores2 = [[50,90],[50,87]]
scores3 = [[70,49,90],[68,50,38],[73,31,100]]
print(solution(scores3))