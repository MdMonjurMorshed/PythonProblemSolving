def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    print(dp)

    for coin in coins:
        print('starts from this:',coin)
        for i in range(coin,amount+1):  
            dp[i] = min(dp[i],dp[i-coin]+1)
            print(dp[i])
        print(f"for coin {coin}",dp)
    return dp[amount] if dp[amount] != float('inf') else -1     

print(coin_change([2,5,4],6))