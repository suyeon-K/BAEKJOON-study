from itertools import combinations

def solution(number, k):
    answer = ''
    stack = []
    for i in number:
        while len(stack)>0 and stack[-1] < int(i) and k>0:
            k-=1 
            stack.pop() 
        stack.append(int(i))   
    return "".join(map(str,stack[:len(stack)-k]))


number = "4177252841"	
k = 4
print(solution(number,k))


# def solution(number, k):
#     answer = ''
#     nCr = list(combinations(number,len(number)-k))
#     numbers = [int("".join(x)) for x in nCr]
#     return str(max(numbers))

