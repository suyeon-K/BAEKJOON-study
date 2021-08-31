def solution(brown, yellow):
    answer = []
    
    for b_h in range(3,brown):
        
        y_h = b_h - 2

        if(yellow%y_h) != 0:
            continue

        y_w = yellow // y_h
        
        b_w = brown//2 - b_h + 2

        if (y_w+2) == b_w:
            answer.append(b_w)
            answer.append(b_h)
            
            break
            
    return answer

brown = 24
yellow = 24
print(solution(brown,yellow))