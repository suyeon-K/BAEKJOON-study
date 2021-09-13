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




from heapq import heappush, heappop

def solution(arguments):
    max_heap = []
    min_heap = []
    for arg in arguments:
        if arg == "D 1":
            if max_heap != []:
                heappop(max_heap)
                if max_heap == [] or -max_heap[0] < min_heap[0]:
                    min_heap = []
                    max_heap = []
        elif arg == "D -1":
            if min_heap != []:
                heappop(min_heap)
                if min_heap == [] or -max_heap[0] < min_heap[0]:
                    max_heap = []
                    min_heap = []
        else:
            num = int(arg[2:])
            heappush(max_heap, -num)
            heappush(min_heap, num)
    if min_heap == []:
        return [0, 0]
    return [-heappop(max_heap), heappop(min_heap)]