# https://programmers.co.kr/learn/courses/30/lessons/42747 H-Index
# H-Index 설명 : https://namu.wiki/w/h%20%EC%9D%B8%EB%8D%B1%EC%8A%A4

def solution(citations):
    answer = 0

    # h번 이상 인용된 문서의 수가 h개 이상일 때 이 h를 h-index

    citations = sorted(citations) # 0 1 3 5 6 : 3번 이상 인용된 문서 수 3개 이상
    
    # 조건에 만족하는 가장 큰 수를 구하는 것이므로
    max_num = citations[-1] # 6

    for i in range(max_num,-1,-1):  # 6.. 5.. 4.. 3.. 2.. 1..

        # i = 3
        for count in range(1,len(citations)+1): # i번 이상 인용되었는지 확인하는 루프
            
            # 6.. 5.. 3.. 비교 (조건 만족:모두 3이상 이용되어서)-> 1일때 루프 break(3번 미만 이용되어서)
            if(citations[-count] < i):  # 인용된 횟수가 i보다 작을 때 루프문 탈출
                count -= 1
                break

        if count >= i: # 몇개가 만족하는지 확인하는 조건문
            answer = i
            break

    return answer


citations =[3, 0, 6, 1, 5]
print(solution(citations))



# ----------------- 다른 사람 풀이 -------------------


def solution1(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0


def solution2(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer