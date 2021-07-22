N, A, B = map(int,input().split())

member = [i for i in range(1,N+1)]
team = []

for i in range(N//2):
    team.append([member[2*i],member[2*i+1]])

count = 1

while(True):

    if ([A,B] in team) or ([B,A] in team):
        break

    if len(team) == 1:
        count = -1
        break

    count += 1

    winner = []

    if len(winner)%2 == 1:
        winner.append(member[-1])

    for i in team:
        if A in i:
            winner.append(A)
        elif B in i:
            winner.append(B)
        else:
            winner.append(i[0])

    member = winner[:]
    team = []

    for i in range(len(winner)//2):
        team.append([member[2*i],member[2*i+1]])
     
  
print(count)