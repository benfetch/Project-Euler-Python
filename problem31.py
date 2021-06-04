# def ways(target, coins):
#
#     largest_coin = coins[-1]
#     if largest_coin > target:
#         return ways(target, coins[0:-1])
#     if largest_coin == 1 or target == 0:
#         return 1
#     else:
#         sum = 0
#         for i in range(target//largest_coin):
#             sum += ways(target - i*largest_coin, coins[0:-1])
#         return sum
#
# coins = [1,2,5,10,20,50,100,200]
# print(ways(2,coins))

def ways(target, coins):
    c = coins[-1]

    if c == 1 or target == 1:
        return 1
    if c > target:
        return ways(target, coins[0:-1])
    else:
        return ways(target, coins[0:-1]) + ways(target - c, coins)


print(ways(200, [1,2,5,10,20,50,100,200]))
