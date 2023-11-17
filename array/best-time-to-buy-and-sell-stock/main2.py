#calculate difference between low value and current value
import sys

num=list(map(int,input().split()))

def maxProfit(prices:list[int])->int:

    profit=0
    min_price=sys.maxsize

    for price in prices:

        min_price=min(min_price,price)
        profit=max(profit,price-min_price)

    return profit

print(maxProfit(num))


