def solution(a, b, g, s, w, t):

    time = 0
    city = []
    for i in range(len(g)):
        golds = []
        silvers = []
        print(g[i])
        if g[i] == 0:
            golds.append(0)
        else:
            while g[i] > 0:
                if w[i] > g[i]:
                    golds.append(g[i])
                else:
                    golds.append(w[i])
                g[i] -= w[i]

        if s[i] == 0:
            silvers.append(0)
        else:
            while s[i] > 0:
                if w[i] > s[i]:
                    silvers.append(s[i])
                else:
                    silvers.append(w[i])
                s[i] -= w[i]
                
        print((golds,silvers,t[i]))
        city.append((golds,silvers,t[i]))

    city = sorted(city, key = lambda x : x[2])
    
    g_t = 0
    s_t = 0
    
    while(a > 0 or b > 0):
        print(city)
        print()
        print("a :", a, "b :",b)


        gold = city[0][0][0]
        silver = city[0][0][0]
        
        g_idx = 0
        s_idx = 0

        g_t = city[0][2]
        s_t = city[0][2]

        for i,x in enumerate(city):
            if gold < x[0][0]:
                gold = x[0][0]
                g_t = x[2]
                g_idx = i
            if gold >= a:
                break

        for i,x in enumerate(city):
            if silver < x[0][0]:
                silver = x[0][0]
                s_t = x[2]
                s_idx = i
            if silver >= a:
                break
        
        print("gold :",gold)
        print("silver :",silver)

        a -= gold
        b -= silver
        time += (g_t + s_t)*2
        
        city[g_idx][0].pop(0)
        city[s_idx][1].pop(0)

    time -= (g_t + s_t)

    return time

print(solution(90,5000,[70,70,0],[0,0,500],[100,100,2],[4,8,1]))