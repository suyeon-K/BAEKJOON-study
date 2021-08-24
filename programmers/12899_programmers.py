def solution(n):
    answer = ''

    dic = {0:1,1:2,2:4}

    x = 1

    while(True):
        if (n >= (3**x-1)//2) and (n < (3**(x+1)-1)//2):
            break
        x+=1
    
    n -= (3**x-1)//2

    for _ in range(x):
        # print(f"n : {n}, r : {r}")
        n,r = divmod(n,3)
        answer = str(dic[r]) + answer

    return answer



n = int(input())
print(solution(n))



def solution2(n):
    num = ['1','2','4']
    answer = ""


    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3
        
    return answer

