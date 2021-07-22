from math import sqrt,gcd


a , b = map(int,input().split(" "))

bottom = b-a
top = int(sqrt(b)) - int(sqrt(a)) # 제곱근 개수 구하기
            
if top == 0:
    print(0)
else:
    div = gcd(top,bottom)
    print("{}/{}".format(top//div,bottom//div))