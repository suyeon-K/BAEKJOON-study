def solution(weights, head2head):
    answer = []

    player = []
    def rate(result):
        temp = 0
        rnd = 0
        for x in result:
            if x=="W":
                temp +=1
                rnd +=1
            elif x=="L":
                rnd +=1
    
        if rnd == 0:
            return 0
        return round(temp/rnd,2)


    for i in range(len(weights)):
        player.append([i+1, rate(head2head[i]), weights[i]])

    player = sorted(player, key=lambda)

    return answer