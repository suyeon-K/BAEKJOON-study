# https://programmers.co.kr/learn/courses/30/lessons/42577 전화번호 목록

# 정확도 통과 효율성 실패
def solution1(phone_book):
    answer = True

    for x in phone_book:
        for y in phone_book:
            if len(x) < len(y) and x != y :
                if y[:len(x)] == x:
                    answer = False
                    break

    return answer

# 정확도 통과 효율성 통과
def solution2(phone_book):
    answer = True

    phone_book.sort()

    for i in range(len(phone_book)-1):
        x = len(phone_book[i])
        if phone_book[i][:x] == phone_book[i+1][:x]:
            answer = False
            break


    return answer


phone_book = ["119", "97674223", "1195524421"]

print(solution2(phone_book))


# ------ 다른 풀이 --------

def solution3(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

# startswith 사용법 : https://security-nanglam.tistory.com/429