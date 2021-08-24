N, K = map(int, input().split())
people = list(range(1,N+1))

del_people = []
flag = K-1

while (True):

    if(len(people) == 0 ):
        del_people.extend(list(map(str,people)))
        break

    del_people.append(str(people.pop(flag)))
    flag = (flag + K-1) % len(people)
    # print('del_people: ', del_people)
    # print('people: ', people)


print('<' + ', '.join(del_people) + '>')