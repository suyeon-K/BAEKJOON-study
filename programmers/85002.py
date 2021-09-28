"""
1. 전체 승률이 높은 복서의 번호가 앞쪽으로 갑니다. 
2. 아직 다른 복서랑 붙어본 적이 없는 복서의 승률은 0%로 취급합니다.
3. 승률이 동일한 복서의 번호들 중에서는 자신보다 몸무게가 무거운 복서를 이긴 횟수가 많은 복서의 번호가 앞쪽으로 갑니다.
4. 자신보다 무거운 복서를 이긴 횟수까지 동일한 복서의 번호들 중에서는 자기 몸무게가 무거운 복서의 번호가 앞쪽으로 갑니다.
5. 자기 몸무게까지 동일한 복서의 번호들 중에서는 작은 번호가 앞쪽으로 갑니다.
"""

def solution(weights, head2head):
    answer = []
    player = []

    # 승률 계산 함수 (승률과 불리한 상황에서 이긴 횟수 리턴)
    def rate(result,i):

        win = 0  # 이긴 횟수
        rnd = 0  # 경기 횟수 (비긴 경우 제외)
        d = 0  # 불리한 상황에서 이긴 횟수

        for j, x in enumerate(result):
            if x=="W":
                win +=1
                rnd +=1

                # 불리한 상황에서 이긴 횟수 계산
                if weights[i] < weights[j]:
                    d += 1

            elif x=="L":
                rnd +=1
        
        # 모두 비긴 경우 승률 0%
        if rnd == 0:
            return (0,0)
        
        # 승률 = 이긴 횟수 / 경기 횟수(비긴 경우 제외)
        return (win/rnd,d)

    # 선수 번호, 승률, 무게를 리스트로 묶어서 player에 append
    for i in range(len(weights)):
        player.append([i+1, rate(head2head[i],i), weights[i]])

    # 승률 -> 불리한 상황에서 이긴 횟수 -> 몸무게 기준으로 정렬
    player = sorted(player, key=lambda x: (-x[1][0], -x[1][1],-x[2]))

    for x in player:
        answer.append(x[0])
    
    # return [x[0] for x in player]
    return answer

weights = [50,82,75,120]
head2head = ["NLWL","WNLL","LWNW","WWLN"]	
print(solution(weights,head2head))