def solution(table, languages, preference):
    answer = ''

    # 직업군과 언어 분리 -> 딕셔너리로
    language_scores = {}

    for row in table:
        # "SI JAVA JAVASCRIPT SQL PYTHON C#"
        temp = row.split(" ")

        job = temp[0]
        lang = temp[1:]
        # print(lang)

        language_scores[job] = lang[::-1]
        # print(language_scores[job] )

    # languages와 preference 묶기
    language_preference = dict(zip(languages,preference))
    
    # 언어선호도 * 직업군 언어 점수
    job_scores = dict(zip(language_scores.keys(),[0 for _ in range(len(language_scores.keys()))]))

    # 나의 언어 선호도
    for l,lang_score in language_preference.items():
        # 직업별 언어 점수
        for j in language_scores.keys():
            j_score = 0
            if l in language_scores[j]:
                j_score = language_scores[j].index(l) + 1

            job_scores[j] += lang_score*j_score
            

    job_scores = sorted(job_scores.items(), key=lambda x:(-x[1],x[0]))
    # print(job_scores)
    answer = job_scores[0][0]

    return answer


# 다른풀이
def solution2(table, languages, preference):
    score = {}
    for t in table:
        for lang, pref in zip(languages, preference):
            if lang in t.split():
                score[t.split()[0]] = score.get(t.split()[0], 0) +  (6 - t.split().index(lang)) * pref
    return sorted(score.items(), key = lambda item: [-item[1], item[0]])[0][0]



table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["PYTHON", "C++", "SQL"]
preference = [7,5,5]
print(solution(table, languages, preference))

table1 = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages1 = ["JAVA", "JAVASCRIPT"]
preference1 = [7, 5]
print(solution2(table1, languages1, preference1))


fruits = {'사과':1, '바나나':3, '포도':2}
print("사과 :",fruits.get('사과',0))
print("딸기 :",fruits.get('딸기',0))