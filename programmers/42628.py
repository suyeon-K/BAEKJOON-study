def solution(operations):
    answer = []
    
    q= [] 
    
    for i in range(len(operations)):
        task = operations[i][0]
        num = int(operations[i][2:])
        
        if task == "I":
            q.append(num)
        elif (task == "D") and (num == 1):
            if q:
                q.remove(max(q))
        else:
            if q:
                q.remove(min(q))
                
    
    if len(q) == 0:
        return [0,0]
    
    return [max(q),min(q)]

operations = ["I 16","D 1"]
print(solution(operations))