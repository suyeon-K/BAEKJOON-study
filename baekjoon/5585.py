coins_list = [500,100,50,10,5,1]

def changes(n):

    count = 0

    for x in coins_list:
        q,n = divmod(n,x)
        count += q

        if n == 0: 
            break

    return count

money = int(input())
print(changes(1000-money))


def calc_coin(i, coins_list, charge_money):
    if i == len(coins_list):
        return 0
        
    coin_cnt = charge_money//coins_list[i]
    return coin_cnt + calc_coin(i+1, coins_list, charge_money%coins_list[i])