'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 

Constraints:

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104
'''

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    profit = 0
    buyPrice = prices[0]
    for i in range(len(prices)):
        if i == len(prices) - 1:
            if prices[i] > buyPrice:
                profit += prices[i] - buyPrice
        elif prices[i + 1] < prices[i]:
            profit += prices[i] - buyPrice
            buyPrice = prices[i + 1]
    
    return profit
    
print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([1,2,3,4,5]))
print(maxProfit([7,6,4,3,1]))

'''
We can get the max profit if we can buy at the lowest price in the list, then sell at the highest. We get more profit buy repeating until the end of the price array
We can achieve this by checking whether we will dip below the current price or not. If so, sell the stock and buy it the next day as a "min" price
The code then checks if we reach the end, then sell if the buyPrice is less than the last day stock price to get the last amount of profit
'''