# classic coin change problem
# search a sorted list in reverse to till we accumlate total coin value
# alternative solution is to reverse sort the list in search in order

def coinChange(totalNumber, coins):
    N = totalNumber
    coins.sort()
    index = len(coins)-1
    while True:
        coinValue = coins[index]
        if N >= coinValue:
            print(coinValue)
            N = N - coinValue
        if N < coinValue:
            index -= 1
        
        if N == 0:
            break

coins = [1,5,10,20,50,100,1000]
coinChange(122, coins)
