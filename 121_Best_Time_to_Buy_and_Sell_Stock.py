def maxProfit(prices: list[int]) -> int:
    min_so_far = 10001
    max_profit = 0
    for price in prices:
        if price < min_so_far:
            min_so_far = price
        else:
            profit = price - min_so_far
            max_profit = max(max_profit, profit)
    return max_profit

print(maxProfit(prices = [7,6,4,3,1]))