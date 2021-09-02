from itertools import product

num_list = {'1','2','3','4','5'}

global lst 
lst = []

for i in range(1,6):
    temp = list(product(num_list, repeat = i))
    for x in temp:
        lst.append(int("".join(x))/(10**i))
lst.sort()

def solution2(word):
    answer = 0
    char_int = {'A':"1", 'E':"2", 'I':"3", 'O':"4", 'U':"5"}
    word_list = list(word)
    for i in range(len(word)):
        word_list[i] = char_int[word[i]]
    word = int("".join(word_list))/(10**len(word_list))
    answer = lst.index(word) + 1
    return answer

def solution(word):
    chars = "AEIOU"
    word_list = []
    for i in range(1,6):
        temp = product(chars, repeat = i)
        for x in temp:
            word_list.append("".join(x))
    word_list = sorted(word_list)
    return word_list.index(word)+1


print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))




# 다른사람 풀이
solution = lambda word: sorted(["".join(c) for i in range(5) for c in product("AEIOU", repeat=i+1)]).index(word) + 1

solution = lambda word: sum("AEIOU".index(c) * 781 // 5 ** i + 1 for i, c in enumerate(word))