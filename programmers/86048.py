def solution(enter, leave):
    meet = [ [] for _ in range(len(enter))]

    for x in leave:
        idx = enter.index(x)

        for y in enter[:idx+1]:
            for z in enter[:idx+1]:
                meet[y-1].append(z)
        enter.pop(idx)

    return [len(list(set(x)))-1 for x in meet]

# 들어온 순서 1 4 2 3 
# 나가는 순서 2 1 3 4 