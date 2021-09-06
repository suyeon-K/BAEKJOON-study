def solution(str1, str2):
    
    alpha = "abcdefghijklmnopqrstuvwxyz"
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1_set = []
    for i in range(1,len(str1)):
        for x in str1[i-1:i+1]:
            temp = []
            if x in alpha:
                temp.append(True)
            else:
                temp.append(False)
        if all(temp):
            str1_set.append(str1[i-1:i+1])

    str2_set = []
    for i in range(1,len(str1)):
        for x in str2[i-1:i+1]:
            temp = []
            if x in alpha:
                temp.append(True)
            else:
                temp.append(False)
        if all(temp):
            str1_set.append(str2[i-1:i+1])

    str1_str2_set = set(str1_set + str2_set)

    union_num = 0
    intersection_num = 0

# str1 = "aa1+aa2" -> str1_set = "aa" "aa"
# str2 = "AAAA12"  -> str2_set = "aa" "aa" "aa"
# str1_str2_set = "aa"
# union = "aa" "aa" "aa"
# intersection = "aa" "aa"
# "++","--"

    for x in str1_str2_set:
        temp1 = str1_set.count(x)  2
        temp2 = str2_set.count(x)  3

        union_num += max(temp1,temp2)
        intersection_num += min(temp1,temp2)

    if union_num == intersection_num:
        return 65536
    return (intersection_num * 65536) // union_num

str1 = "aa1+aa2"
str2 = "AAAA12"
print(solution(str1,str2))


def solution2(str1, str2):
    
    alpha = "abcdefghijklmnopqrstuvwxyz"
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1_set = [ str1[i-1:i+1] for i in range(1,len(str1)) if all( True if x in alpha else False for x in str1[i-1:i+1]) ]
    str2_set = [ str2[i-1:i+1] for i in range(1,len(str2)) if all( True if x in alpha else False for x in str2[i-1:i+1]) ]

    union_num = sum([max(str1_set.count(x),str2_set.count(x)) for x in set(str1_set + str2_set)])
    intersection_num = sum([min(str1_set.count(x),str2_set.count(x)) for x in set(str1_set + str2_set)])

    if union_num == intersection_num:
        return 65536
    return (intersection_num * 65536) // union_num

str1 = "aa1+aa2"
str2 = "AAAA12"
print(solution2(str1,str2))