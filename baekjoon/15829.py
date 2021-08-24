z = [0]*26
a = [chr(i) for i in range(97,123)]

dic = dict(zip(a,z))

L = int(input())
st = input()
sum_num = 0

for c in st:
    sum_num += (ord(c)-96) * (31 ** dic[c])
    dic[c] += 1

print(sum_num % 1234567891)