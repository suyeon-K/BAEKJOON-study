def solution(weights, head2head):
    answer = []

    player = []
    def rate(result,i):
        temp = 0
        rnd = 0
        d = 0

        for j, x in enumerate(result):
            if x=="W":
                temp +=1
                rnd +=1
                if weights[i] < weights[j]:
                    d += 1
            elif x=="L":
                rnd +=1
                
    
        if rnd == 0:
            return (0,d)
        return (round(temp/rnd,2),d)


    for i in range(len(weights)):
        player.append([i+1, rate(head2head[i],i), weights[i]])

    player = sorted(player, key=lambda x: (-x[1][0], -x[1][1],-x[2]))

    for x in player:
        answer.append(x[0])
    print(player)
    return answer

weights = [50,82,75,120]
head2head = ["NLWL","WNLL","LWNW","WWLN"]	
print(solution(weights,head2head))