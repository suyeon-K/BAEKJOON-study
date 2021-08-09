# https://programmers.co.kr/learn/courses/30/lessons/42579 베스트 엘범

def solution1(genres, plays):
    answer = []

    music = list(zip(genres,enumerate(plays)))

    dic = {}

    for g, p in music:
        if g in dic.keys():
            dic[g][0] += p[1]
            dic[g].append(p)
        else:
            dic[g] = [p[0], p]

    sum_plays = sorted(dic.values(),  key=lambda x: x[0], reverse=True)

    for l in sum_plays:
        l_sort = sorted(l[1:], key=lambda x: x[1], reverse=True)

        if len(l_sort) > 1:
            answer.append(l_sort[0][0])
            answer.append(l_sort[1][0])
        else:
            answer.append(l[0][0])
    
    return answer


def solution2(genres, plays):
    answer = []
    
    musics = sorted(list(enumerate(plays)), key = lambda x : x[1], reverse=True)

    g_dic = {}

    for i, p in musics:
        genre = genres[i]
        if genre in g_dic.keys():
            g_dic[genre][0] += p
            g_dic[genre].append(i)
        else:
            g_dic[genre] = [p,i]

    g_dic = sorted(g_dic.values(), key = lambda x : x[0], reverse=True)

    for _,x in enumerate(g_dic):
        if len(x) < 3:
            answer.append(x[-1])
            continue
        answer.append(x[1])
        answer.append(x[2])

    return answer

# genres = ["classic", "pop", "classic", "classic", "pop"]
# plays = [500, 600, 150, 800, 2500]
genres =["classic", "pop", "classic", "classic","jazz","pop", "Rock", "jazz"]
plays =[500, 600, 150, 800, 1100, 2500, 100, 1000]
print(solution2(genres, plays))